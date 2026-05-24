from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class OutcomeMinMaxDtype(EmptyPrimitiveTypeDtype):
    """
    This is a data-type for the 'qti-outcome-minimum' and
    'qti-outcome-maximum' QTI expressio- ns for outcome processing.
    """

    class Meta:
        name = "OutcomeMinMaxDType"

    section_identifier: None | str = field(
        default=None,
        metadata={
            "name": "section-identifier",
            "type": "Attribute",
        },
    )
    include_category: list[str] = field(
        default_factory=list,
        metadata={
            "name": "include-category",
            "type": "Attribute",
            "tokens": True,
        },
    )
    exclude_category: list[str] = field(
        default_factory=list,
        metadata={
            "name": "exclude-category",
            "type": "Attribute",
            "tokens": True,
        },
    )
    outcome_identifier: str = field(
        metadata={
            "name": "outcome-identifier",
            "type": "Attribute",
        }
    )
    weight_identifier: None | str = field(
        default=None,
        metadata={
            "name": "weight-identifier",
            "type": "Attribute",
        },
    )
