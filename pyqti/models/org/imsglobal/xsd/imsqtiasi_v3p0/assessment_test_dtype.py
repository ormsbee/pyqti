from dataclasses import dataclass, field
from typing import Dict, List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.context_declaration_dtype import (
    ContextDeclarationDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.qti_outcome_declaration import (
    QtiOutcomeDeclaration,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.qti_outcome_processing import (
    QtiOutcomeProcessing,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.style_sheet_dtype import (
    StyleSheetDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_feedback_dtype import (
    TestFeedbackDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_part_dtype import (
    TestPartDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_rubric_block_dtype import (
    TestRubricBlockDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.time_limits_dtype import (
    TimeLimitsDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class AssessmentTestDtype:
    """An assessment test is a group of assessmentItems with an associated set of
    rules that det- ermine which of the items the candidate sees, in what order,
    and in what way the candidate interacts with them.

    The rules describe the valid paths through the test, when responses
    are submitted for response processing and when (if at all) feedback
    is to be given. Asses- sment tests are composed of one or more test
    parts.
    """

    class Meta:
        name = "AssessmentTestDType"

    qti_context_declaration: List[ContextDeclarationDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-context-declaration",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_outcome_declaration: List[QtiOutcomeDeclaration] = field(
        default_factory=list,
        metadata={
            "name": "qti-outcome-declaration",
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
    qti_stylesheet: List[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
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
    qti_test_part: List[TestPartDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-test-part",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    qti_outcome_processing: Optional[QtiOutcomeProcessing] = field(
        default=None,
        metadata={
            "name": "qti-outcome-processing",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
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
            "required": True,
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
    tool_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "tool-name",
            "type": "Attribute",
        },
    )
    tool_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "tool-version",
            "type": "Attribute",
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
