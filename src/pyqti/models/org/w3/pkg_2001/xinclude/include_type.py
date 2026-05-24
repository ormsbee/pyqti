from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from pyqti.models.org.w3.pkg_2001.xinclude.parse_type import ParseType

__NAMESPACE__ = "http://www.w3.org/2001/XInclude"


@dataclass(kw_only=True)
class IncludeType:
    class Meta:
        name = "includeType"

    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    parse: ParseType = field(
        default=ParseType.XML,
        metadata={
            "type": "Attribute",
        },
    )
    xpointer: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    encoding: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    accept: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    accept_language: None | str = field(
        default=None,
        metadata={
            "name": "accept-language",
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "fallback",
                    "type": ForwardRef("Fallback"),
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Include(IncludeType):
    class Meta:
        name = "include"
        namespace = "http://www.w3.org/2001/XInclude"


@dataclass(kw_only=True)
class FallbackType:
    class Meta:
        name = "fallbackType"

    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Fallback(FallbackType):
    class Meta:
        name = "fallback"
        namespace = "http://www.w3.org/2001/XInclude"
