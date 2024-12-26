from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class InterpolationTableEntryDtype(EmptyPrimitiveTypeDtype):
    """
    Provides an interpolation table entry in the associated interpolation table.
    """

    class Meta:
        name = "InterpolationTableEntryDType"

    source_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "source-value",
            "type": "Attribute",
            "required": True,
        },
    )
    include_boundary: bool = field(
        default=True,
        metadata={
            "name": "include-boundary",
            "type": "Attribute",
        },
    )
    target_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "target-value",
            "type": "Attribute",
            "required": True,
        },
    )
