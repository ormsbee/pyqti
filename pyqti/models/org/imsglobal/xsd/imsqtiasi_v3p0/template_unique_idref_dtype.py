from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class TemplateUniqueIdrefDtype(EmptyPrimitiveTypeDtype):
    """
    The data-type for the template variable identifiers that are to be available to
    the PCI.
    """

    class Meta:
        name = "TemplateUniqueIDRefDType"

    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
