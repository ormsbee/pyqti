from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class FileHrefCardDtype:
    """
    This is the data-type for the URI for the associated content file for the
    alternative acc- essibility content.
    """

    class Meta:
        name = "FileHrefCardDType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "mime-type",
            "type": "Attribute",
            "required": True,
            "pattern": r'[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+/[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+',
        },
    )
