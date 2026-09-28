"""An XBlock that delivers and grades a single QTI 3.0 assessment item.

The block registers the OLX tag ``openedx-qti``. Its attributes are the
platform's (``url_name``, ``display_name``, ``max_attempts``, ...) and its only
child is the item, as real QTI, so the two vocabularies never share an
element::

    <openedx-qti display_name="Unattended Luggage" max_attempts="2">
      <qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
                           identifier="luggage" title="Unattended Luggage" ...>
        ...
      </qti-assessment-item>
    </openedx-qti>

Course export writes that element to ``openedx-qti/{url_name}.xml`` and leaves
only ``<openedx-qti url_name="..."/>`` in the parent, as the platform's
built-in blocks do; see :meth:`QtiAssessmentItemBlock.export_to_file`.

**pyqti does not render, and neither does this block.** Presentation is
delegated to Citolab's QTI web components in the browser; the block serves them
a *redacted* copy of the item via :func:`pyqti.redaction.presentation_xml` and
does every bit of scoring server-side, against the authoritative copy that never
leaves the server. Nothing here may produce item XML by any other route.

Two dependency notes:

* ``lxml`` is used only for the OLX hooks, because that is what the runtime
  hands us. pyqti's core stays lxml-free, deliberately (see ``README.md``).
* ``xblock.utils`` is *not* used, because importing it requires Django. Keeping
  this module Django-free means the block can be unit-tested with nothing but
  ``XBlock`` installed, and keeps ``pyqti[xblock]`` from dragging a web
  framework into a library with one dependency. The cost is a hand-rolled
  Studio editor, which is a textarea.
"""

from __future__ import annotations

import copy
import hashlib
import logging
from functools import lru_cache
from importlib.resources import files
from typing import Any

try:
    from lxml import etree
    from web_fragments.fragment import Fragment
    from webob import Response
    from xblock.core import XBlock
    from xblock.exceptions import JsonHandlerError
    from xblock.fields import Boolean, Dict, Float, Integer, Scope, String
    from xblock.scorable import ScorableXBlockMixin, Score
except ImportError as exc:  # pragma: no cover - exercised by the packaging tests
    # The xblock.v1 entry point is present in package metadata even when the
    # extra is not installed, and some Studio paths eagerly import every
    # registered block via Plugin.load_classes(fail_silently=True). That call
    # swallows this exception, so the message is the only thing an operator
    # ever sees -- make it name the fix.
    raise ImportError(
        "pyqti's XBlock support requires the optional 'xblock' extra: "
        "install it with `pip install pyqti[xblock]`."
    ) from exc

from pyqti._xsdata import QTI_NAMESPACE
from pyqti.errors import (
    PyQtiError,
    QtiStructureError,
    QtiTypeError,
    UnsupportedQtiFeature,
)
from pyqti.item import ItemDefinition
from pyqti.loading import load_assessment_item
from pyqti.redaction import presentation_xml
from pyqti.session import NOT_ATTEMPTED, ItemSession

log = logging.getLogger(__name__)

#: Pinned, and matching the demo harness. Overridable per usage so that an
#: operator behind a strict CSP, or with no outbound network at all, can serve
#: the components themselves. See ``components_url``.
CITOLAB_VERSION = "7.28.1"
DEFAULT_COMPONENTS_URL = (
    f"https://cdn.jsdelivr.net/npm/@citolab/qti-components@{CITOLAB_VERSION}"
)

#: The OLX tag, which is the ``xblock.v1`` entry point's name.
OLX_TAG = "openedx-qti"
QTI_ROOT = "qti-assessment-item"
_QUALIFIED_ROOT = f"{{{QTI_NAMESPACE}}}{QTI_ROOT}"
#: Put on the OLX node by the runtime; not fields of this block.
_RUNTIME_ATTRIBUTES = frozenset({"url_name", "xblock-family"})


def _definition_path(url_name: str) -> str:
    """Where course export keeps a block's definition, relative to the course."""
    return f"{OLX_TAG}/{url_name}.xml"


def _is_pointer(node: Any) -> bool:
    """``<openedx-qti url_name="..."/>``: a name and nothing else."""
    return (
        set(node.attrib) == {"url_name"}
        and len(node) == 0
        and not (node.text or "").strip()
    )


def _asset(name: str) -> str:
    return files("pyqti.xblock.static").joinpath(name).read_text(encoding="utf-8")


@lru_cache(maxsize=32)
def _parse(qti_xml: str) -> Any:
    """Parse once per distinct item.

    Parsing is by far the expensive step (the generated models are large) and is
    a pure function of the source, so it caches well across requests and across
    learners. The redacted copy is *not* cached: ``presentation_xml`` deep-copies
    before redacting, so sharing the parsed model between callers is safe, and
    re-serialising a redacted tree is cheap next to re-parsing.
    """
    return load_assessment_item(qti_xml)


def _localname(tag: Any) -> str:
    if not isinstance(tag, str):
        return ""
    return tag.rsplit("}", 1)[-1]


def _qualify(node: Any) -> Any:
    """Put a bare OLX subtree into the QTI namespace.

    QTI 3.0 puts its shared HTML vocabulary (``p``, ``em``, ...) in the QTI
    namespace too, so every unprefixed element belongs there. Elements that
    already carry a namespace -- MathML, most obviously -- are left alone.
    """
    qualified = copy.deepcopy(node)
    for element in qualified.iter():
        if isinstance(element.tag, str) and not element.tag.startswith("{"):
            element.tag = f"{{{QTI_NAMESPACE}}}{element.tag}"
    return qualified


def _qti_child(node: Any) -> Any:
    """The ``<qti-assessment-item>`` inside ``<openedx-qti>``, or None if empty.

    A block with no item yet is legitimate --- it is what Studio creates --- but
    anything else in the wrapper is refused rather than dropped.
    """
    stray = (node.text or "") + "".join(child.tail or "" for child in node)
    elements = [child for child in node if isinstance(child.tag, str)]
    if stray.strip() or len(elements) > 1 or (
        elements and _localname(elements[0].tag) != QTI_ROOT
    ):
        found = ", ".join(f"<{_localname(child.tag)}>" for child in elements)
        raise QtiStructureError(
            f"<{OLX_TAG}> must contain exactly one <{QTI_ROOT}> and nothing "
            f"else; found {found or 'text'}"
        )
    return elements[0] if elements else None


def _qti_source(node: Any) -> tuple[str, bool]:
    """Recover QTI XML from an OLX node, tolerating either shape.

    Authors may declare the QTI namespace (a file that is valid QTI as it
    stands, which is the point of registering this tag) or leave it off in the
    usual namespace-free OLX style. Both are accepted; which one was used is
    recorded so that export round-trips to the shape the author wrote.
    """
    if _localname(node.tag) != QTI_ROOT:
        raise QtiStructureError(
            f"expected a <{QTI_ROOT}> root element, got <{_localname(node.tag)}>"
        )

    declared = node.tag == _QUALIFIED_ROOT
    source = node if declared else _qualify(node)
    xml = etree.tostring(source, encoding="unicode", with_tail=False)
    return xml, declared


class QtiAssessmentItemBlock(ScorableXBlockMixin, XBlock):
    """A single QTI 3.0 item, delivered redacted and graded server-side."""

    has_score = True
    icon_class = "problem"
    # QTI children are item content, never child blocks. The inherited
    # parse_xml would otherwise try to build an XBlock out of every <p>.
    has_children = False

    display_name = String(
        display_name="Display Name",
        help="Shown in the unit navigation. Defaults to the item's QTI title.",
        default="QTI Item",
        scope=Scope.settings,
    )

    # --- Authored content -------------------------------------------------
    qti_xml = String(
        display_name="QTI",
        help="The QTI 3.0 assessment item. This is the authoritative copy and "
        "is never sent to a browser as authored.",
        default="",
        scope=Scope.content,
        multiline_editor=True,
    )
    qti_namespace_declared = Boolean(
        help="Whether the author declared the QTI namespace, so that OLX export "
        "round-trips to the shape they wrote.",
        default=True,
        scope=Scope.content,
    )

    # --- Per-usage policy -------------------------------------------------
    max_attempts = Integer(
        display_name="Maximum attempts",
        help="0 means unlimited. QTI puts attempt limits on the test rather "
        "than the item, so this is the platform's setting, not the item's.",
        default=0,
        scope=Scope.settings,
    )
    weight = Float(
        display_name="Problem weight",
        help="How much this problem contributes to the subsection score. "
        "Unrelated to QTI's own test-level weighting, which pyqti does not "
        "implement.",
        default=1.0,
        scope=Scope.settings,
    )
    raw_possible_override = Float(
        display_name="Maximum score",
        help="Use when the item does not declare a MAXSCORE outcome and its "
        "SCORE is not on a 0..1 scale.",
        default=None,
        scope=Scope.settings,
    )
    show_score_immediately = Boolean(
        display_name="Show the score on submit",
        help="Turn off for high-stakes delivery: returning the score on every "
        "submission hands the candidate an oracle to probe.",
        default=True,
        scope=Scope.settings,
    )
    components_url = String(
        display_name="QTI components base URL",
        help="Where to load the QTI web components from. Point this at a "
        "self-hosted copy for offline or CSP-restricted deployments.",
        default=DEFAULT_COMPONENTS_URL,
        scope=Scope.settings,
    )

    # --- Durable per-learner state ---------------------------------------
    # This is the half ItemSession deliberately does not provide: it is
    # in-memory and per-request. See TODO.md section 5.
    num_attempts = Integer(default=0, scope=Scope.user_state)
    raw_responses = Dict(default={}, scope=Scope.user_state)
    raw_earned = Float(default=None, scope=Scope.user_state)
    raw_possible = Float(default=None, scope=Scope.user_state)
    completion_status = String(default=NOT_ATTEMPTED, scope=Scope.user_state)
    shuffle_seed = String(default="", scope=Scope.user_state)

    editable_fields = (
        "display_name",
        "qti_xml",
        "max_attempts",
        "weight",
        "raw_possible_override",
        "show_score_immediately",
        "components_url",
    )

    # ------------------------------------------------------------------ #
    # Authoring: OLX and Studio share one validated store
    # ------------------------------------------------------------------ #

    def _store_qti(self, qti_xml: str) -> None:
        """Normalise, validate on the same path grading will use, then store.

        Every authoring route goes through here --- OLX import and the Studio
        editor alike --- so "accepted" is a real guarantee rather than a syntax
        check, and both accept QTI with or without its namespace declared. An
        item that cannot be compiled, or cannot be safely redacted, must fail at
        authoring time; failing at exam time instead is the whole thing pyqti
        exists to avoid.
        """
        try:
            node = etree.fromstring(qti_xml.encode("utf-8"))
        except etree.XMLSyntaxError as exc:
            raise QtiStructureError(f"not well-formed XML: {exc}") from exc

        qti_xml, namespace_declared = _qti_source(node)
        item = ItemDefinition.from_model(load_assessment_item(qti_xml))

        # Refuse what redaction would silently hollow out. Template processing
        # is cleared by redact_for_delivery, so an item that depends on it would
        # reach the candidate as a degraded, misleading version of itself.
        model = item.model
        if getattr(model, "qti_template_declaration", None) or getattr(
            model, "qti_template_processing", None
        ):
            raise UnsupportedQtiFeature(
                "this item uses QTI template processing, which pyqti does not "
                "implement server-side yet"
            )

        # Compiles response processing; raises on unsupported rules/expressions.
        ItemSession(item)
        # Raises if redaction has no decision for some field of the item.
        presentation_xml(model)

        self.qti_xml = qti_xml
        self.qti_namespace_declared = namespace_declared

        self.display_name = item.title

    @classmethod
    def parse_xml(cls, node, runtime, keys):
        """Read ``<openedx-qti>``: settings from its attributes, QTI from its child."""
        block = runtime.construct_xblock_from_class(cls, keys)

        node = cls._follow_pointer(node, runtime)
        qti = _qti_child(node)
        if qti is not None:
            block._store_qti(etree.tostring(qti, encoding="unicode", with_tail=False))

        # After _store_qti, which defaults display_name to the item's title, so
        # that an explicit display_name attribute wins.
        for name, value in node.attrib.items():
            if name in _RUNTIME_ATTRIBUTES:
                continue
            field = cls.fields.get(name)
            if field is None or field.scope != Scope.settings:
                # Ignored with a warning, as XBlock core does. Content and
                # learner state are never set this way: qti_xml in particular
                # must only ever arrive through _store_qti.
                log.warning(
                    "pyqti: ignoring <%s> attribute %r, which is not a setting",
                    OLX_TAG,
                    name,
                )
                continue
            setattr(block, name, field.from_string(value))
        return block

    @classmethod
    def _follow_pointer(cls, node, runtime):
        """Swap a course export's pointer for the definition file it names.

        Only when that file exists. The same shape is also an inline block with
        no item and no settings yet, and outside course import there is no such
        file: the split modulestore's ``resources_fs`` is a per-course scratch
        directory, the content library runtime's an empty stand-in.
        """
        if not _is_pointer(node):
            return node
        resources_fs = getattr(runtime, "resources_fs", None)
        path = _definition_path(node.get("url_name"))
        if resources_fs is None or not resources_fs.exists(path):
            if resources_fs is not None:
                log.warning("pyqti: no %s; importing an empty block", path)
            return node

        with resources_fs.open(path, "rb") as definition_file:
            # Our parser, not the platform's: it strips blank text, and
            # whitespace between inline elements in an item body renders.
            definition = etree.fromstring(definition_file.read())
        if definition.tag != OLX_TAG:
            raise QtiStructureError(
                f"{path}: expected a <{OLX_TAG}> root element, "
                f"got <{_localname(definition.tag)}>"
            )
        return definition

    def _definition(self) -> Any:
        """This block as an ``<openedx-qti>`` element.

        Every explicitly set settings field becomes an attribute, not just this
        block's own: the platform mixes in fields such as
        ``visible_to_staff_only`` and ``group_access``, and an export that
        dropped those would silently loosen access on re-import. The QTI goes
        back out in the shape the author wrote it.
        """
        definition = etree.Element(OLX_TAG)
        for name, field in sorted(self.fields.items()):
            if field.scope != Scope.settings or not field.is_set_on(self):
                continue
            value = field.to_string(field.read_from(self))
            if value is not None:
                definition.set(name, value)

        if self.qti_xml:
            source = etree.fromstring(self.qti_xml.encode("utf-8"))
            if not self.qti_namespace_declared:
                for element in source.iter():
                    if isinstance(element.tag, str):
                        element.tag = _localname(element.tag)
                etree.cleanup_namespaces(source)
            definition.append(source)
        return definition

    def export_to_file(self) -> bool:
        """Whether course export writes this block to a file of its own.

        It does, as the platform's built-in blocks do. edx-platform's library
        and clipboard serializer needs one self-contained node instead, and
        gets it by overriding this on the instance to return False.
        """
        return True

    def add_xml_to_node(self, node) -> None:
        """Export as ``<openedx-qti>``, to its own file when the runtime allows.

        That takes a filesystem and a ``url_name``, which edx-platform's course
        export provides and other runtimes do not; without them, and whenever
        :meth:`export_to_file` says no, the node is written inline.
        """
        definition = self._definition()
        export_fs = getattr(self.runtime, "export_fs", None)
        url_name = node.get("url_name")
        if self.export_to_file() and export_fs is not None and url_name:
            export_fs.makedirs(OLX_TAG, recreate=True)
            with export_fs.open(_definition_path(url_name), "wb") as definition_file:
                # Not pretty-printed, unlike the platform's own files: indenting
                # an item with no whitespace of its own (generated or minified
                # QTI) puts some between inline elements, and that renders.
                definition_file.write(
                    etree.tostring(definition, encoding="utf-8", xml_declaration=True)
                )
                definition_file.write(b"\n")
            node.tag = OLX_TAG
            return

        node.tag = definition.tag
        node.attrib.update(definition.attrib)
        node.extend(definition)

    # ------------------------------------------------------------------ #
    # Item access
    # ------------------------------------------------------------------ #

    def _item(self) -> ItemDefinition:
        return ItemDefinition.from_model(_parse(self.qti_xml))

    def _session(self) -> ItemSession:
        """A session that knows how many attempts this candidate has had.

        Built fresh per request, because ItemSession holds no durable state ---
        the XBlock field store is what persists. ``prior_attempts`` is what keeps
        response processing that reads ``numAttempts`` from seeing every attempt
        as the first.
        """
        return ItemSession(self._item(), prior_attempts=self.num_attempts)

    def _seed(self) -> str:
        """A per-learner, per-usage shuffle seed, fixed on first render.

        Citolab reorders choices client-side from this, deterministically, so
        the candidate sees a stable order across reloads while different
        candidates see different ones.
        """
        if not self.shuffle_seed:
            anonymous = getattr(self.runtime, "anonymous_student_id", None) or "anon"
            usage = str(getattr(self.scope_ids, "usage_id", "usage"))
            digest = hashlib.sha256(f"{anonymous}:{usage}".encode())
            self.shuffle_seed = digest.hexdigest()[:16]
        return self.shuffle_seed

    # ------------------------------------------------------------------ #
    # Views
    # ------------------------------------------------------------------ #

    def student_view(self, context=None):  # noqa: ARG002 - runtime contract
        fragment = Fragment()
        if not self.qti_xml:
            fragment.add_content(
                '<div class="pyqti-block"><p>This problem has no QTI item '
                "yet.</p></div>"
            )
            return fragment

        fragment.add_content(
            '<div class="pyqti-block">'
            '  <form class="pyqti-form">'
            "    <qti-item><item-container></item-container></qti-item>"
            '    <button type="submit" class="pyqti-submit">Submit</button>'
            "  </form>"
            '  <output class="pyqti-result" hidden></output>'
            "</div>"
        )
        fragment.add_css(_asset("qti-xblock.css"))
        fragment.add_javascript(_asset("qti-xblock.js"))
        fragment.initialize_js(
            "QtiAssessmentItemBlock",
            {
                "componentsUrl": self.components_url,
                "seed": self._seed(),
                "attemptsUsed": self.num_attempts,
                "attemptsAllowed": self.max_attempts,
            },
        )
        return fragment

    def author_view(self, context=None):
        return self.student_view(context)

    def studio_view(self, context=None):  # noqa: ARG002 - runtime contract
        fragment = Fragment()
        fragment.add_content(
            '<div class="pyqti-studio">'
            "  <label>QTI 3.0 item"
            '    <textarea class="pyqti-xml" spellcheck="false">'
            f"{_escape(self.qti_xml)}</textarea>"
            "  </label>"
            '  <p class="pyqti-studio-note">Edit &lt;qti-assessment-item&gt; XML here. '
            'The item is validated on save.</p>'
            '  <div class="pyqti-studio-error" hidden></div>'
            '  <button class="pyqti-studio-save">Save</button>'
            "</div>"
        )
        fragment.add_css(_asset("qti-xblock.css"))
        fragment.add_javascript(_asset("qti-xblock.js"))
        fragment.initialize_js("QtiAssessmentItemStudio")
        return fragment

    # ------------------------------------------------------------------ #
    # Handlers
    # ------------------------------------------------------------------ #

    @XBlock.handler
    def item_xml(self, request, suffix=""):  # noqa: ARG002 - runtime contract
        """Serve the redacted item.

        This function is the only thing in the block that emits item XML, and
        everything it can reach is already redacted. Keeping it this narrow is
        itself a control: there is no branch here that could serve the
        authoritative copy by accident.
        """
        try:
            xml = presentation_xml(_parse(self.qti_xml))
        except PyQtiError:
            log.exception(
                "pyqti: cannot redact item for usage %s", self.scope_ids.usage_id
            )
            return Response(status=500, json_body={"error": "item unavailable"})
        return Response(
            body=xml.encode("utf-8"),
            content_type="application/xml",
            charset="utf-8",
        )

    @XBlock.json_handler
    def submit_response(self, data, suffix=""):  # noqa: ARG002 - runtime contract
        responses = data.get("responses")
        if not isinstance(responses, dict):
            raise JsonHandlerError(400, "responses must be a JSON object")

        # Enforced before pyqti is touched at all: ItemSession has no concept of
        # a policy limit, only a counter.
        if self.max_attempts and self.num_attempts >= self.max_attempts:
            raise JsonHandlerError(403, "No attempts remaining.")

        try:
            session = self._session()
        except UnsupportedQtiFeature:
            log.exception(
                "pyqti: item for usage %s cannot be compiled for grading",
                self.scope_ids.usage_id,
            )
            raise JsonHandlerError(
                500, "This problem cannot be scored right now."
            ) from None

        # Reported, never enforced. Turning this into a gate would make the
        # server disagree with what submit() would have scored.
        validity = session.validate_responses(responses)

        try:
            outcomes = session.submit(responses)
        except (QtiTypeError, QtiStructureError):
            raise JsonHandlerError(
                400, "Your response could not be understood."
            ) from None
        except UnsupportedQtiFeature:
            log.exception(
                "pyqti: response processing for usage %s hit unsupported QTI",
                self.scope_ids.usage_id,
            )
            raise JsonHandlerError(
                500, "This problem cannot be scored right now."
            ) from None

        self.num_attempts += 1
        self.raw_responses = responses
        self.completion_status = session.completion_status

        score = Score(
            raw_earned=_as_float(outcomes.get("SCORE")),
            raw_possible=self._raw_possible(outcomes),
        )
        self.set_score(score)
        self._publish_grade(score)

        payload = {
            "valid": validity.valid,
            "errors": validity.errors,
            "completion_status": self.completion_status,
            "attempts_used": self.num_attempts,
            "attempts_remaining": (
                None
                if not self.max_attempts
                else max(0, self.max_attempts - self.num_attempts)
            ),
        }
        if self.show_score_immediately:
            payload["score"] = score.raw_earned
            payload["max_score"] = score.raw_possible
        return payload

    @XBlock.json_handler
    def submit_studio_edits(self, data, suffix=""):  # noqa: ARG002
        values = data.get("values") or {}
        qti_xml = values.get("qti_xml", self.qti_xml)

        try:
            self._store_qti(qti_xml)
        except UnsupportedQtiFeature as exc:
            raise JsonHandlerError(
                400,
                "This item uses a QTI feature pyqti does not implement yet, so "
                f"it cannot be saved: {exc}",
            ) from None
        except (QtiStructureError, QtiTypeError) as exc:
            raise JsonHandlerError(400, f"This item is not valid QTI: {exc}") from None
        except PyQtiError as exc:
            raise JsonHandlerError(
                400, f"This item cannot be delivered: {exc}"
            ) from None
        except Exception as exc:  # noqa: BLE001 - authoring input is arbitrary
            raise JsonHandlerError(400, f"This is not valid QTI 3.0: {exc}") from None

        for name in self.editable_fields:
            if name != "qti_xml" and name in values:
                setattr(self, name, values[name])
        return {"result": "success"}

    # ------------------------------------------------------------------ #
    # ScorableXBlockMixin
    # ------------------------------------------------------------------ #

    def has_submitted_answer(self) -> bool:
        return self.num_attempts > 0

    def get_score(self) -> Score:
        return Score(
            raw_earned=_as_float(self.raw_earned),
            raw_possible=_as_float(self.raw_possible, default=1.0),
        )

    def set_score(self, score: Score) -> None:
        self.raw_earned = score.raw_earned
        self.raw_possible = score.raw_possible

    def calculate_score(self) -> Score:
        """Re-grade the stored responses without touching state."""
        session = ItemSession(
            self._item(), prior_attempts=max(self.num_attempts - 1, 0)
        )
        outcomes = session.submit(dict(self.raw_responses))
        return Score(
            raw_earned=_as_float(outcomes.get("SCORE")),
            raw_possible=self._raw_possible(outcomes),
        )

    def max_score(self) -> float:
        return _as_float(self.raw_possible, default=1.0)

    def _raw_possible(self, outcomes: dict[str, Any]) -> float:
        """Work out what the item is out of.

        QTI does not reliably say. A declared MAXSCORE outcome is authoritative
        when present; otherwise the author may say so explicitly; otherwise SCORE
        is taken to be on the conventional 0..1 scale.
        """
        declared = outcomes.get("MAXSCORE")
        if declared is not None:
            return _as_float(declared, default=1.0)
        if self.raw_possible_override is not None:
            return float(self.raw_possible_override)
        return 1.0


def _as_float(value: Any, default: float = 0.0) -> float:
    if value is None:
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


__all__ = ["QtiAssessmentItemBlock"]