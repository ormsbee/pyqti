from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.any_ndtype import (
    LogicSingleDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.branch_rule_dtype import (
    BranchRuleDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.item_session_control_dtype import (
    ItemSessionControlDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_default_dtype import (
    TemplateDefaultDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.time_limits_dtype import (
    TimeLimitsDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.variable_mapping_dtype import (
    VariableMappingDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.weight_dtype import (
    WeightDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class AssessmentItemRefDtype:
    """
    Items are incorporated into the test by reference and not by direct
    aggregation.

    Note that the identifier of the reference need not have any meaning
    outside the test. In particular it is not required to be unique in the
    context of any catalog, or be represented in the i- tem's metadata.
    """

    class Meta:
        name = "AssessmentItemRefDType"

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
    qti_variable_mapping: list[VariableMappingDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-variable-mapping",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_weight: list[WeightDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-weight",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_template_default: list[TemplateDefaultDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-template-default",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
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
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    href: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    category: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
