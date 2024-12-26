from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.assessment_test_dtype import (
    AssessmentTestDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class QtiAssessmentTest(AssessmentTestDtype):
    class Meta:
        name = "qti-assessment-test"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
