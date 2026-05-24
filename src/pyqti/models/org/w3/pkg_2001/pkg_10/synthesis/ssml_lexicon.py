from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class SsmlLexicon:
    class Meta:
        name = "ssml-lexicon"

    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    uri: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    type_value: str = field(
        default="application/pls+xml",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    fetchtimeout: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\+)?([0-9]*\.)?[0-9]+(ms|s)",
        },
    )
    maxage: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maxstale: None | int = field(
        default=None,
        metadata={
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
