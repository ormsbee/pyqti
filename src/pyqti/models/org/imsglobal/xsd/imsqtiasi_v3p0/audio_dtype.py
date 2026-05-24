from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.audio_dtype_crossorigin import (
    AudioDtypeCrossorigin,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.audio_dtype_preload import (
    AudioDtypePreload,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_dtype import (
    BaseSequenceDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.source import Source
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.track import Track

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class AudioDtype(BaseSequenceDtype):
    """
    The 'audio' tag is an HTML5 feature.

    An audio tag represents a sound or audio stream. Con- tent may be
    provided inside the audio tag. User agents should not show this content
    to the user; it is intended for older Web browsers which do not support
    audio, so that legacy au- dio plugins can be tried, or to show text to
    the users of these older browsers informing them of how to access the
    audio contents.
    """

    class Meta:
        name = "AudioDType"

    src: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    crossorigin: None | AudioDtypeCrossorigin = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    preload: AudioDtypePreload = field(
        default=AudioDtypePreload.METADATA,
        metadata={
            "type": "Attribute",
        },
    )
    autoplay: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mediagroup: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    loop: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    muted: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    controls: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
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
