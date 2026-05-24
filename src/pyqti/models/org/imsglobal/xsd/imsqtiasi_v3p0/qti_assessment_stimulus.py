from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.assessment_stimulus_dtype import (
    AssessmentStimulusDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class QtiAssessmentStimulus(AssessmentStimulusDtype):
    class Meta:
        name = "qti-assessment-stimulus"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
