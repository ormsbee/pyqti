from dataclasses import dataclass, field
from typing import Dict, List

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass
class SsmlMetadata:
    class Meta:
        name = "ssml-metadata"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
