from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_dtype import (
    TemplateDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class Template(TemplateDtype):
    class Meta:
        name = "template"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
