from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.hrdtype import Hrdtype

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Hr(Hrdtype):
    class Meta:
        name = "hr"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
