from dataclasses import dataclass, field
from typing import Dict, List, Optional

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class SelectionDtype:
    """The selection class specifies the rules used to select the child elements of
    a section for each test session.

    If no selection rules are given it must be assumed that all elements
    a- re to be selected. The selection class also provides an
    opportunity for extensions to this specification to include support
    for more complex selection algorithms.
    """

    class Meta:
        name = "SelectionDType"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    select: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    with_replacement: bool = field(
        default=False,
        metadata={
            "name": "with-replacement",
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
