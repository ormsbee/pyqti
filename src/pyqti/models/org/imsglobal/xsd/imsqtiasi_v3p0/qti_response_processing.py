from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.response_processing_dtype import (
    ResponseProcessingDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class QtiResponseProcessing(ResponseProcessingDtype):
    class Meta:
        name = "qti-response-processing"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
