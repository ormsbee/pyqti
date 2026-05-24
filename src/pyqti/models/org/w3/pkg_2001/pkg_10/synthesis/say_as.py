from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class SayAs:
    class Meta:
        name = "say-as"
        namespace = "http://www.w3.org/2001/10/synthesis"

    interpret_as: str = field(
        metadata={
            "name": "interpret-as",
            "type": "Attribute",
        }
    )
    format: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    detail: None | str = field(
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
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
