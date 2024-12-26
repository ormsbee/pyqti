from dataclasses import dataclass, field
from typing import Dict, List, Optional

from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.strength_datatype import (
    StrengthDatatype,
)

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass
class Break:
    class Meta:
        name = "break"
        namespace = "http://www.w3.org/2001/10/synthesis"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\+)?([0-9]*\.)?[0-9]+(ms|s)",
        },
    )
    strength: StrengthDatatype = field(
        default=StrengthDatatype.MEDIUM,
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
