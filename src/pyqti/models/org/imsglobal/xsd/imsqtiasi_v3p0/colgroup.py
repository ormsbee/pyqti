from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.col_group_dtype import (
    ColGroupDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class Colgroup(ColGroupDtype):
    class Meta:
        name = "colgroup"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
