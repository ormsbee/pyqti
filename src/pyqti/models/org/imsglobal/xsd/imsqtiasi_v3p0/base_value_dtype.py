from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_value_dtype_base_type import (
    BaseValueDtypeBaseType,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class BaseValueDtype:
    """
    One of the QTI expression functions.

    The simplest expression returns a single value from the set defined by
    the given base-type.
    """

    class Meta:
        name = "BaseValueDType"

    value: str = field(default="")
    base_type: BaseValueDtypeBaseType = field(
        metadata={
            "name": "base-type",
            "type": "Attribute",
        }
    )
