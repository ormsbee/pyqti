from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class DefaultDtype(EmptyPrimitiveTypeDtype):
    """
    This is one of the QTI expression functions.

    This expression looks up the declaration of an item variable and
    returns the associated default value or NULL if no default value was
    declared. When used in outcomes processing item identifier prefixing
    (see variable) may be used to obtain the default value from an
    individual item.
    """

    class Meta:
        name = "DefaultDType"

    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
