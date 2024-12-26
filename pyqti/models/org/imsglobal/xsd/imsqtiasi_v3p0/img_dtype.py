from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype import (
    BaseSequenceXbaseEmptyDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ImgDtype(BaseSequenceXbaseEmptyDtype):
    """
    This provides the HTML 'img' tag content capability.
    """

    class Meta:
        name = "ImgDType"

    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    longdesc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]+%?",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]+%?",
        },
    )
