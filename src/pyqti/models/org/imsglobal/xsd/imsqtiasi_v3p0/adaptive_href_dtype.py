from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class AdaptiveHrefDtype(EmptyPrimitiveTypeDtype):
    """
    This is the data-type for referencing information that is to be used to
    support the data exchange with the adaptive testing engine.
    """

    class Meta:
        name = "AdaptiveHrefDType"

    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    href: str = field(
        metadata={
            "type": "Attribute",
        }
    )
