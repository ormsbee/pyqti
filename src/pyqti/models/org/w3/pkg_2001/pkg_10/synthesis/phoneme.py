from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class Phoneme:
    class Meta:
        name = "phoneme"
        namespace = "http://www.w3.org/2001/10/synthesis"

    ph: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    alphabet: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(ipa|x-.*)",
        },
    )
    type_value: str = field(
        default="default",
        metadata={
            "name": "type",
            "type": "Attribute",
            "pattern": r"default|ruby",
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
