from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class FileHrefCardDtype:
    """
    This is the data-type for the URI for the associated content file for
    the alternative acc- essibility content.
    """

    class Meta:
        name = "FileHrefCardDType"

    value: str = field(default="")
    mime_type: str = field(
        metadata={
            "name": "mime-type",
            "type": "Attribute",
            "pattern": r'[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+/[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+',
        }
    )
