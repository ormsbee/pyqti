from dataclasses import dataclass, field
from typing import List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_dtype import (
    BaseSequenceDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.source import Source
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.track import Track
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.video_dtype_crossorigin import (
    VideoDtypeCrossorigin,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.video_dtype_preload import (
    VideoDtypePreload,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class VideoDtype(BaseSequenceDtype):
    """The 'video' tag is an HTML5 feature.

    A video tag is used for playing videos or movies, and audio files
    with captions.
    """

    class Meta:
        name = "VideoDType"

    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    crossorigin: Optional[VideoDtypeCrossorigin] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    preload: VideoDtypePreload = field(
        default=VideoDtypePreload.METADATA,
        metadata={
            "type": "Attribute",
        },
    )
    autoplay: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mediagroup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    loop: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    muted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    controls: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    poster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "source",
                    "type": Source,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "track",
                    "type": Track,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
