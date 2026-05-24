from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.assessment_item_dtype import (
    AssessmentItemDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class QtiAssessmentItem(AssessmentItemDtype):
    class Meta:
        name = "qti-assessment-item"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
