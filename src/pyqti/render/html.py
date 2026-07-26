"""Render a QTI item body to HTML.

**How.** Rather than walking the generated dataclasses, this consumes xsdata's own
serialisation event stream --- ``EventGenerator.generate(obj)`` yields
``(START, qname) / (ATTR, qname, value) / (DATA, text) / (END, qname)``. That comes
with correct document-ordered mixed content and wildcard handling for free, which is
exactly the part most likely to have subtle bugs if hand-written: renderable QTI
containers use two incompatible shapes (block-only compound ``Elements`` fields, and
``content: list[object]`` mixed wildcards), and ``SimpleChoiceDType`` is the second
kind. ``TreeSerializer`` would be the obvious alternative but requires lxml, which
this project avoids for memory reasons.

QTI puts its HTML-ish elements in the *QTI* namespace rather than XHTML, so reducing
every qname to its local name yields ``p``, ``em``, ``strong``,
``qti-choice-interaction``, ``qti-simple-choice`` directly.

**Two decisions worth understanding before changing anything here.**

1. ``ignore_default_attributes`` must stay ``False``. xsdata's ``next_attribute``
   skips any attribute whose value equals its field default, so turning it on
   silently drops ``max-choices="1"`` --- 1 being the XSD default --- along with
   ``shuffle``, ``orientation``, ``fixed``, ``show-hide`` and ``dir``. The front end
   would then be unable to tell a single-answer interaction from a multi-select. The
   price of leaving it off is the ~24 ARIA attributes every element inherits from
   ``AriabaseDType``, which is why attributes are filtered by an explicit allowlist.

2. Unknown elements **raise**. An allowlist renderer that silently skipped content it
   did not recognise would drop a question's diagram or a table of data and the
   candidate would answer the wrong question. For an assessment engine that is a
   correctness and fairness failure, not a cosmetic one. Growing
   :data:`ALLOWED_ELEMENTS` is a deliberate act, one fixture at a time.
"""

from __future__ import annotations

from html import escape
from typing import Any

from xsdata.formats.dataclass.serializers.mixins import EventGenerator, XmlWriterEvent

from pyqti._xsdata import CONTEXT, RENDER_SERIALIZER_CONFIG, XSI_NAMESPACE
from pyqti.errors import UnsupportedContentError, UnsupportedQtiFeature
from pyqti.qtitree import local_name

#: HTML elements that never have a closing tag.
VOID_ELEMENTS = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "source",
        "track",
        "wbr",
    }
)

#: QTI custom elements passed straight through for the front end to upgrade.
QTI_ELEMENTS = frozenset(
    {
        "qti-choice-interaction",
        "qti-simple-choice",
        "qti-prompt",
    }
)

#: HTML content elements the renderer knows how to emit.
HTML_ELEMENTS = frozenset(
    {
        "a",
        "abbr",
        "b",
        "blockquote",
        "br",
        "caption",
        "cite",
        "code",
        "col",
        "colgroup",
        "dd",
        "del",
        "dfn",
        "div",
        "dl",
        "dt",
        "em",
        "figcaption",
        "figure",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "hr",
        "i",
        "img",
        "ins",
        "kbd",
        "li",
        "ol",
        "p",
        "pre",
        "q",
        "samp",
        "small",
        "span",
        "strong",
        "sub",
        "sup",
        "table",
        "tbody",
        "td",
        "tfoot",
        "th",
        "thead",
        "tr",
        "ul",
        "var",
    }
)

ALLOWED_ELEMENTS = QTI_ELEMENTS | HTML_ELEMENTS

#: Attributes allowed on any element.
GLOBAL_ATTRIBUTES = frozenset({"class", "id", "lang", "dir", "title"})

#: Attributes allowed on specific elements. Everything else --- notably the ARIA
#: flood inherited from ``AriabaseDType`` --- is dropped.
ELEMENT_ATTRIBUTES: dict[str, frozenset[str]] = {
    "qti-choice-interaction": frozenset(
        {"response-identifier", "max-choices", "min-choices", "shuffle", "orientation"}
    ),
    "qti-simple-choice": frozenset({"identifier", "fixed", "show-hide"}),
    "a": frozenset({"href", "target", "rel"}),
    "img": frozenset({"src", "alt", "width", "height", "longdesc"}),
    "td": frozenset({"colspan", "rowspan", "headers", "scope"}),
    "th": frozenset({"colspan", "rowspan", "headers", "scope", "abbr"}),
    "col": frozenset({"span"}),
    "colgroup": frozenset({"span"}),
    "ol": frozenset({"type", "start", "reversed"}),
    "del": frozenset({"cite", "datetime"}),
    "ins": frozenset({"cite", "datetime"}),
    "q": frozenset({"cite"}),
    "blockquote": frozenset({"cite"}),
}

#: Attributes to drop when they hold a specific value.
#:
#: Because ``ignore_default_attributes`` is off (see the module docstring), every XSD
#: default reaches the emitter. Most are pure noise: ``dir="auto"`` would appear on
#: literally every element, and ``fixed``/``show-hide`` only mean anything in their
#: non-default state. Attributes the front end actually reads --- ``max-choices``,
#: ``min-choices``, ``shuffle``, ``orientation`` --- are deliberately *not* listed
#: here, so they are emitted even when they equal the schema default.
SUPPRESS_WHEN: dict[str, str] = {
    "dir": "auto",
    "fixed": "false",
    "show-hide": "show",
}

#: The root element of an item body arrives under its *type* name, because
#: ``qti-item-body``'s element name lives on the parent field rather than the class.
_ITEM_BODY_TYPE_NAMES = frozenset({"ItemBodyDType", "qti-item-body"})


def _format_attribute_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, list | tuple):
        return " ".join(_format_attribute_value(item) for item in value)
    return str(getattr(value, "value", value))


def _check_interaction_supported(attrs: dict[str, str]) -> None:
    """Refuse choice interactions this slice cannot faithfully render.

    Rendering a shuffled interaction unshuffled, or a multi-select as radio buttons,
    would present the candidate with a different question than the item author wrote.
    Better to refuse than to quietly disagree with the content.
    """
    if attrs.get("shuffle") == "true":
        raise UnsupportedContentError(
            'qti-choice-interaction/@shuffle="true" is not implemented yet '
            "(it needs stable per-session ordering)"
        )

    max_choices = attrs.get("max-choices")
    if max_choices is not None and max_choices != "1":
        raise UnsupportedContentError(
            f"qti-choice-interaction/@max-choices={max_choices!r} is not implemented "
            "yet; only single-answer (max-choices=1) is supported"
        )


class _HtmlEmitter:
    """Turns an xsdata event stream into an HTML string."""

    def __init__(self, *, wrapper_class: str | None) -> None:
        self.wrapper_class = wrapper_class
        self.parts: list[str] = []
        self.open_tags: list[str | None] = []
        self.pending: tuple[str, dict[str, str]] | None = None
        self.depth = 0

    # -- element/attribute plumbing ------------------------------------- #

    def _flush_pending(self) -> None:
        if self.pending is None:
            return
        tag, attrs = self.pending
        self.pending = None

        if tag == "qti-choice-interaction":
            _check_interaction_supported(attrs)

        rendered = "".join(
            f' {name}="{escape(value, quote=True)}"' for name, value in attrs.items()
        )
        if tag in VOID_ELEMENTS:
            self.parts.append(f"<{tag}{rendered}>")
            self.open_tags.append(None)
        else:
            self.parts.append(f"<{tag}{rendered}>")
            self.open_tags.append(tag)

    def start(self, qname: str) -> None:
        self._flush_pending()
        name = local_name(qname)
        self.depth += 1

        # The outermost element is the item body itself; it is replaced by a wrapper
        # (or nothing) rather than emitted as an unknown tag.
        if self.depth == 1 and name in _ITEM_BODY_TYPE_NAMES:
            if self.wrapper_class is None:
                self.open_tags.append(None)
            else:
                self.parts.append(f'<div class="{escape(self.wrapper_class)}">')
                self.open_tags.append("div")
            return

        if name not in ALLOWED_ELEMENTS:
            raise UnsupportedContentError(
                f"<{name}> is not supported by the HTML renderer yet"
            )

        self.pending = (name, {})

    def attribute(self, qname: str, value: Any) -> None:
        if self.pending is None:
            return
        namespace, name = _split(qname)
        if namespace == XSI_NAMESPACE:
            return

        tag, attrs = self.pending
        allowed = GLOBAL_ATTRIBUTES | ELEMENT_ATTRIBUTES.get(tag, frozenset())
        if name not in allowed:
            return

        formatted = _format_attribute_value(value)
        if formatted == "" or SUPPRESS_WHEN.get(name) == formatted:
            return
        attrs[name] = formatted

    def data(self, text: Any) -> None:
        self._flush_pending()
        if text is None:
            return
        # quote=False keeps apostrophes readable; attribute values escape separately.
        self.parts.append(escape(str(text), quote=False))

    def end(self, qname: str) -> None:
        self._flush_pending()
        self.depth -= 1
        tag = self.open_tags.pop() if self.open_tags else None
        if tag is not None:
            self.parts.append(f"</{tag}>")

    def result(self) -> str:
        self._flush_pending()
        return "".join(self.parts)


def _split(qname: str) -> tuple[str | None, str]:
    if qname.startswith("{"):
        namespace, _, name = qname[1:].partition("}")
        return namespace, name
    return None, qname


def render_item_body_html(
    item_body: Any,
    *,
    session: Any | None = None,
    wrapper_class: str | None = "qti-item-body",
) -> str:
    """Render a ``qti-item-body`` model to an HTML fragment.

    QTI-specific elements are emitted as custom elements (``<qti-choice-interaction>``,
    ``<qti-simple-choice>``) for the front end to upgrade, which is the seam the
    README's "web components for the qti-item-body" approach needs. A React
    implementation later replaces the element definition, not this function.

    ``session`` is accepted and currently unused. Feedback (``qti-feedback-block``,
    ``show-hide``, the ``FEEDBACK`` outcome) has to be rendered *after* response
    processing with outcome state in hand, and adding the parameter later would touch
    every call site including the HTTP layer.

    Raises :class:`~pyqti.errors.UnsupportedContentError` for any element not in
    :data:`ALLOWED_ELEMENTS`.
    """
    if item_body is None:
        return ""

    emitter = _HtmlEmitter(wrapper_class=wrapper_class)
    generator = EventGenerator(context=CONTEXT, config=RENDER_SERIALIZER_CONFIG)

    for event, *args in generator.generate(item_body):
        if event == XmlWriterEvent.START:
            emitter.start(*args)
        elif event == XmlWriterEvent.ATTR:
            emitter.attribute(*args)
        elif event == XmlWriterEvent.DATA:
            emitter.data(*args)
        elif event == XmlWriterEvent.END:
            emitter.end(*args)
        else:  # pragma: no cover - xsdata would have to add an event type
            raise UnsupportedQtiFeature(f"unexpected xsdata event {event!r}")

    return emitter.result()
