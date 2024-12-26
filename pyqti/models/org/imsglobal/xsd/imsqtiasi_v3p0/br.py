from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.brdtype import Brdtype

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Br(Brdtype):
    class Meta:
        name = "br"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
