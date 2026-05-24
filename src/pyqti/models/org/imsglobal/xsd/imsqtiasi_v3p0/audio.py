from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.audio_dtype import (
    AudioDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class Audio(AudioDtype):
    class Meta:
        name = "audio"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
