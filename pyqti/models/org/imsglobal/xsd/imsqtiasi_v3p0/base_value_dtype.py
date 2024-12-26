from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_value_dtype_base_type import (
    BaseValueDtypeBaseType,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class BaseValueDtype:
    """One of the QTI expression functions.

    The simplest expression returns a single value from the set defined
    by the given base-type.
    """

    class Meta:
        name = "BaseValueDType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    base_type: Optional[BaseValueDtypeBaseType] = field(
        default=None,
        metadata={
            "name": "base-type",
            "type": "Attribute",
            "required": True,
        },
    )
