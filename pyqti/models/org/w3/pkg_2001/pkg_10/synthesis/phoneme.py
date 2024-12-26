from dataclasses import dataclass, field
from typing import Dict, List, Optional

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass
class Phoneme:
    class Meta:
        name = "phoneme"
        namespace = "http://www.w3.org/2001/10/synthesis"

    ph: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    alphabet: Optional[str] = field(
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
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
