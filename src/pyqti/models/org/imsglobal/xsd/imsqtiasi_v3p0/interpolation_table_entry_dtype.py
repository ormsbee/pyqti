from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class InterpolationTableEntryDtype(EmptyPrimitiveTypeDtype):
    """
    Provides an interpolation table entry in the associated interpolation
    table.
    """

    class Meta:
        name = "InterpolationTableEntryDType"

    source_value: float = field(
        metadata={
            "name": "source-value",
            "type": "Attribute",
        }
    )
    include_boundary: bool = field(
        default=True,
        metadata={
            "name": "include-boundary",
            "type": "Attribute",
        },
    )
    target_value: str = field(
        metadata={
            "name": "target-value",
            "type": "Attribute",
        }
    )
