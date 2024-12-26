from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_empty_dtype import (
    BaseSequenceEmptyDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class SourceDtype(BaseSequenceEmptyDtype):
    """The 'source' tag is an HTML5 feature.

    The source tag allows authors to specify multiple a- lternative
    media resources for media tags. It does not represent anything on
    its own.
    """

    class Meta:
        name = "SourceDType"

    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "pattern": r'[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+/[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+',
        },
    )
    srcset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    media: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sizes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
