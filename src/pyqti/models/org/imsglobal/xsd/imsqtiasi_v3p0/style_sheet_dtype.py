from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class StyleSheetDtype(EmptyPrimitiveTypeDtype):
    """
    Used to associate an external stylesheet with an object such as an
    assessmentItem, etc.

    Q- TI supports CSS 2.1 and CSS 3.0.
    """

    class Meta:
        name = "StyleSheetDType"

    href: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "pattern": r'[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+/[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+',
        }
    )
    media: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
