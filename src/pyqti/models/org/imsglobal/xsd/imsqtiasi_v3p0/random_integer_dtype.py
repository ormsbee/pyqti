from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class RandomIntegerDtype(EmptyPrimitiveTypeDtype):
    """
    This is a QTI expression function.

    Selects a random integer from the specified range [min- ,max]
    satisfying min + step * n for some integer n. For example, with min=2,
    max=11 and s- tep=3 the values {2,5,8,11} are possible.
    """

    class Meta:
        name = "RandomIntegerDType"

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
    step: object = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
