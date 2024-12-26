from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.math_constant_dtype_name import (
    MathConstantDtypeName,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class MathConstantDtype(EmptyPrimitiveTypeDtype):
    """This is a QTI expression function.

    The result is a mathematical constant returned as a si- ngle float,
    e.g. Pi and e.
    """

    class Meta:
        name = "MathConstantDType"

    name: Optional[MathConstantDtypeName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
