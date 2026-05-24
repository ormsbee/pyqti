from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.col_dtype import ColDtype

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class Col(ColDtype):
    class Meta:
        name = "col"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
