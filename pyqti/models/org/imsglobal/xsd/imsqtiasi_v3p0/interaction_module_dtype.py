from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class InteractionModuleDtype(EmptyPrimitiveTypeDtype):
    """An interaction configuration settings to be used by the PCI [PCI, 20].

    This setting is de- fined with respect to the set of JavaScript
    library modules.
    """

    class Meta:
        name = "InteractionModuleDType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    primary_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "primary-path",
            "type": "Attribute",
        },
    )
    fallback_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "fallback-path",
            "type": "Attribute",
        },
    )
