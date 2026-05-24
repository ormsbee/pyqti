from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.param_dtype_valuetype import (
    ParamDtypeValuetype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class ParamDtype(EmptyPrimitiveTypeDtype):
    """
    This is the container for a parameter being passed to the HTML 'object'
    tag.
    """

    class Meta:
        name = "ParamDType"

    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    value: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    valuetype: ParamDtypeValuetype = field(
        metadata={
            "type": "Attribute",
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "pattern": r'[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+/[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+',
        },
    )
