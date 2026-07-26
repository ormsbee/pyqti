"""The single point of contact between pyqti and xsdata.

Everything pyqti knows about xsdata lives here, in ``qtitree.py``, and in
``render/html.py``. That is deliberate: pyqti depends on several xsdata APIs that
are *not* part of its documented public surface --- ``XmlContext.build``,
``XmlMeta``, ``XmlVar.elements``, and ``serializers.mixins.EventGenerator``. The
``render.py`` that used to live in this repo called ``XmlSerializer.next_value``,
which no longer exists, so this coupling is a known and previously-realised risk.
``pyproject.toml`` pins ``xsdata<27`` for the same reason.

Building an ``XmlContext`` is expensive and it caches every ``build()`` result, so
there is exactly one shared instance for the process.
"""

from __future__ import annotations

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers.config import SerializerConfig

QTI_NAMESPACE = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
XSI_NAMESPACE = "http://www.w3.org/2001/XMLSchema-instance"
XML_NAMESPACE = "http://www.w3.org/XML/1998/namespace"

#: Shared model-metadata cache. Reused by the parser, the compiler and the renderer.
CONTEXT = XmlContext()


def make_parser_config(base_url: str | None = None) -> ParserConfig:
    """Build a deliberately strict parser config.

    ``fail_on_converter_warnings`` defaults to ``False`` in xsdata, which means
    ``max-choices="lots"`` parses "successfully" and leaves the attribute as the
    string ``'lots'`` with only a warning. For an assessment engine a ``base-type``
    or ``cardinality`` that silently stays a ``str`` is exactly the class of bug
    that mis-grades candidates, so pyqti turns those warnings into errors.

    Note that this is *not* schema validation --- xsdata does not validate against
    the XSD at all. Combined with ``fail_on_unknown_properties`` (already the
    xsdata default) it catches most authoring mistakes, but genuine validation
    would need lxml, which this project avoids for memory reasons.
    """
    return ParserConfig(
        base_url=base_url,
        fail_on_converter_warnings=True,
        fail_on_unknown_properties=True,
    )


#: Strict parser shared by every load that does not need a base URI.
PARSER = XmlParser(config=make_parser_config(), context=CONTEXT)

#: For serialising models back out as QTI XML (what ``overhead`` prints).
XML_SERIALIZER_CONFIG = SerializerConfig(
    indent="  ",
    ignore_default_attributes=True,
)

#: For HTML rendering.
#:
#: ``ignore_default_attributes`` MUST stay ``False`` here. xsdata's
#: ``next_attribute`` skips any attribute whose value equals its field default, so
#: turning this on silently drops ``max-choices="1"`` (1 is the XSD default) along
#: with ``shuffle``, ``orientation``, ``fixed``, ``show-hide`` and ``dir``. The
#: renderer would then emit a choice interaction the front end cannot tell apart
#: from a multi-select. The cost of leaving it off is ~24 inherited ARIA attributes
#: per element, which ``render/html.py`` filters with an explicit allowlist.
RENDER_SERIALIZER_CONFIG = SerializerConfig(
    xml_declaration=False,
    ignore_default_attributes=False,
)
