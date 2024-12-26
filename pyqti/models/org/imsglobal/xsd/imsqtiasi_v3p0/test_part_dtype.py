from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.any_ndtype import (
    LogicSingleDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.assessment_section_dtype import (
    QtiAssessmentSection,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.assessment_section_ref_dtype import (
    AssessmentSectionRefDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.branch_rule_dtype import (
    BranchRuleDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.item_session_control_dtype import (
    ItemSessionControlDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_feedback_dtype import (
    TestFeedbackDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_part_dtype_navigation_mode import (
    TestPartDtypeNavigationMode,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_part_dtype_submission_mode import (
    TestPartDtypeSubmissionMode,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_rubric_block_dtype import (
    TestRubricBlockDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.time_limits_dtype import (
    TimeLimitsDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class TestPartDtype:
    """A test is composed of one or more test parts.

    A test-part represents a major division of the test and is used to
    control the basic mode parameters that apply to all sections and
    sub-sections within that part.
    """

    class Meta:
        name = "TestPartDType"

    qti_pre_condition: List[LogicSingleDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-pre-condition",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_branch_rule: List[BranchRuleDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-branch-rule",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_item_session_control: Optional[ItemSessionControlDtype] = field(
        default=None,
        metadata={
            "name": "qti-item-session-control",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_time_limits: Optional[TimeLimitsDtype] = field(
        default=None,
        metadata={
            "name": "qti-time-limits",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_rubric_block: List[TestRubricBlockDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-rubric-block",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_assessment_section_or_qti_assessment_section_ref: List[
        Union[QtiAssessmentSection, AssessmentSectionRefDtype]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-assessment-section",
                    "type": QtiAssessmentSection,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-assessment-section-ref",
                    "type": AssessmentSectionRefDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    qti_test_feedback: List[TestFeedbackDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-test-feedback",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    navigation_mode: Optional[TestPartDtypeNavigationMode] = field(
        default=None,
        metadata={
            "name": "navigation-mode",
            "type": "Attribute",
            "required": True,
        },
    )
    submission_mode: Optional[TestPartDtypeSubmissionMode] = field(
        default=None,
        metadata={
            "name": "submission-mode",
            "type": "Attribute",
            "required": True,
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
