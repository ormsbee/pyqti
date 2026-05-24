from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.outcome_processing_dtype import (
    OutcomeProcessingDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class QtiOutcomeProcessing(OutcomeProcessingDtype):
    class Meta:
        name = "qti-outcome-processing"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
