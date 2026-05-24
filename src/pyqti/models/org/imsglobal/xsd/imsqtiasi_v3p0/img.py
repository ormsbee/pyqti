from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.img_dtype import ImgDtype

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class Img(ImgDtype):
    class Meta:
        name = "img"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
