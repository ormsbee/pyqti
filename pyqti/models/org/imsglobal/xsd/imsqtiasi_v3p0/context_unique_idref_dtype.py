from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ContextUniqueIdrefDtype(EmptyPrimitiveTypeDtype):
    """
    The data-type for the context variable identifiers that are to be available to
    the PCI.
    """

    class Meta:
        name = "ContextUniqueIDRefDType"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
