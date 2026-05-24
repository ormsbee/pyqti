from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.strength_datatype import (
    StrengthDatatype,
)

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class Break:
    class Meta:
        name = "break"
        namespace = "http://www.w3.org/2001/10/synthesis"

    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    time: None | str = field(
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
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
