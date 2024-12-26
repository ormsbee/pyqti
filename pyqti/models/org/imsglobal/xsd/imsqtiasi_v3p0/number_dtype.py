from dataclasses import dataclass, field
from typing import List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class NumberDtype(EmptyPrimitiveTypeDtype):
    """This is base class for some of the QTI expressions.

    This is the data-type used in some of the functions that are used in
    Outcome Processing only and which provide summative inform- ation.
    """

    class Meta:
        name = "NumberDType"

    section_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "section-identifier",
            "type": "Attribute",
        },
    )
    include_category: List[str] = field(
        default_factory=list,
        metadata={
            "name": "include-category",
            "type": "Attribute",
            "tokens": True,
        },
    )
    exclude_category: List[str] = field(
        default_factory=list,
        metadata={
            "name": "exclude-category",
            "type": "Attribute",
            "tokens": True,
        },
    )
