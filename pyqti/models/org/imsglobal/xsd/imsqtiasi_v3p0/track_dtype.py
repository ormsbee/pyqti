from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_empty_dtype import (
    BaseSequenceEmptyDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.track_dtype_kind import (
    TrackDtypeKind,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class TrackDtype(BaseSequenceEmptyDtype):
    """The 'track' tag is an HTML5 feature.

    The track tag allows authors to specify explicit ext- ernal timed
    text tracks for media elements. It does not represent anything on
    its own.
    """

    class Meta:
        name = "TrackDType"

    kind: Optional[TrackDtypeKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    srclang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    default: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
