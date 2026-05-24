from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adaptive_selection_dtype import (
    AdaptiveSelectionDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.any_ndtype import (
    LogicSingleDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.assessment_item_ref_dtype import (
    AssessmentItemRefDtype,
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
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ordering_dtype import (
    OrderingDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.selection_dtype import (
    SelectionDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_rubric_block_dtype import (
    TestRubricBlockDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.time_limits_dtype import (
    TimeLimitsDtype,
)
from pyqti.models.org.w3.pkg_2001.xinclude.include_type import Include

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class AssessmentSectionDtype:
    """
    An assessment section groups together individual item references and/or
    sub-sections.

    A s- ection can be composed of any hierarchy/combination of items and
    sections. A section can only reference an item using a
    qti-assessment-item-ref object but it may contain or refer- ence other
    sections. The grouping of the sections/items depends upon the nature of
    the pa- rent section i.e. each section can be used for different
    grouping criteria e.g. organizat- ional, pedagogic, etc.
    """

    class Meta:
        name = "AssessmentSectionDType"

    qti_pre_condition: list[LogicSingleDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-pre-condition",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_branch_rule: list[BranchRuleDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-branch-rule",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_item_session_control: None | ItemSessionControlDtype = field(
        default=None,
        metadata={
            "name": "qti-item-session-control",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_time_limits: None | TimeLimitsDtype = field(
        default=None,
        metadata={
            "name": "qti-time-limits",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_adaptive_selection_or_qti_selection_or_qti_ordering: list[
        AdaptiveSelectionDtype | SelectionDtype | OrderingDtype
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-adaptive-selection",
                    "type": AdaptiveSelectionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-selection",
                    "type": SelectionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordering",
                    "type": OrderingDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
            "max_occurs": 2,
        },
    )
    qti_rubric_block: list[TestRubricBlockDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-rubric-block",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    choice: list[
        Include
        | AssessmentItemRefDtype
        | QtiAssessmentSection
        | AssessmentSectionRefDtype
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-assessment-item-ref",
                    "type": AssessmentItemRefDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-assessment-section",
                    "type": ForwardRef("QtiAssessmentSection"),
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
    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    required: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    fixed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    title: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    visible: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    keep_together: bool = field(
        default=True,
        metadata={
            "name": "keep-together",
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class QtiAssessmentSection(AssessmentSectionDtype):
    class Meta:
        name = "qti-assessment-section"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
