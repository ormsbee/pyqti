from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class InteractionModuleDtype(EmptyPrimitiveTypeDtype):
    """
    An interaction configuration settings to be used by the PCI [PCI, 20].

    This setting is de- fined with respect to the set of JavaScript library
    modules.
    """

    class Meta:
        name = "InteractionModuleDType"

    id: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    primary_path: None | str = field(
        default=None,
        metadata={
            "name": "primary-path",
            "type": "Attribute",
        },
    )
    fallback_path: None | str = field(
        default=None,
        metadata={
            "name": "fallback-path",
            "type": "Attribute",
        },
    )
