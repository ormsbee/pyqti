from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.picture_dtype import (
    PictureDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Picture(PictureDtype):
    class Meta:
        name = "picture"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
