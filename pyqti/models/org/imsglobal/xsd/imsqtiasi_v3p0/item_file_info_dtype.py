from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ItemFileInfoDtype:
    """
    This is the container for information about an external file that contains
    information to be made available to the learner.
    """

    class Meta:
        name = "ItemFileInfoDType"

    qti_file_href: Optional[str] = field(
        default=None,
        metadata={
            "name": "qti-file-href",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
    qti_resource_icon: Optional[str] = field(
        default=None,
        metadata={
            "name": "qti-resource-icon",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "mime-type",
            "type": "Attribute",
            "pattern": r'[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+/[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+',
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
