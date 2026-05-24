from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class SsmlMeta:
    class Meta:
        name = "ssml-meta"

    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    http_equiv: None | str = field(
        default=None,
        metadata={
            "name": "http-equiv",
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
