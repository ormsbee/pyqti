from dataclasses import dataclass, field
from typing import List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_dtype import (
    BaseSequenceDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.img import Img
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.source import Source

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class PictureDtype(BaseSequenceDtype):
    """
    This provides the functionality of the HTML 'picture' tag (a new tag added in
    HTML5).
    """

    class Meta:
        name = "PictureDType"

    source: List[Source] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    img: Optional[Img] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
