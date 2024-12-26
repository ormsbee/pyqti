from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class CorrectDtype(EmptyPrimitiveTypeDtype):
    """This is a QTI expression.

    This expression looks up the declaration of a response variable and
    returns the associated correctResponse or NULL if no correct value
    was declared. When used in outcomes processing item identifier
    prefixing (see variable) may be used to obtain the correct response
    from an individual item.
    """

    class Meta:
        name = "CorrectDType"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
