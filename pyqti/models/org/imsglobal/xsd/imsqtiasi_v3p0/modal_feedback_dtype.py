from dataclasses import dataclass, field
from typing import Dict, List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    CatalogInfoDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.feedback_flow_content_body_dtype import (
    FeedbackFlowContentBodyDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.modal_feedback_dtype_show_hide import (
    ModalFeedbackDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.style_sheet_dtype import (
    StyleSheetDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ModalFeedbackDtype:
    """Modal feedback is shown to the candidate directly following response
    processing.

    The value of an outcome variable is used in conjunction with the
    showHide and identifier characteri- stics to determine whether or
    not the feedback is shown. The content of the modalFeedback must not
    contain any interactions.
    """

    class Meta:
        name = "ModalFeedbackDType"

    qti_stylesheet: List[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_content_body: Optional[FeedbackFlowContentBodyDtype] = field(
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
    outcome_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "outcome-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    show_hide: Optional[ModalFeedbackDtypeShowHide] = field(
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
