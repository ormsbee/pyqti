from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class SelectionDtype:
    """
    The selection class specifies the rules used to select the child
    elements of a section for each test session.

    If no selection rules are given it must be assumed that all elements a-
    re to be selected. The selection class also provides an opportunity for
    extensions to this specification to include support for more complex
    selection algorithms.
    """

    class Meta:
        name = "SelectionDType"

    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    select: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    with_replacement: bool = field(
        default=False,
        metadata={
            "name": "with-replacement",
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
