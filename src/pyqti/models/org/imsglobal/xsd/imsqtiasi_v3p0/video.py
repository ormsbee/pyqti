from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.video_dtype import (
    VideoDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class Video(VideoDtype):
    class Meta:
        name = "video"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
