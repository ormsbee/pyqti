from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class RandomFloatDtype(EmptyPrimitiveTypeDtype):
    """
    This is a QTI expresssion function.

    Selects a random float from the specified range [min,- max].
    """

    class Meta:
        name = "RandomFloatDType"

    min: object = field(
        default="0",
        metadata={
            "type": "Attribute",
        },
    )
    max: object = field(
        metadata={
            "type": "Attribute",
        }
    )
