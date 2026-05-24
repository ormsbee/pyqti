from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class AssessmentItemDtype:
    """
    An assessment item encompasses the information that is presented to a
    candidate and infor- mation about how to score the item.

    Scoring takes place when candidate responses are tran- sformed into
    outcomes by response processing rules. It is sometimes desirable to
    have sev- eral different items that appear the same to the candidate
    but which are scored different- ly. In this specification, these are
    distinct items by definition and must therefore have distinct
    identifiers. To help facilitate the exchange of items that share
    significant par- ts of their presentation this specification supports
    the inclusion of separately managed item fragments (see Item and Test
    Fragments) in the qti-item-body.
    """

    class Meta:
        name = "AssessmentItemDType"

    qti_context_declaration: list[ContextDeclarationDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-context-declaration",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_response_declaration: list[ResponseDeclarationDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-response-declaration",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_outcome_declaration: list[QtiOutcomeDeclaration] = field(
        default_factory=list,
        metadata={
            "name": "qti-outcome-declaration",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_template_declaration: list[TemplateDeclarationDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-template-declaration",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_template_processing: None | TemplateProcessingDtype = field(
        default=None,
        metadata={
            "name": "qti-template-processing",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_assessment_stimulus_ref: list[AssessmentStimulusRefDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-assessment-stimulus-ref",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_companion_materials_info: None | CompanionMaterialsInfoDtype = field(
        default=None,
        metadata={
            "name": "qti-companion-materials-info",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_stylesheet: list[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_item_body: None | ItemBodyDtype = field(
        default=None,
        metadata={
            "name": "qti-item-body",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_catalog_info: None | CatalogInfoDtype = field(
        default=None,
        metadata={
            "name": "qti-catalog-info",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_response_processing: None | QtiResponseProcessing = field(
        default=None,
        metadata={
            "name": "qti-response-processing",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_modal_feedback: list[ModalFeedbackDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-modal-feedback",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    title: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    label: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    tool_name: None | str = field(
        default=None,
        metadata={
            "name": "tool-name",
            "type": "Attribute",
        },
    )
    tool_version: None | str = field(
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
    time_dependent: bool = field(
        metadata={
            "name": "time-dependent",
            "type": "Attribute",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
