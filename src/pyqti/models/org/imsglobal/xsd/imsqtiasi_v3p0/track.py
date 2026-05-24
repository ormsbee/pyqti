from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.track_dtype import (
    TrackDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class Track(TrackDtype):
    class Meta:
        name = "track"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
