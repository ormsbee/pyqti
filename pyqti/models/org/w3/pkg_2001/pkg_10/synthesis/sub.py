from dataclasses import dataclass, field
from typing import Dict, List, Optional

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass
class Sub:
    class Meta:
        name = "sub"
        namespace = "http://www.w3.org/2001/10/synthesis"

    alias: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
