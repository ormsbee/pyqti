from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class ItemFileInfoDtype:
    """
    This is the container for information about an external file that
    contains information to be made available to the learner.
    """

    class Meta:
        name = "ItemFileInfoDType"

    qti_file_href: str = field(
        metadata={
            "name": "qti-file-href",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        }
    )
    qti_resource_icon: None | str = field(
        default=None,
        metadata={
            "name": "qti-resource-icon",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    mime_type: None | str = field(
        default=None,
        metadata={
            "name": "mime-type",
            "type": "Attribute",
            "pattern": r'[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+/[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+',
        },
    )
    label: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
