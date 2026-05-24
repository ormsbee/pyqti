from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype import (
    BaseSequenceXbaseEmptyDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class ImgDtype(BaseSequenceXbaseEmptyDtype):
    """
    This provides the HTML 'img' tag content capability.
    """

    class Meta:
        name = "ImgDType"

    src: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    alt: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    longdesc: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]+%?",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]+%?",
        },
    )
