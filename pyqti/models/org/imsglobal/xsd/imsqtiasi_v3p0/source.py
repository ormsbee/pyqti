from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.source_dtype import (
    SourceDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Source(SourceDtype):
    class Meta:
        name = "source"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
