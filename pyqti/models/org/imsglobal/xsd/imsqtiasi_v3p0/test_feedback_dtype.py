from dataclasses import dataclass, field
from typing import Dict, List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    CatalogInfoDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.style_sheet_dtype import (
    StyleSheetDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_feedback_dtype_access import (
    TestFeedbackDtypeAccess,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_feedback_dtype_show_hide import (
    TestFeedbackDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_feedback_flow_content_body_dtype import (
    TestFeedbackFlowContentBodyDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class TestFeedbackDtype:
    """This class is used to define the test-level feedback content that can be
    presented to the learner.

    It must not contain an interaction object, either directly or
    indirectly. Feedba- ck elements can be embedded inside each other,
    with one exception: feedBackInline cannot contain feedbackBlock
    elements.
    """

    class Meta:
        name = "TestFeedbackDType"

    qti_stylesheet: List[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_content_body: Optional[TestFeedbackFlowContentBodyDtype] = field(
        default=None,
        metadata={
            "name": "qti-content-body",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_catalog_info: Optional[CatalogInfoDtype] = field(
        default=None,
        metadata={
            "name": "qti-catalog-info",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    access: Optional[TestFeedbackDtypeAccess] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    outcome_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "outcome-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    show_hide: Optional[TestFeedbackDtypeShowHide] = field(
        default=None,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
            "required": True,
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
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
