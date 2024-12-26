from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.value_dtype_base_type import (
    ValueDtypeBaseType,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ValueDtype:
    """A class that can represent a single value of any base-type in variable
    declarations and r- esult reports.

    The base-type is defined by the 'base-type' attribute of the
    declaration e- xcept in the case of variables with record
    cardinality.
    """

    class Meta:
        name = "ValueDType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    field_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "field-identifier",
            "type": "Attribute",
        },
    )
    base_type: Optional[ValueDtypeBaseType] = field(
        default=None,
        metadata={
            "name": "base-type",
            "type": "Attribute",
        },
    )
