"""Parsing QTI documents into the generated models.

Only seven generated classes carry a ``Meta.namespace`` and are therefore valid
parse roots (``QtiAssessmentItem``, ``QtiAssessmentTest``, ``QtiAssessmentStimulus``,
``QtiResponseProcessing``, ``QtiOutcomeDeclaration``, ``QtiOutcomeProcessing``,
``QtiAssessmentSection``). Everything else --- ``qti-item-body``,
``qti-choice-interaction``, ``qti-response-declaration`` --- exists only as a field
on a parent, with its element name in the parent's metadata. So an item can only be
loaded whole.

``QtiResponseProcessing`` being a root in its own right is what lets the vendored
response-processing templates go through this same code path, and therefore through
the same compiler as inline rules.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import IO, Any

from xsdata.formats.dataclass.parsers import XmlParser

from pyqti._xsdata import CONTEXT, PARSER, make_parser_config
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0 import (
    QtiAssessmentItem,
    QtiResponseProcessing,
)

#: ``str``/``bytes`` are XML *content*; ``Path``/``os.PathLike``/file objects are
#: files. This follows the ``fromstring`` vs ``parse`` split every Python XML
#: library uses, and :func:`_parse` raises rather than guessing when a ``str``
#: is obviously a filename.
Source = str | bytes | os.PathLike[str] | IO[bytes] | IO[str]


def _parser_for(base_uri: str | None) -> XmlParser:
    if base_uri is None:
        return PARSER
    return XmlParser(config=make_parser_config(base_url=base_uri), context=CONTEXT)


def _parse(source: Source, target: type[Any], base_uri: str | None) -> Any:
    parser = _parser_for(base_uri)

    if isinstance(source, os.PathLike):
        with Path(source).open("rb") as handle:
            return parser.parse(handle, target)
    if isinstance(source, bytes):
        return parser.from_bytes(source, target)
    if isinstance(source, str):
        if "<" not in source:
            raise ValueError(
                "load_* takes XML content as str/bytes; "
                f"{source!r} looks like a filename. Wrap it in pathlib.Path()."
            )
        return parser.from_string(source, target)
    return parser.parse(source, target)


def load_assessment_item(
    source: Source, *, base_uri: str | None = None
) -> QtiAssessmentItem:
    """Parse a ``qti-assessment-item`` document.

    ``base_uri`` is accepted now, and threaded into xsdata's ``ParserConfig.base_url``,
    even though nothing consumes it yet. Relative ``template-location`` references and
    XInclude both need it, and a loader that discards the source location can never
    resolve them later.
    """
    return _parse(source, QtiAssessmentItem, base_uri)


def load_response_processing(
    source: Source, *, base_uri: str | None = None
) -> QtiResponseProcessing:
    """Parse a standalone ``qti-response-processing`` document.

    Used for the vendored response-processing templates.
    """
    return _parse(source, QtiResponseProcessing, base_uri)
