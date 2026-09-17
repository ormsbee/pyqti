"""The single point of contact between pyqti and xsdata.

Everything pyqti knows about xsdata lives here and in ``qtitree.py``. That is
deliberate: pyqti depends on several xsdata APIs that are *not* part of its
documented public surface --- ``XmlContext.build``, ``XmlMeta`` and
``XmlVar.elements``, all used by ``qtitree.py`` to recover QTI element names. An
earlier prototype in this repo called ``XmlSerializer.next_value``, which no longer
exists, so this coupling is a known and previously-realised risk;
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

# xsdata picks its parser handler and serializer writer at import time, using the
# lxml-backed pair when lxml is importable and a pure-Python pair otherwise --- and
# the two do not agree (the native writer reflows mixed content when indenting; the
# lxml one does not). A serializer whose output shape depends on what else happens
# to be installed is not acceptable here, because ``presentation_xml`` output is
# this project's security boundary and ``tests/test_redaction.py`` asserts over it
# as text.
#
# So lxml is a hard dependency (see ``pyproject.toml``) rather than an incidental
# one, and xsdata's default selection is left alone: with lxml always present the
# choice is fixed. ``tests/test_serialization.py`` asserts that it really is the
# lxml pair in use, so this cannot drift back into being conditional.

#: Shared model-metadata cache. Reused by the parser, the compiler and the serializer.
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
    xsdata default) it catches most authoring mistakes. Genuine XSD validation
    would need lxml, which is now a dependency, so it has become possible rather
    than merely desirable --- see ``TODO.md``.
    """
    return ParserConfig(
        base_url=base_url,
        fail_on_converter_warnings=True,
        fail_on_unknown_properties=True,
    )


#: Strict parser shared by every load that does not need a base URI.
PARSER = XmlParser(config=make_parser_config(), context=CONTEXT)


def make_serializer_config(indent: str | None = None) -> SerializerConfig:
    """Build a config for writing models back out as QTI XML.

    ``indent`` defaults to ``None``, and that default still matters, though less
    dramatically than it once did. The pure-Python writer reflows mixed content
    when indenting, turning ``<p>the <em>x</em></p>`` into ``<p>the\n
    <em>x</em>\n</p>``; lxml's writer, which is what pyqti uses, keeps the
    sentence inline but still inserts whitespace before the closing tag. That
    whitespace is inside an element the candidate reads. Only ask for
    indentation when a human is going to read the output.

    ``ignore_default_attributes=True`` omits any attribute whose value equals its
    XSD default, so ``max-choices="1"`` does not appear in the output. That is safe
    for XML --- a schema-aware consumer restores the default, and Citolab's
    ``qti-choice-interaction`` is verified to initialise ``maxChoices = 1`` /
    ``minChoices = 0`` to match. It would *not* have been safe for HTML output,
    which has no schema to restore from.
    """
    return SerializerConfig(indent=indent, ignore_default_attributes=True)
