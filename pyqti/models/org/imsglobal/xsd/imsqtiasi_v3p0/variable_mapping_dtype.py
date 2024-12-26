from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class VariableMappingDtype(EmptyPrimitiveTypeDtype):
    """Variable mappings allow outcome variables declared with the name source-
    identifier in the corresponding item to be treated as if they were declared
    with the name target-identifier during outcome processing.

    Use of variable mappings allows more control over the way outc- omes
    are aggregated when using test variables.
    """

    class Meta:
        name = "VariableMappingDType"

    source_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "source-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    target_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "target-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
