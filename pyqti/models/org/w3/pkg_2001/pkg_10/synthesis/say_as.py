from dataclasses import dataclass, field
from typing import Dict, List, Optional

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass
class SayAs:
    class Meta:
        name = "say-as"
        namespace = "http://www.w3.org/2001/10/synthesis"

    interpret_as: Optional[str] = field(
        default=None,
        metadata={
            "name": "interpret-as",
            "type": "Attribute",
            "required": True,
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    detail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
