from dataclasses import dataclass, field
from typing import Dict, List, Optional

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass
class SsmlLexicon:
    class Meta:
        name = "ssml-lexicon"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    type_value: str = field(
        default="application/pls+xml",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    fetchtimeout: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\+)?([0-9]*\.)?[0-9]+(ms|s)",
        },
    )
    maxage: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maxstale: Optional[int] = field(
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
