from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    CatalogInfoDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.assessment_stimulus_ref_dtype import (
    AssessmentStimulusRefDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.companion_materials_info_dtype import (
    CompanionMaterialsInfoDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.context_declaration_dtype import (
    ContextDeclarationDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.item_body_dtype import (
    ItemBodyDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.modal_feedback_dtype import (
    ModalFeedbackDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.qti_outcome_declaration import (
    QtiOutcomeDeclaration,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.qti_response_processing import (
    QtiResponseProcessing,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.response_declaration_dtype import (
    ResponseDeclarationDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.style_sheet_dtype import (
    StyleSheetDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_declaration_dtype import (
    TemplateDeclarationDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_processing_dtype import (
    TemplateProcessingDtype,
)
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class AssessmentItemDtype:
    """An assessment item encompasses the information that is presented to a
    candidate and infor- mation about how to score the item.

    Scoring takes place when candidate responses are tran- sformed into
    outcomes by response processing rules. It is sometimes desirable to
    have sev- eral different items that appear the same to the candidate
    but which are scored different- ly. In this specification, these are
    distinct items by definition and must therefore have distinct
    identifiers. To help facilitate the exchange of items that share
    significant par- ts of their presentation this specification
    supports the inclusion of separately managed item fragments (see
    Item and Test Fragments) in the qti-item-body.
    """

    class Meta:
        name = "AssessmentItemDType"

    qti_context_declaration: List[ContextDeclarationDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-context-declaration",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_response_declaration: List[ResponseDeclarationDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-response-declaration",
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
    qti_template_declaration: List[TemplateDeclarationDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-template-declaration",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_template_processing: Optional[TemplateProcessingDtype] = field(
        default=None,
        metadata={
            "name": "qti-template-processing",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_assessment_stimulus_ref: List[AssessmentStimulusRefDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-assessment-stimulus-ref",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_companion_materials_info: Optional[CompanionMaterialsInfoDtype] = (
        field(
            default=None,
            metadata={
                "name": "qti-companion-materials-info",
                "type": "Element",
                "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            },
        )
    )
    qti_stylesheet: List[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_item_body: Optional[ItemBodyDtype] = field(
        default=None,
        metadata={
            "name": "qti-item-body",
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
    qti_response_processing: Optional[QtiResponseProcessing] = field(
        default=None,
        metadata={
            "name": "qti-response-processing",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_modal_feedback: List[ModalFeedbackDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-modal-feedback",
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
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
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
    adaptive: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    time_dependent: Optional[bool] = field(
        default=None,
        metadata={
            "name": "time-dependent",
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
