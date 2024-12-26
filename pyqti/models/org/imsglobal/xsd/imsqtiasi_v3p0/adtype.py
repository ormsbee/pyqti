from dataclasses import dataclass, field
from typing import Dict, ForwardRef, List, Optional, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype import (
    AriabaseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.associable_hotspot_dtype import (
    AssociableHotspotDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.audio import (
    Audio as ImsglobalXsdImsqtiasiV3P0AudioAudio,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_prompt_interaction_dtype_data_qti_suppress_tts import (
    BasePromptInteractionDtypeDataQtiSuppressTts,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_prompt_interaction_dtype_dir import (
    BasePromptInteractionDtypeDir,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_dtype import (
    BaseSequenceDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_full_dtype import (
    BaseSequenceFullDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_rident_dtype import (
    BaseSequenceRidentDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_dtype import (
    BaseSequenceXbaseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.br import Br
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.card_dtype_value import (
    CardDtypeValue,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.choice_interaction_dtype_orientation import (
    ChoiceInteractionDtypeOrientation,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.col import Col
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.colgroup import Colgroup
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.context_unique_idref_dtype import (
    ContextUniqueIdrefDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.custom_interaction_dtype import (
    CustomInteractionDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.end_attempt_interaction_dtype import (
    EndAttemptInteractionDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.extended_text_interaction_dtype_format import (
    ExtendedTextInteractionDtypeFormat,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.feedback_block_dtype_show_hide import (
    FeedbackBlockDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.feedback_inline_dtype_show_hide import (
    FeedbackInlineDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.file_href_card_dtype import (
    FileHrefCardDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.gap_dtype import GapDtype
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.gap_img_dtype_show_hide import (
    GapImgDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.gap_text_dtype_show_hide import (
    GapTextDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.hot_text_dtype_show_hide import (
    HotTextDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.hotspot_choice_dtype import (
    HotspotChoiceDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.hr import Hr
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.img import Img
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.inline_choice_dtype_show_hide import (
    InlineChoiceDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.interaction_modules_dtype import (
    InteractionModulesDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.order_interaction_dtype_orientation import (
    OrderInteractionDtypeOrientation,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.param_dtype import (
    ParamDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.picture import Picture
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.printed_variable_dtype import (
    PrintedVariableDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.simple_associable_choice_dtype_show_hide import (
    SimpleAssociableChoiceDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.simple_choice_dtype_show_hide import (
    SimpleChoiceDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.slider_interaction_dtype_orientation import (
    SliderInteractionDtypeOrientation,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.style_sheet_dtype import (
    StyleSheetDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.tdhdtype_align import (
    TdhdtypeAlign,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.tdhdtype_scope import (
    TdhdtypeScope,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.tdhdtype_valign import (
    TdhdtypeValign,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template import Template
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_block_dtype_show_hide import (
    TemplateBlockDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_block_feedback_block_dtype_show_hide import (
    TemplateBlockFeedbackBlockDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_inline_dtype_show_hide import (
    TemplateInlineDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_unique_idref_dtype import (
    TemplateUniqueIdrefDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.text_entry_interaction_dtype import (
    TextEntryInteractionDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.video import Video
from pyqti.models.org.w3.pkg_1998.math.math_ml.math import Math
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.break_mod import Break
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.mark import Mark
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.paragraph import (
    Audio as W3Pkg2001Pkg10SynthesisParagraphAudio,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.paragraph import (
    Emphasis,
    Prosody,
    S,
    Voice,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.paragraph import (
    P as ParagraphP,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.phoneme import Phoneme
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.say_as import SayAs
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.speak import Speak
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.sub import Sub as SubSub
from pyqti.models.org.w3.pkg_2001.xinclude.include_type import Include
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Adtype(BaseSequenceXbaseDtype):
    """This provides the functionality of the HTML 'a' tag and is used to identifiy
    a link.

    If t- he 'a' tag has an href attribute, then it represents a
    hyperlink (a hypertext anchor) lab- eled by its contents. If the a
    element has no href attribute, then the element represents a
    placeholder for where a link might otherwise have been placed, if it
    had been relevant, consisting of just the element's contents.
    """

    class Meta:
        name = "ADType"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "pattern": r'[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+/[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+',
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-text-entry-interaction",
                    "type": TextEntryInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext",
                    "type": ForwardRef("HotTextDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap",
                    "type": GapDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": ForwardRef("FeedbackInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inline-choice-interaction",
                    "type": ForwardRef("InlineChoiceInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-end-attempt-interaction",
                    "type": EndAttemptInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-interaction",
                    "type": CustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": ForwardRef("A"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": ForwardRef("Bdo"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": ForwardRef("Bdi"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": ForwardRef("Label"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class BasePromptInteractionDtype(AriabaseDtype):
    """The BasePromptInteraction is the base class for the QTI interactions that
    support a Promp- t.

    This also consists of a set of children characteristics.
    """

    class Meta:
        name = "BasePromptInteractionDType"

    qti_prompt: Optional["PromptDtype"] = field(
        default=None,
        metadata={
            "name": "qti-prompt",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    id: Optional[str] = field(
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
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    w3_org_xml_1998_namespace_lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "name": "lang",
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    w3_org_xml_1998_namespace_base: Optional[str] = field(
        default=None,
        metadata={
            "name": "base",
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    response_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "response-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    dir: BasePromptInteractionDtypeDir = field(
        default=BasePromptInteractionDtypeDir.AUTO,
        metadata={
            "type": "Attribute",
        },
    )
    data_catalog_idref: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-catalog-idref",
            "type": "Attribute",
        },
    )
    data_qti_suppress_tts: Optional[
        BasePromptInteractionDtypeDataQtiSuppressTts
    ] = field(
        default=None,
        metadata={
            "name": "data-qti-suppress-tts",
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


@dataclass
class CardDtype:
    """A data structure within a catalog which contains dormant HTML content or a
    resource refer- ence for a specific support/feature.

    A card may also contain multiple CardEntry container- s. For
    example, you might have multiple CardEntry nodes for different
    language versions of a particular support.
    """

    class Meta:
        name = "CardDType"

    qti_html_content_or_qti_file_href_or_qti_card_entry: List[
        Union["HtmlcontentDtype", FileHrefCardDtype, "CardEntryDtype"]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-html-content",
                    "type": ForwardRef("HtmlcontentDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-file-href",
                    "type": FileHrefCardDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-card-entry",
                    "type": ForwardRef("CardEntryDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    support: Optional[CardDtypeValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class GapImgDtype(BaseSequenceDtype):
    """
    A gap image contains a single image object to be inserted into a gap by the
    candidate.
    """

    class Meta:
        name = "GapImgDType"

    object_or_img_or_picture: Optional[Union["Object", Img, Picture]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
        },
    )
    show_hide: GapImgDtypeShowHide = field(
        default=GapImgDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    match_group: List[str] = field(
        default_factory=list,
        metadata={
            "name": "match-group",
            "type": "Attribute",
            "tokens": True,
        },
    )
    match_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "match-max",
            "type": "Attribute",
            "required": True,
        },
    )
    match_min: int = field(
        default=0,
        metadata={
            "name": "match-min",
            "type": "Attribute",
        },
    )
    object_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "object-label",
            "type": "Attribute",
        },
    )
    top: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    left: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class GraphicOrderInteractionDtype(BaseSequenceFullDtype):
    """A graphic order interaction is a graphic interaction with a corresponding
    set of choices that are defined as areas of the graphic image.

    The candidate's task is to impose an orde- ring on the areas
    (hotspots). The order hotspot interaction should only be used when
    the spacial relationship of the choices with respect to each other
    (as represented by the gra- phic image) is important to the needs of
    the item. Otherwise, orderInteraction should be used instead with
    separate material for each option. The delivery engine must clearly
    ind- icate all defined area(s) of the image. The order hotspot
    interaction must be bound to a response variable with a base-type of
    identifier and ordered cardinality.
    """

    class Meta:
        name = "GraphicOrderInteractionDType"

    qti_prompt: Optional["PromptDtype"] = field(
        default=None,
        metadata={
            "name": "qti-prompt",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    object_or_img_or_picture: Optional[Union["Object", Img, Picture]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    qti_hotspot_choice: List[HotspotChoiceDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-hotspot-choice",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    min_choices: Optional[int] = field(
        default=None,
        metadata={
            "name": "min-choices",
            "type": "Attribute",
        },
    )
    max_choices: Optional[int] = field(
        default=None,
        metadata={
            "name": "max-choices",
            "type": "Attribute",
        },
    )


@dataclass
class AssociateInteractionDtype(BasePromptInteractionDtype):
    """An Associate Interaction is a blockInteraction that presents candidates with
    a number of choices and allows them to create associations between them.

    The associateInteraction must be bound to a response variable with
    base-type pair and either single or multiple cardina- lity.
    """

    class Meta:
        name = "AssociateInteractionDType"

    qti_simple_associable_choice: List["SimpleAssociableChoiceDtype"] = field(
        default_factory=list,
        metadata={
            "name": "qti-simple-associable-choice",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    shuffle: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    max_associations: int = field(
        default=1,
        metadata={
            "name": "max-associations",
            "type": "Attribute",
        },
    )
    min_associations: int = field(
        default=0,
        metadata={
            "name": "min-associations",
            "type": "Attribute",
        },
    )


@dataclass
class CatalogDtype:
    """A container of content or resource references that is outside the content
    body node.

    A ca- talog holds support-specific dormant content that can be made
    active (a part of the perce- ivable content presented to the
    candidate) based on the candidate's PNP information (or an
    assessment program's settings). A catalog is referenced from a
    specific portion of the co- ntent body by a specific, unique
    identifier, which matches the catalog's identifier. A ca- talog
    contains one or more "cards", each of which address a specific
    support/feature.
    """

    class Meta:
        name = "CatalogDType"

    qti_card: List[CardDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-card",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ChoiceInteractionDtype(BasePromptInteractionDtype):
    """The choice interaction presents a set of choices to the candidate.

    The candidate's task is to select one or more of the choices, up to
    a maximum of max-choices. The interaction is always initialized with
    no choices selected. The ChoiceInteraction must be bound to a res-
    ponse variable with a base-type of identifier and single or multiple
    cardinality.
    """

    class Meta:
        name = "ChoiceInteractionDType"

    qti_simple_choice: List["SimpleChoiceDtype"] = field(
        default_factory=list,
        metadata={
            "name": "qti-simple-choice",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    shuffle: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    max_choices: int = field(
        default=1,
        metadata={
            "name": "max-choices",
            "type": "Attribute",
        },
    )
    min_choices: int = field(
        default=0,
        metadata={
            "name": "min-choices",
            "type": "Attribute",
        },
    )
    orientation: ChoiceInteractionDtypeOrientation = field(
        default=ChoiceInteractionDtypeOrientation.VERTICAL,
        metadata={
            "type": "Attribute",
        },
    )
    data_min_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-min-selections-message",
            "type": "Attribute",
        },
    )
    data_max_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-max-selections-message",
            "type": "Attribute",
        },
    )


@dataclass
class DrawingInteractionDtype(BasePromptInteractionDtype):
    """The drawing interaction allows the candidate to use a common set of drawing
    tools to modi- fy a given graphical image (the canvas).

    It must be bound to a response variable with bas- e-type file and
    single cardinality. The result is a file in the same format as the
    origin- al image. The use of 'object' to include the background
    image is deprecated and the use of either 'picture' or 'img' is
    preferred.
    """

    class Meta:
        name = "DrawingInteractionDType"

    object_or_img_or_picture: Optional[Union["Object", Img, Picture]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class ExtendedTextInteractionDtype(BasePromptInteractionDtype):
    """An Extended Text Interaction is a block interaction that allows the
    candidate to enter an extended amount of text.

    The qti-extended-text-interaction must be bound to a response va-
    riable of single, multiple, ordered or record cardinality. If the
    response variable has r- ecord cardinality the fields in the record
    must be 'stringValue', 'floatValue', etc. Othe- rwise it ust have a
    base-type of string, integer or float. When bound to response
    variable with single cardinality a single string of text is required
    from the candidate. When bound to a response variable with multiple
    or ordered cardinality several separate text strings may be
    required.
    """

    class Meta:
        name = "ExtendedTextInteractionDType"

    base: int = field(
        default=10,
        metadata={
            "type": "Attribute",
        },
    )
    string_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "string-identifier",
            "type": "Attribute",
        },
    )
    expected_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "expected-length",
            "type": "Attribute",
        },
    )
    pattern_mask: Optional[str] = field(
        default=None,
        metadata={
            "name": "pattern-mask",
            "type": "Attribute",
        },
    )
    placeholder_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "placeholder-text",
            "type": "Attribute",
        },
    )
    max_strings: Optional[int] = field(
        default=None,
        metadata={
            "name": "max-strings",
            "type": "Attribute",
        },
    )
    min_strings: int = field(
        default=0,
        metadata={
            "name": "min-strings",
            "type": "Attribute",
        },
    )
    expected_lines: Optional[int] = field(
        default=None,
        metadata={
            "name": "expected-lines",
            "type": "Attribute",
        },
    )
    format: ExtendedTextInteractionDtypeFormat = field(
        default=ExtendedTextInteractionDtypeFormat.PLAIN,
        metadata={
            "type": "Attribute",
        },
    )
    data_patternmask_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-patternmask-message",
            "type": "Attribute",
        },
    )


@dataclass
class GraphicAssociateInteractionDtype(BasePromptInteractionDtype):
    """A graphic associate interaction is a graphic interaction with a
    corresponding set of choi- ces that are defined as areas of the graphic image.

    The candidate's task is to associate the areas (hotspots) with each
    other. The graphic associate interaction should only be us- ed when
    the graphical relationship of the choices with respect to each other
    (as represen- ted by the graphic image) is important to the needs of
    the item. Otherwise, associateInte- raction should be used instead
    with separate Material for each option. The delivery engine must
    clearly indicate all defined area(s) of the image. The
    graphicAssociateInteraction m- ust be bound to a response variable
    with base-type pair and either single or multiple car- dinality.
    """

    class Meta:
        name = "GraphicAssociateInteractionDType"

    object_or_img_or_picture: Optional[Union["Object", Img, Picture]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    qti_associable_hotspot: List[AssociableHotspotDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-associable-hotspot",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    min_associations: Optional[int] = field(
        default=None,
        metadata={
            "name": "min-associations",
            "type": "Attribute",
        },
    )
    max_associations: int = field(
        default=1,
        metadata={
            "name": "max-associations",
            "type": "Attribute",
        },
    )


@dataclass
class HotspotInteractionDtype(BasePromptInteractionDtype):
    """A hotspot interaction is a graphical interaction with a corresponding set of
    choices that are defined as areas of the graphic image.

    The candidate's task is to select one or more of the areas
    (hotspots). The hotspot interaction should only be used when the
    spacial rel- ationship of the choices with respect to each other (as
    represented by the graphic image) is important to the needs of the
    item. Otherwise, choiceInteraction should be used instead with
    separate material for each option. The delivery engine must clearly
    indicate the sel- ected area(s) of the image and may also indicate
    the unselected areas as well. Interactio- ns with hidden hotspots
    are achieved with the selectPointInteraction. The hotspot interac-
    tion must be bound to a response variable with a base-type of
    identifier and single or mu- ltiple cardinality.
    """

    class Meta:
        name = "HotspotInteractionDType"

    object_or_img_or_picture: Optional[Union["Object", Img, Picture]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    qti_hotspot_choice: List[HotspotChoiceDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-hotspot-choice",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    min_choices: int = field(
        default=0,
        metadata={
            "name": "min-choices",
            "type": "Attribute",
        },
    )
    max_choices: int = field(
        default=1,
        metadata={
            "name": "max-choices",
            "type": "Attribute",
        },
    )
    data_min_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-min-selections-message",
            "type": "Attribute",
        },
    )
    data_max_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-max-selections-message",
            "type": "Attribute",
        },
    )


@dataclass
class MatchInteractionDtype(BasePromptInteractionDtype):
    """A match interaction is a blockInteraction that presents candidates with two
    sets of choic- es and allows them to create associates between pairs of choices
    in the two sets, but not between pairs of choices in the same set.

    Further restrictions can still be placed on the allowable
    associations using the match-max characteristic of the choices. The
    matchIntera- ction must be bound to a response variable with base-
    type 'directedPair' and either single or multiple cardinality.
    """

    class Meta:
        name = "MatchInteractionDType"

    qti_simple_match_set: List["SimpleMatchSetDtype"] = field(
        default_factory=list,
        metadata={
            "name": "qti-simple-match-set",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    shuffle: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    max_associations: int = field(
        default=1,
        metadata={
            "name": "max-associations",
            "type": "Attribute",
        },
    )
    min_associations: int = field(
        default=0,
        metadata={
            "name": "min-associations",
            "type": "Attribute",
        },
    )
    data_min_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-min-selections-message",
            "type": "Attribute",
        },
    )
    data_max_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-max-selections-message",
            "type": "Attribute",
        },
    )
    data_first_column_header: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-first-column-header",
            "type": "Attribute",
        },
    )


@dataclass
class MediaInteractionDtype(BasePromptInteractionDtype):
    """
    The Media Interaction allows more control over the way the candidate interacts
    with a tim- e-based media object and allows the number of times the media
    object was experienced to be reported in the value of the associated response
    variable, which must be of base-type int- eger and single cardinality.
    """

    class Meta:
        name = "MediaInteractionDType"

    object_or_audio_or_video: Optional[
        Union["Object", ImsglobalXsdImsqtiasiV3P0AudioAudio, Video]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    autostart: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    min_plays: int = field(
        default=0,
        metadata={
            "name": "min-plays",
            "type": "Attribute",
        },
    )
    max_plays: int = field(
        default=0,
        metadata={
            "name": "max-plays",
            "type": "Attribute",
        },
    )
    loop: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    coords: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(([0-9]+%?[,]){2}([0-9]+%?))|(([0-9]+%?[,]){3}([0-9]+%?))|(([0-9]+%?[,]){2}(([0-9]+%?[,]){2})+([0-9]+%?[,])([0-9]+%?))",
        },
    )


@dataclass
class OrderInteractionDtype(BasePromptInteractionDtype):
    """In an Order Interaction the candidate's task is to reorder the choices, the
    order in which the choices are displayed initially is significant.

    By default the candidate's task is to order all of the choices but a
    subset of the choices can be requested using the max-choic- es and
    min-choices attributes. When specified the candidate must select a
    subset of the c- hoices and impose an ordering on them.
    """

    class Meta:
        name = "OrderInteractionDType"

    qti_simple_choice: List["SimpleChoiceDtype"] = field(
        default_factory=list,
        metadata={
            "name": "qti-simple-choice",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    shuffle: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    min_choices: Optional[int] = field(
        default=None,
        metadata={
            "name": "min-choices",
            "type": "Attribute",
        },
    )
    max_choices: Optional[int] = field(
        default=None,
        metadata={
            "name": "max-choices",
            "type": "Attribute",
        },
    )
    orientation: Optional[OrderInteractionDtypeOrientation] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    data_min_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-min-selections-message",
            "type": "Attribute",
        },
    )
    data_max_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-max-selections-message",
            "type": "Attribute",
        },
    )
    data_choices_container_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "data-choices-container-width",
            "type": "Attribute",
        },
    )


@dataclass
class SliderInteractionDtype(BasePromptInteractionDtype):
    """The Slider Interaction presents the candidate with a control for selecting a
    numerical va- lue between a lower and upper bound.

    It must be bound to a response variable with single cardinality with
    a base-type of either integer or float. Note that a slider
    interaction d- oes not have a default or initial position except
    where specified by a default value for the associated response
    variable. The currently selected value, if any, must be clearly i-
    ndicated to the candidate. Because a slider interaction does not
    have a default or initial position, except where specified by a
    default value for the associated response variable, it is difficult
    to distinguish between an intentional response that corresponds to
    the sl- ider's initial position and a NULL response. As a
    workaround, sliderInteraction items have to either a) not count NULL
    responses (i.e. count all responses as intentional) or b) inc- lude
    a 'skip' button and count its activation combined with a RESPONSE
    variable that is e- qual to the slider's initial position as a NULL
    response.
    """

    class Meta:
        name = "SliderInteractionDType"

    lower_bound: Optional[float] = field(
        default=None,
        metadata={
            "name": "lower-bound",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    upper_bound: Optional[float] = field(
        default=None,
        metadata={
            "name": "upper-bound",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    step: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    step_label: bool = field(
        default=False,
        metadata={
            "name": "step-label",
            "type": "Attribute",
        },
    )
    orientation: Optional[SliderInteractionDtypeOrientation] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reverse: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class UploadInteractionDtype(BasePromptInteractionDtype):
    """The Upload Interaction allows the candidate to upload a pre-prepared file
    representing th- eir response.

    It must be bound to a response variable with base-type file and
    single card- inality.
    """

    class Meta:
        name = "UploadInteractionDType"

    type_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Attribute",
            "pattern": r'[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+/[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+',
            "tokens": True,
        },
    )


@dataclass
class A(Adtype):
    class Meta:
        name = "a"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class BaseHtml5FlowDtype(BaseSequenceDtype):
    """This is the base class for the HTML5 tags that support a large range of
    child HTML and QTI interaction tags.

    This set of child tags are used to create a coherent flow of
    content.
    """

    class Meta:
        name = "BaseHTML5FlowDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-block",
                    "type": ForwardRef("FeedbackBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext",
                    "type": ForwardRef("HotTextDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": ForwardRef("FeedbackInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": ForwardRef("TemplateBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-text-entry-interaction",
                    "type": TextEntryInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inline-choice-interaction",
                    "type": ForwardRef("InlineChoiceInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-end-attempt-interaction",
                    "type": EndAttemptInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-interaction",
                    "type": CustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-portable-custom-interaction",
                    "type": ForwardRef("PortableCustomInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-drawing-interaction",
                    "type": ForwardRef("DrawingInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap-match-interaction",
                    "type": ForwardRef("GapMatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match-interaction",
                    "type": ForwardRef("MatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-gap-match-interaction",
                    "type": ForwardRef("GraphicGapMatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hotspot-interaction",
                    "type": ForwardRef("HotspotInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-order-interaction",
                    "type": ForwardRef("GraphicOrderInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-select-point-interaction",
                    "type": ForwardRef("SelectPointInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-associate-interaction",
                    "type": ForwardRef("GraphicAssociateInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-slider-interaction",
                    "type": ForwardRef("SliderInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-choice-interaction",
                    "type": ForwardRef("ChoiceInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-media-interaction",
                    "type": ForwardRef("MediaInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext-interaction",
                    "type": ForwardRef("HotTextInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-order-interaction",
                    "type": ForwardRef("OrderInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-extended-text-interaction",
                    "type": ForwardRef("ExtendedTextInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-upload-interaction",
                    "type": ForwardRef("UploadInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-associate-interaction",
                    "type": ForwardRef("AssociateInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": ForwardRef("H1"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": ForwardRef("H2"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": ForwardRef("H3"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": ForwardRef("H4"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": ForwardRef("H5"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": ForwardRef("H6"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ForwardRef("P"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": ForwardRef("Address"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("Dl"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": ForwardRef("Blockquote"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": ForwardRef("Div"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": ForwardRef("Bdo"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": ForwardRef("Bdi"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": ForwardRef("Figure"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": ForwardRef("Article"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": ForwardRef("Aside"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": ForwardRef("Footer"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": ForwardRef("Header"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": ForwardRef("Label"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": ForwardRef("Nav"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": ForwardRef("Section"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": ForwardRef("Details"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class CatalogInfoDtype:
    """The container that holds one or more catalogs and their content.

    Content inside CatalogIn- fo is considered "dormant" and is not
    included for delivery to candidates by default. A c- andidate's
    profile (or assessment program settings) will indicate whether the
    candidate s- hould be presented any of the possible supports
    included within the CatalogInfo.
    """

    class Meta:
        name = "CatalogInfoDType"

    qti_catalog: List[CatalogDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-catalog",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )


@dataclass
class FeedbackBlockDtype(BaseSequenceXbaseDtype):
    """This class is used to define the feedback content that can be presented to
    the learner.

    A feedback element that forms part of a Non-adaptive Item must not
    contain an interaction o- bject, either directly or indirectly. When
    an interaction is contained in a hidden feedba- ck element it must
    also be hidden. The candidate must not be able to set or update the
    va- lue of the associated response variables. Feedback elements can
    be embedded inside each o- ther, with one exception: qti-feedback-
    inline cannot contain qti-feedback-block elements.
    """

    class Meta:
        name = "FeedbackBlockDType"

    qti_stylesheet: List[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_content_body: Optional["FeedbackContentBodyDtype"] = field(
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
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    show_hide: FeedbackBlockDtypeShowHide = field(
        default=FeedbackBlockDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )


@dataclass
class TemplateBlockContentDtype(BaseSequenceXbaseDtype):
    """
    This container class is used to define the common block content structures that
    are avail- able for the creation of Item templates.
    """

    class Meta:
        name = "TemplateBlockContentDType"

    qti_stylesheet: List[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_content_body: Optional["TemplateBlockContentBodyDtype"] = field(
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


@dataclass
class Article(BaseHtml5FlowDtype):
    class Meta:
        name = "article"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Aside(BaseHtml5FlowDtype):
    class Meta:
        name = "aside"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Figcaption(BaseHtml5FlowDtype):
    class Meta:
        name = "figcaption"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Footer(BaseHtml5FlowDtype):
    class Meta:
        name = "footer"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Header(BaseHtml5FlowDtype):
    class Meta:
        name = "header"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Label(BaseHtml5FlowDtype):
    class Meta:
        name = "label"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Nav(BaseHtml5FlowDtype):
    class Meta:
        name = "nav"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Section(BaseHtml5FlowDtype):
    class Meta:
        name = "section"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Bdidtype(BaseSequenceDtype):
    """The 'bdi' tag is an HTML5 feature.

    This defines the content for defining bidirectional co- ntent. The
    bdi tag represents a span of text that is to be isolated from its
    surroundings for the purposes of bidirectional text formatting.
    """

    class Meta:
        name = "BDIDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": ForwardRef("H1"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": ForwardRef("H2"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": ForwardRef("H3"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": ForwardRef("H4"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": ForwardRef("H5"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": ForwardRef("H6"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ForwardRef("P"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": ForwardRef("Address"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("Dl"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": ForwardRef("Blockquote"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": ForwardRef("Div"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": ForwardRef("Bdo"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": ForwardRef("Bdi"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": ForwardRef("Figure"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": ForwardRef("Details"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class BaseHtml5PhrasingDtype(BaseSequenceDtype):
    """This class is used to enable the complex capabilities of the 'ruby' tag.

    Ruby annotations are short runs of text presented alongside base
    text, primarily used in East Asian typogr- aphy as a guide for
    pronunciation or to include other annotations.
    """

    class Meta:
        name = "BaseHTML5PhrasingDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": ForwardRef("Bdo"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": ForwardRef("Bdi"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class TemplateBlockDtype(TemplateBlockContentDtype):
    """This class is used to define the block content structures that are available
    for the crea- tion of Item templates.

    A qti-template-block must not contain any interactions, either di-
    rectly or indirectly.
    """

    class Meta:
        name = "TemplateBlockDType"

    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    show_hide: TemplateBlockDtypeShowHide = field(
        default=TemplateBlockDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TemplateBlockFeedbackBlockDtype(TemplateBlockContentDtype):
    """This enables the Block content to be placed in template blocks.

    This structure is used to add constraints on how the block content
    can be used in recursive block templates.
    """

    class Meta:
        name = "TemplateBlockFeedbackBlockDType"

    outcome_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "outcome-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    show_hide: TemplateBlockFeedbackBlockDtypeShowHide = field(
        default=TemplateBlockFeedbackBlockDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Bdi(Bdidtype):
    class Meta:
        name = "bdi"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Rb(BaseHtml5PhrasingDtype):
    class Meta:
        name = "rb"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Rp(BaseHtml5PhrasingDtype):
    class Meta:
        name = "rp"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Rt(BaseHtml5PhrasingDtype):
    class Meta:
        name = "rt"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Summary(BaseHtml5PhrasingDtype):
    class Meta:
        name = "summary"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Bdodtype(BaseSequenceDtype):
    """This enables the HTML 'bdo' tag.

    The 'bdo' tag represents explicit text directionality fo- rmatting
    control for its children. It allows authors to override the Unicode
    bidirectional algorithm by explicitly specifying a direction
    override. Authors must specify the dir att- ribute on this tag, with
    the value ltr to specify a left-to-right override and with the v-
    alue rtl to specify a right-to-left override. The auto value must
    not be specified.
    """

    class Meta:
        name = "BDODType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": ForwardRef("Bdo"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class Bdo(Bdodtype):
    class Meta:
        name = "bdo"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class BlockQuoteDtype(BaseSequenceXbaseDtype):
    """This defines the content of the 'blockquote' HTML tag.

    The 'blockquote' tag represents co- ntent that is quoted from
    another source, optionally with a citation which must be within a
    footer or cite element, and optionally with in-line changes such as
    annotations and abb- reviations. Content inside a blockquote other
    than citations and in-line changes must be quoted from another
    source, whose address, if it has one, may be cited in the cite
    attrib- ute. The content of a blockquote may be abbreviated, may
    have context added or may have a- nnotations. Any such additions or
    changes to quoted text must be indicated in the text (at the text
    level). This may mean the use of notational conventions or explicit
    remarks, such as "emphasis mine".
    """

    class Meta:
        name = "BlockQuoteDType"

    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": ForwardRef("H1"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": ForwardRef("H2"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": ForwardRef("H3"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": ForwardRef("H4"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": ForwardRef("H5"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": ForwardRef("H6"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ForwardRef("P"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": ForwardRef("Address"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("Dl"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": ForwardRef("Blockquote"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": ForwardRef("Div"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": ForwardRef("Figure"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": ForwardRef("Details"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class FeedbackInlineDtype(BaseSequenceXbaseDtype):
    """This is feedback that is presented as inline content.

    Inline feedback that forms part of a Non-adaptive Item must not
    contain an interaction object, either directly or indirectly. When
    an interaction is contained in a hidden feedback it must also be
    hidden. The candida- te must not be able to set or update the value
    of the associated response variables. Feed- back can be embedded
    inside each other, with one exception: qti-feedback-inline cannot
    co- ntain feedback block elements.
    """

    class Meta:
        name = "FeedbackInlineDType"

    outcome_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "outcome-identifier",
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
    show_hide: FeedbackInlineDtypeShowHide = field(
        default=FeedbackInlineDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class GapTextDtype(BaseSequenceDtype):
    """
    A simple run of text to be inserted into a gap by the user, may be subject to
    variable va- lue substitution with qti-printed-variable.
    """

    class Meta:
        name = "GapTextDType"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
        },
    )
    show_hide: GapTextDtypeShowHide = field(
        default=GapTextDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    match_group: List[str] = field(
        default_factory=list,
        metadata={
            "name": "match-group",
            "type": "Attribute",
            "tokens": True,
        },
    )
    match_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "match-max",
            "type": "Attribute",
            "required": True,
        },
    )
    match_min: int = field(
        default=0,
        metadata={
            "name": "match-min",
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class HotTextDtype(BaseSequenceXbaseDtype):
    """A HotText area is used within the content of an hotTextInteraction to
    provide the individ- ual choices.

    It must not contain any nested interactions or other hottext areas.
    When a h- ottext choice is hidden (by the value of an associated
    template variable) the content of the choice must still be presented
    to the candidate as if it were simply part of the surr- ounding
    material. In the case of hottext, the effect of hiding the choice is
    simply to ma- ke the run of text unselectable by the candidate.
    """

    class Meta:
        name = "HotTextDType"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
        },
    )
    show_hide: HotTextDtypeShowHide = field(
        default=HotTextDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class Blockquote(BlockQuoteDtype):
    class Meta:
        name = "blockquote"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class CaptionDtype(BaseSequenceDtype):
    """Provides the HTML 'caption' tag functionality.

    The 'caption' tag represents the title of the table that is its
    parent, if it has a parent and that is a 'table' tag. The caption t-
    ag takes part in the table model. When a table tag is the only
    content in a figure tag ot- her than the figcaption, the caption tag
    should be omitted in favor of the figcaption. A caption can
    introduce context for a table, making it significantly easier to
    understand.
    """

    class Meta:
        name = "CaptionDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-block",
                    "type": ForwardRef("FeedbackBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext",
                    "type": ForwardRef("HotTextDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": ForwardRef("FeedbackInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": ForwardRef("TemplateBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-text-entry-interaction",
                    "type": TextEntryInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inline-choice-interaction",
                    "type": ForwardRef("InlineChoiceInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-end-attempt-interaction",
                    "type": EndAttemptInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-interaction",
                    "type": CustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-portable-custom-interaction",
                    "type": ForwardRef("PortableCustomInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-drawing-interaction",
                    "type": ForwardRef("DrawingInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap-match-interaction",
                    "type": ForwardRef("GapMatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match-interaction",
                    "type": ForwardRef("MatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-gap-match-interaction",
                    "type": ForwardRef("GraphicGapMatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hotspot-interaction",
                    "type": ForwardRef("HotspotInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-order-interaction",
                    "type": ForwardRef("GraphicOrderInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-select-point-interaction",
                    "type": ForwardRef("SelectPointInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-associate-interaction",
                    "type": ForwardRef("GraphicAssociateInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-slider-interaction",
                    "type": SliderInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-choice-interaction",
                    "type": ForwardRef("ChoiceInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-media-interaction",
                    "type": ForwardRef("MediaInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext-interaction",
                    "type": ForwardRef("HotTextInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-order-interaction",
                    "type": ForwardRef("OrderInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-extended-text-interaction",
                    "type": ExtendedTextInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-upload-interaction",
                    "type": UploadInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-associate-interaction",
                    "type": AssociateInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": ForwardRef("H1"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": ForwardRef("H2"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": ForwardRef("H3"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": ForwardRef("H4"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": ForwardRef("H5"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": ForwardRef("H6"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ForwardRef("P"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": ForwardRef("Address"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("Dl"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": ForwardRef("Div"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": ForwardRef("Figure"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": ForwardRef("Details"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class Dddtype(BaseSequenceXbaseDtype):
    """The 'dd' tag is a part of the HTML content.

    The 'dd' tag represents the description, defi- nition, or value,
    part of a term-description group in a description list ('dl' tag).
    """

    class Meta:
        name = "DDDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-block",
                    "type": ForwardRef("FeedbackBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext",
                    "type": ForwardRef("HotTextDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": ForwardRef("FeedbackInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": ForwardRef("TemplateBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-text-entry-interaction",
                    "type": TextEntryInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inline-choice-interaction",
                    "type": ForwardRef("InlineChoiceInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-end-attempt-interaction",
                    "type": EndAttemptInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-interaction",
                    "type": CustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-portable-custom-interaction",
                    "type": ForwardRef("PortableCustomInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-drawing-interaction",
                    "type": ForwardRef("DrawingInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap-match-interaction",
                    "type": ForwardRef("GapMatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match-interaction",
                    "type": ForwardRef("MatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-gap-match-interaction",
                    "type": ForwardRef("GraphicGapMatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hotspot-interaction",
                    "type": ForwardRef("HotspotInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-order-interaction",
                    "type": ForwardRef("GraphicOrderInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-select-point-interaction",
                    "type": ForwardRef("SelectPointInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-associate-interaction",
                    "type": ForwardRef("GraphicAssociateInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-slider-interaction",
                    "type": SliderInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-choice-interaction",
                    "type": ChoiceInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-media-interaction",
                    "type": ForwardRef("MediaInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext-interaction",
                    "type": ForwardRef("HotTextInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-order-interaction",
                    "type": ForwardRef("OrderInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-extended-text-interaction",
                    "type": ExtendedTextInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-upload-interaction",
                    "type": UploadInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-associate-interaction",
                    "type": AssociateInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": ForwardRef("H1"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": ForwardRef("H2"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": ForwardRef("H3"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": ForwardRef("H4"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": ForwardRef("H5"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": ForwardRef("H6"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ForwardRef("P"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": ForwardRef("Address"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("Dl"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": ForwardRef("Div"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": ForwardRef("Figure"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": ForwardRef("Details"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class DetailsDtype(BaseSequenceDtype):
    """This provides the functionality of the HTML 'details' tag (a new tag added
    in HTML5).

    This tag creates a disclosure widget in which information is visible
    only when the widget is t- oggled into an 'open' state.
    """

    class Meta:
        name = "DetailsDType"

    summary: Optional[Summary] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
    choice: List[
        Union[
            "Pre",
            "H1",
            "H2",
            "H3",
            "H4",
            "H5",
            "H6",
            "P",
            "Address",
            "Dl",
            "Ol",
            "Ul",
            Br,
            Hr,
            Img,
            "Object",
            Blockquote,
            "Em",
            A,
            "Code",
            "Span",
            "Sub",
            "Acronym",
            "Big",
            "Tt",
            "Kbd",
            "Q",
            "I",
            "Dfn",
            "Abbr",
            "Strong",
            "Sup",
            "Var",
            "Small",
            "Samp",
            "B",
            "Cite",
            "Table",
            "Div",
            Bdo,
            Bdi,
            "Figure",
            ImsglobalXsdImsqtiasiV3P0AudioAudio,
            Video,
            Article,
            Aside,
            Footer,
            Header,
            Label,
            Nav,
            Section,
            "Ruby",
            ParagraphP,
            S,
            SayAs,
            Phoneme,
            SubSub,
            Voice,
            Emphasis,
            Break,
            Prosody,
            Mark,
            W3Pkg2001Pkg10SynthesisParagraphAudio,
            Speak,
            Picture,
            "Details",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": ForwardRef("H1"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": ForwardRef("H2"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": ForwardRef("H3"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": ForwardRef("H4"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": ForwardRef("H5"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": ForwardRef("H6"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ForwardRef("P"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": ForwardRef("Address"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("Dl"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": ForwardRef("Div"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": ForwardRef("Figure"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": ForwardRef("Details"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    open: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class GraphicGapMatchInteractionDtype(BaseSequenceFullDtype):
    """A graphic gap-match interaction is a graphical interaction with a set of
    gaps that are de- fined as areas (hotspots) of the graphic image and an
    additional set of gap choices that are defined outside the image.

    The candidate must associate the gap choices with the gaps in the
    image and be able to review the image with the gaps filled in
    context, as indicated by their choices. Care should be taken when
    designing these interactions to ensure that t- he gaps in the image
    are a suitable size to receive the required gap choices. It must be
    clear to the candidate which hotspot each choice has been associated
    with. When associate- d, choices must appear wholly inside the gaps
    if at all possible and, where overlaps are required, should not hide
    each other completely. If the candidate indicates the associati- on
    by positioning the choice over the gap (e.g. drag and drop) the
    system should 'snap' it to the nearest position that satisfies these
    requirements. The graphicGapMatchInteraction must be bound to a
    response variable with base-type directedPair and multiple
    cardinality. The choices represent the source of the pairing and the
    gaps in the image (the hotspots) the targets. Unlike the simple
    gapMatchInteraction, each gap can have several choices ass- ociated
    with it if desired, furthermore, the same choice may be associated
    with an associ- ableHotspot multiple times, in which case the
    corresponding directed pair appears multiple times in the value of
    the response variable.
    """

    class Meta:
        name = "GraphicGapMatchInteractionDType"

    qti_prompt: Optional["PromptDtype"] = field(
        default=None,
        metadata={
            "name": "qti-prompt",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    object_or_img_or_picture: Optional[Union["Object", Img, Picture]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    qti_gap_text_or_qti_gap_img: List[Union[GapTextDtype, GapImgDtype]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "qti-gap-text",
                        "type": GapTextDtype,
                        "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    },
                    {
                        "name": "qti-gap-img",
                        "type": GapImgDtype,
                        "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    },
                ),
            },
        )
    )
    qti_associable_hotspot: List[AssociableHotspotDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-associable-hotspot",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    min_associations: Optional[int] = field(
        default=None,
        metadata={
            "name": "min-associations",
            "type": "Attribute",
        },
    )
    max_associations: int = field(
        default=1,
        metadata={
            "name": "max-associations",
            "type": "Attribute",
        },
    )
    data_min_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-min-selections-message",
            "type": "Attribute",
        },
    )
    data_max_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-max-selections-message",
            "type": "Attribute",
        },
    )
    data_choices_container_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "data-choices-container-width",
            "type": "Attribute",
        },
    )


@dataclass
class HtmltextDtype(BaseSequenceXbaseDtype):
    """
    This provides the content for text-based HTML tags e.g. 'pre', 'p', 'h1', 'h2',
    etc.
    """

    class Meta:
        name = "HTMLTextDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-text-entry-interaction",
                    "type": TextEntryInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext",
                    "type": HotTextDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap",
                    "type": GapDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inline-choice-interaction",
                    "type": ForwardRef("InlineChoiceInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-end-attempt-interaction",
                    "type": EndAttemptInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-interaction",
                    "type": CustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class Abbr(HtmltextDtype):
    class Meta:
        name = "abbr"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Acronym(HtmltextDtype):
    class Meta:
        name = "acronym"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Address(HtmltextDtype):
    class Meta:
        name = "address"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class B(HtmltextDtype):
    class Meta:
        name = "b"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Big(HtmltextDtype):
    class Meta:
        name = "big"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Caption(CaptionDtype):
    class Meta:
        name = "caption"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Cite(HtmltextDtype):
    class Meta:
        name = "cite"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Code(HtmltextDtype):
    class Meta:
        name = "code"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Dd(Dddtype):
    class Meta:
        name = "dd"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Details(DetailsDtype):
    class Meta:
        name = "details"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Dfn(HtmltextDtype):
    class Meta:
        name = "dfn"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Em(HtmltextDtype):
    class Meta:
        name = "em"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class H1(HtmltextDtype):
    class Meta:
        name = "h1"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class H2(HtmltextDtype):
    class Meta:
        name = "h2"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class H3(HtmltextDtype):
    class Meta:
        name = "h3"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class H4(HtmltextDtype):
    class Meta:
        name = "h4"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class H5(HtmltextDtype):
    class Meta:
        name = "h5"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class H6(HtmltextDtype):
    class Meta:
        name = "h6"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class I(HtmltextDtype):
    class Meta:
        name = "i"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Kbd(HtmltextDtype):
    class Meta:
        name = "kbd"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class P(HtmltextDtype):
    class Meta:
        name = "p"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Pre(HtmltextDtype):
    class Meta:
        name = "pre"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Samp(HtmltextDtype):
    class Meta:
        name = "samp"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Small(HtmltextDtype):
    class Meta:
        name = "small"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Span(HtmltextDtype):
    class Meta:
        name = "span"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Strong(HtmltextDtype):
    class Meta:
        name = "strong"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Sub(HtmltextDtype):
    class Meta:
        name = "sub"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Sup(HtmltextDtype):
    class Meta:
        name = "sup"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Tt(HtmltextDtype):
    class Meta:
        name = "tt"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Var(HtmltextDtype):
    class Meta:
        name = "var"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Dldtype(BaseSequenceXbaseDtype):
    """Denotes the 'dl' HTML tag.

    The 'dl' tag represents an association list consisting of zero or
    more name-value groups (a description list). A name-value group
    consists of one or more names ('dt' tags) followed by one or more
    values ('dd' tags), ignoring any nodes other th- an 'dt' and 'dd'
    tags. Within a single 'dl' tag, there should not be more than one
    'dt' t- ag for each name.
    """

    class Meta:
        name = "DLDType"

    dd_or_dt: List[Union[Dd, "Dt"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "dd",
                    "type": Dd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dt",
                    "type": ForwardRef("Dt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class DivDtype(BaseSequenceXbaseDtype):
    """This provides the functionality of the HTML 'div' tag.

    The div tag has no special meaning at all. It represents its
    children. It can be used with the class, lang, and title charac-
    teristics to mark up semantics common to a group of consecutive
    elements. Authors are str- ongly encouraged to view the div tag as
    an element of last resort, for when no other elem- ent is suitable.
    Use of more appropriate elements instead of the div element leads to
    bet- ter accessibility for readers and easier maintainability for
    authors.
    """

    class Meta:
        name = "DivDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-position-object-stage",
                    "type": ForwardRef("PositionObjectStageDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-block",
                    "type": ForwardRef("FeedbackBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext",
                    "type": ForwardRef("HotTextDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": ForwardRef("FeedbackInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": ForwardRef("TemplateBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-text-entry-interaction",
                    "type": TextEntryInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inline-choice-interaction",
                    "type": ForwardRef("InlineChoiceInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-end-attempt-interaction",
                    "type": EndAttemptInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-interaction",
                    "type": CustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-portable-custom-interaction",
                    "type": ForwardRef("PortableCustomInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-drawing-interaction",
                    "type": ForwardRef("DrawingInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap-match-interaction",
                    "type": ForwardRef("GapMatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match-interaction",
                    "type": ForwardRef("MatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-gap-match-interaction",
                    "type": ForwardRef("GraphicGapMatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hotspot-interaction",
                    "type": ForwardRef("HotspotInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-order-interaction",
                    "type": ForwardRef("GraphicOrderInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-select-point-interaction",
                    "type": ForwardRef("SelectPointInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-associate-interaction",
                    "type": ForwardRef("GraphicAssociateInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-slider-interaction",
                    "type": SliderInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-choice-interaction",
                    "type": ChoiceInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-media-interaction",
                    "type": ForwardRef("MediaInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext-interaction",
                    "type": ForwardRef("HotTextInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-order-interaction",
                    "type": ForwardRef("OrderInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-extended-text-interaction",
                    "type": ExtendedTextInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-upload-interaction",
                    "type": UploadInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-associate-interaction",
                    "type": AssociateInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": ForwardRef("H1"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": ForwardRef("H2"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": ForwardRef("H3"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": ForwardRef("H4"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": ForwardRef("H5"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": ForwardRef("H6"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ForwardRef("P"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": ForwardRef("Address"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("Dl"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": ForwardRef("Div"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": ForwardRef("Figure"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": Details,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class InlineChoiceDtype(BaseSequenceDtype):
    """
    A simple run of text to be displayed to the user, may be subject to variable
    value substi- tution with printedVariable.
    """

    class Meta:
        name = "InlineChoiceDType"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    fixed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
        },
    )
    show_hide: InlineChoiceDtypeShowHide = field(
        default=InlineChoiceDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class TableDtype(BaseSequenceXbaseDtype):
    """
    This provides the HTML 'table' tag functionality within the QTI context.
    """

    class Meta:
        name = "TableDType"

    caption: Optional[Caption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    col: List[Col] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    colgroup: List[Colgroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    thead: Optional["Thead"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    tfoot: Optional["Tfoot"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    tbody: List["Tbody"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    tr: List["Tr"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InlineChoiceInteractionDtype(BaseSequenceFullDtype):
    """An inline choice is an inline Interaction that presents the user with a set
    of choices, e- ach of which is a simple piece of text.

    The candidate's task is to select one of the choi- ces. Unlike the
    choiceInteraction, the delivery engine must allow the candidate to
    review their choice within the context of the surrounding text. The
    inlineChoiceInteraction must be bound to a response variable with a
    base-type of identifier and single cardinality onl- y.
    """

    class Meta:
        name = "InlineChoiceInteractionDType"

    qti_label: Optional["LabelDtype"] = field(
        default=None,
        metadata={
            "name": "qti-label",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_inline_choice: List[InlineChoiceDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-inline-choice",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    shuffle: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    required: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    min_choices: int = field(
        default=0,
        metadata={
            "name": "min-choices",
            "type": "Attribute",
        },
    )
    data_min_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-min-selections-message",
            "type": "Attribute",
        },
    )
    data_prompt: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-prompt",
            "type": "Attribute",
        },
    )


@dataclass
class Div(DivDtype):
    class Meta:
        name = "div"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Dl(Dldtype):
    class Meta:
        name = "dl"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Table(TableDtype):
    class Meta:
        name = "table"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class FigureDtype(BaseSequenceDtype):
    """This defines the permitted content for the HTML5 'figure' tag.

    The 'figure' tag represents some flow content, optionally with a
    caption, that is self-contained (like a complete sen- tence) and is
    typically referenced as a single unit from the main flow of the
    document.
    """

    class Meta:
        name = "FigureDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "figcaption",
                    "type": Figcaption,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": ForwardRef("H1"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": ForwardRef("H2"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": ForwardRef("H3"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": ForwardRef("H4"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": ForwardRef("H5"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": ForwardRef("H6"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ForwardRef("P"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": ForwardRef("Address"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": ForwardRef("Figure"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": Details,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class Figure(FigureDtype):
    class Meta:
        name = "figure"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class GapMatchInteractionDtype(BasePromptInteractionDtype):
    """A gap match interaction is a block interaction that contains a number gaps
    that the candi- date can fill from an associated set of choices.

    The candidate must be able to review the content with the gaps
    filled in context, as indicated by their choices. The GapMatchInter-
    action must be bound to a response variable with base-type
    directedPair and either single or multiple cardinality, depending on
    the number of gaps. The choices represent the source of the pairing
    and gaps the targets. Each gap can have at most one choice
    associated with it. The maximum occurrence of the choices is
    controlled by the match-max characteristic of GapChoice.
    """

    class Meta:
        name = "GapMatchInteractionDType"

    qti_gap_text_or_qti_gap_img: List[Union["GapTextDtype", GapImgDtype]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "qti-gap-text",
                        "type": ForwardRef("GapTextDtype"),
                        "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    },
                    {
                        "name": "qti-gap-img",
                        "type": GapImgDtype,
                        "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    },
                ),
            },
        )
    )
    choice: List[
        Union[
            FeedbackBlockDtype,
            "TemplateBlockDtype",
            Math,
            Include,
            "Pre",
            "H1",
            "H2",
            "H3",
            "H4",
            "H5",
            "H6",
            "P",
            "Address",
            Dl,
            "Ol",
            "Ul",
            Hr,
            Blockquote,
            "Table",
            Div,
            Article,
            Aside,
            ImsglobalXsdImsqtiasiV3P0AudioAudio,
            Figure,
            Footer,
            Header,
            Nav,
            Section,
            Video,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-feedback-block",
                    "type": FeedbackBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": ForwardRef("TemplateBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": ForwardRef("H1"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": ForwardRef("H2"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": ForwardRef("H3"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": ForwardRef("H4"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": ForwardRef("H5"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": ForwardRef("H6"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ForwardRef("P"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": ForwardRef("Address"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    shuffle: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    min_associations: Optional[int] = field(
        default=None,
        metadata={
            "name": "min-associations",
            "type": "Attribute",
        },
    )
    max_associations: int = field(
        default=1,
        metadata={
            "name": "max-associations",
            "type": "Attribute",
        },
    )
    data_min_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-min-selections-message",
            "type": "Attribute",
        },
    )
    data_max_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-max-selections-message",
            "type": "Attribute",
        },
    )
    data_choices_container_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "data-choices-container-width",
            "type": "Attribute",
        },
    )


@dataclass
class HotTextInteractionDtype(BasePromptInteractionDtype):
    """The HotText Interaction presents a set of choices to the candidate
    represented as selecta- ble runs of text embedded within a surrounding context,
    such as a simple passage of text.

    Like choiceInteraction, the candidate's task is to select one or
    more of the choices, up to a maximum of max-choices. The interaction
    is initialized from the qti-default-value of the associated response
    variable, a NULL value indicating that no choices are selected (t-
    he usual case). The qti-hottext-interaction must be bound to a
    response variable with a b- ase-type of identifier and single or
    multiple cardinality.
    """

    class Meta:
        name = "HotTextInteractionDType"

    choice: List[
        Union[
            FeedbackBlockDtype,
            "TemplateBlockDtype",
            Math,
            Include,
            "Pre",
            "H1",
            "H2",
            "H3",
            "H4",
            "H5",
            "H6",
            "P",
            "Address",
            Dl,
            "Ol",
            "Ul",
            Hr,
            Blockquote,
            "Table",
            Div,
            Article,
            Aside,
            ImsglobalXsdImsqtiasiV3P0AudioAudio,
            Figure,
            Footer,
            Header,
            Nav,
            Section,
            Video,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-feedback-block",
                    "type": FeedbackBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": ForwardRef("TemplateBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": ForwardRef("H1"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": ForwardRef("H2"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": ForwardRef("H3"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": ForwardRef("H4"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": ForwardRef("H5"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": ForwardRef("H6"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ForwardRef("P"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": ForwardRef("Address"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    max_choices: int = field(
        default=1,
        metadata={
            "name": "max-choices",
            "type": "Attribute",
        },
    )
    min_choices: int = field(
        default=0,
        metadata={
            "name": "min-choices",
            "type": "Attribute",
        },
    )
    data_min_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-min-selections-message",
            "type": "Attribute",
        },
    )
    data_max_selections_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-max-selections-message",
            "type": "Attribute",
        },
    )


@dataclass
class InteractionMarkupDtype:
    """
    This is the container for the HTML-based markup that is to be used in the
    associated PCI [PCI, 20].
    """

    class Meta:
        name = "InteractionMarkupDType"

    choice: List[
        Union[
            PrintedVariableDtype,
            FeedbackBlockDtype,
            FeedbackInlineDtype,
            "TemplateInlineDtype",
            "TemplateBlockDtype",
            Math,
            Include,
            Pre,
            H1,
            H2,
            H3,
            H4,
            H5,
            H6,
            P,
            Address,
            Dl,
            "Ol",
            "Ul",
            Br,
            Hr,
            Img,
            "Object",
            Blockquote,
            Em,
            A,
            Code,
            Span,
            Sub,
            Acronym,
            Big,
            Tt,
            Kbd,
            "Q",
            I,
            Dfn,
            Abbr,
            Strong,
            Sup,
            Var,
            Small,
            Samp,
            B,
            Cite,
            "Table",
            Div,
            Bdo,
            Bdi,
            Figure,
            ImsglobalXsdImsqtiasiV3P0AudioAudio,
            Video,
            Article,
            Aside,
            Footer,
            Header,
            Label,
            Nav,
            Section,
            "Ruby",
            ParagraphP,
            S,
            SayAs,
            Phoneme,
            SubSub,
            Voice,
            Emphasis,
            Break,
            Prosody,
            Mark,
            W3Pkg2001Pkg10SynthesisParagraphAudio,
            Speak,
            Picture,
            Details,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-block",
                    "type": FeedbackBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": ForwardRef("TemplateBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": Details,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    template: List[Template] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )


@dataclass
class PortableCustomInteractionDtype(BasePromptInteractionDtype):
    """This container enables the placement of PCIs in the assessment activity.

    The supplied inf- ormation enables the launch and collection of
    state information from the actual PCI as de- fined by the PCI
    specification [PCI, 20]. PCIs MUST be used instead of custom
    interactions (the latter have been deprecated).
    """

    class Meta:
        name = "PortableCustomInteractionDType"

    qti_interaction_modules: Optional[InteractionModulesDtype] = field(
        default=None,
        metadata={
            "name": "qti-interaction-modules",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_interaction_markup: Optional[InteractionMarkupDtype] = field(
        default=None,
        metadata={
            "name": "qti-interaction-markup",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
    qti_template_variable: List[TemplateUniqueIdrefDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-template-variable",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_context_variable: List[ContextUniqueIdrefDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-context-variable",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    custom_interaction_type_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "custom-interaction-type-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    module: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Lidtype(BaseSequenceDtype):
    """Provides the HTML 'li' tag functionality.

    The 'li' tag represents a list item. If its par- ent tag is an 'ol'
    or 'ul', then the tag is an item of the parent tag's list, as
    defined for those elements. Otherwise, the list item has no defined
    list-related relationship to any other 'li' tag. If the parent
    element is an 'ol' tag, then the 'li' tag has an ordinal value.
    """

    class Meta:
        name = "LIDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-block",
                    "type": FeedbackBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext",
                    "type": HotTextDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": ForwardRef("TemplateBlockDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-text-entry-interaction",
                    "type": TextEntryInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inline-choice-interaction",
                    "type": InlineChoiceInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-end-attempt-interaction",
                    "type": EndAttemptInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-interaction",
                    "type": CustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-portable-custom-interaction",
                    "type": PortableCustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-drawing-interaction",
                    "type": DrawingInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap-match-interaction",
                    "type": GapMatchInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match-interaction",
                    "type": ForwardRef("MatchInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-gap-match-interaction",
                    "type": GraphicGapMatchInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hotspot-interaction",
                    "type": HotspotInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-order-interaction",
                    "type": GraphicOrderInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-select-point-interaction",
                    "type": ForwardRef("SelectPointInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-associate-interaction",
                    "type": GraphicAssociateInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-slider-interaction",
                    "type": SliderInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-choice-interaction",
                    "type": ChoiceInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-media-interaction",
                    "type": ForwardRef("MediaInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext-interaction",
                    "type": HotTextInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-order-interaction",
                    "type": ForwardRef("OrderInteractionDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-extended-text-interaction",
                    "type": ExtendedTextInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-upload-interaction",
                    "type": UploadInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-associate-interaction",
                    "type": AssociateInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": Details,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class Li(Lidtype):
    class Meta:
        name = "li"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Ouldtype(BaseSequenceXbaseDtype):
    """Provides the HTML 'ol' and 'ul' tag functionalities.

    These provide the ordered and unorde- red list capability. The 'ol'
    tag represents a list of items, where the items have been i-
    ntentionally ordered, such that changing the order would change the
    meaning of the docume- nt. The 'ul' tags have no expicit order
    relationship. The items of the list are the 'li' child nodes.
    """

    class Meta:
        name = "OULDType"

    li: List[Li] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )


@dataclass
class Ol(Ouldtype):
    class Meta:
        name = "ol"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Ul(Ouldtype):
    class Meta:
        name = "ul"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ObjectDtype(BaseSequenceXbaseDtype):
    """
    This is the representation for the HTML 'object' tag.
    """

    class Meta:
        name = "ObjectDType"

    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "pattern": r'[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+/[\p{IsBasicLatin}-[()<>@,;:\\"/\[\]?=]]+',
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]+%?",
        },
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]+%?",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "param",
                    "type": ParamDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": Ol,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": ForwardRef("Object"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": Details,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class Object(ObjectDtype):
    class Meta:
        name = "object"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class PositionObjectInteractionDtype(BaseSequenceRidentDtype):
    """The position object interaction consists of a single image which must be
    positioned on an- other graphic image (the stage) by the candidate.

    Like selectPointInteraction, the associ- ated response may have an
    areaMapping that scores the response on the basis of comparing it
    against predefined areas but the delivery engine must not indicate
    these areas of the stage. Only the actual position(s) selected by
    the candidate shall be indicated. The posi- tion object interaction
    must be bound to a response variable with a base-type of point and
    single or multiple cardinality. The point records the coordinates,
    with respect to the st- age, of the centre point of the image being
    positioned.
    """

    class Meta:
        name = "PositionObjectInteractionDType"

    object_or_img_or_picture: Optional[Union[Object, Img, Picture]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    center_point: List[int] = field(
        default_factory=list,
        metadata={
            "name": "center-point",
            "type": "Attribute",
            "tokens": True,
        },
    )
    min_choices: Optional[int] = field(
        default=None,
        metadata={
            "name": "min-choices",
            "type": "Attribute",
        },
    )
    max_choices: int = field(
        default=1,
        metadata={
            "name": "max-choices",
            "type": "Attribute",
        },
    )


@dataclass
class Qdtype(BaseSequenceXbaseDtype):
    """This provides the content definition for the HTML 'q' tag.

    The q element represents some phrasing content quoted from another
    source. Quotation punctuation (such as quotation mar- ks) that is
    quoting the contents of the tag must not appear immediately before,
    after, or inside q tags; they will be inserted into the rendering by
    the user agent. Content inside a 'q' tag must be quoted from another
    source, whose address, if it has one, may be cited in the cite
    attribute. The source may be fictional, as when quoting characters
    in a novel or screenplay.  The 'q' tag must not be used in place of
    quotation marks that do not repr- esent quotes; for example, it is
    inappropriate to use the q element for marking up sarcas- tic
    statements. The use of 'q' tags to mark up quotations is entirely
    optional; using exp- licit quotation punctuation without 'q' tags is
    just as correct.
    """

    class Meta:
        name = "QDType"

    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-text-entry-interaction",
                    "type": TextEntryInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext",
                    "type": HotTextDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap",
                    "type": GapDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inline-choice-interaction",
                    "type": InlineChoiceInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-end-attempt-interaction",
                    "type": EndAttemptInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-interaction",
                    "type": CustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class SelectPointInteractionDtype(BasePromptInteractionDtype):
    """Like hotspotInteraction, a select point interaction is a graphic
    interaction.

    The candida- te's task is to select one or more points. The
    associated response may have an areaMapping that scores the response
    on the basis of comparing it against predefined areas but the de-
    livery engine must not indicate these areas of the image. Only the
    actual point(s) select- ed by the candidate shall be indicated. The
    select point interaction must be bound to a r- esponse variable with
    a base-type of point and single or multiple cardinality.
    """

    class Meta:
        name = "SelectPointInteractionDType"

    object_or_img_or_picture: Optional[Union[Object, Img, Picture]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    min_choices: int = field(
        default=0,
        metadata={
            "name": "min-choices",
            "type": "Attribute",
        },
    )
    max_choices: int = field(
        default=0,
        metadata={
            "name": "max-choices",
            "type": "Attribute",
        },
    )


@dataclass
class PositionObjectStageDtype:
    """
    This is the content frame for the positionObjectInteraction(s).
    """

    class Meta:
        name = "PositionObjectStageDType"

    object_or_img_or_picture: Optional[Union[Object, Img, Picture]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    qti_position_object_interaction: List[PositionObjectInteractionDtype] = (
        field(
            default_factory=list,
            metadata={
                "name": "qti-position-object-interaction",
                "type": "Element",
                "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                "min_occurs": 1,
            },
        )
    )
    id: Optional[str] = field(
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


@dataclass
class Q(Qdtype):
    class Meta:
        name = "q"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Rtcdtype(BaseSequenceDtype):
    """This feature is a part of the HTML5 Ruby annotation.

    The 'rtc' tag marks a ruby text cont- ainer for ruby text components
    in a ruby annotation. When it is the child of a ruby tag it doesn't
    represent anything itself, but its parent ruby tag uses it as part
    of determining what it represents. An rtc tag that is not a child of
    a ruby tag represents the same thing as its children.
    """

    class Meta:
        name = "RTCDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "rt",
                    "type": Rt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class Rtc(Rtcdtype):
    class Meta:
        name = "rtc"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class RubyDtype(BaseSequenceDtype):
    """This feature is a part of the HTML5 Ruby annotation.

    The ruby tag allows one or more spans of phrasing content to be
    marked with ruby annotations. Ruby annotations are short runs of
    text presented alongside base text, primarily used in East Asian
    typography as a guide for pronunciation or to include other
    annotations. In Japanese, this form of typography is al- so known as
    furigana. Ruby text can appear on either side, and sometimes both
    sides, of t- he base text, and it is possible to control its
    position using CSS.
    """

    class Meta:
        name = "RubyDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "rb",
                    "type": Rb,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "rp",
                    "type": Rp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "rt",
                    "type": Rt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "rtc",
                    "type": Rtc,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class Ruby(RubyDtype):
    class Meta:
        name = "ruby"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class HtmlcontentDtype:
    """
    The container for the content in HTML format.
    """

    class Meta:
        name = "HTMLContentDType"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": Ol,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": Table,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": Details,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class PromptDtype(BaseSequenceDtype):
    """This enables an author to define the prompt for the question.

    The way in which the prompt is displayed depends upon the rendering
    system. The prompt should not be used to contain the actual root of
    the question.
    """

    class Meta:
        name = "PromptDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": Ol,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": Table,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": Details,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class TemplateInlineDtype(BaseSequenceXbaseDtype):
    """This enables the Inline content to be placed in templates.

    This structure is used to add constraints on how the inline content
    can be used in recursive templates.
    """

    class Meta:
        name = "TemplateInlineDType"

    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    show_hide: TemplateInlineDtypeShowHide = field(
        default=TemplateInlineDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-hottext",
                    "type": HotTextDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap",
                    "type": GapDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": ForwardRef("TemplateInlineDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class CardEntryDtype:
    """A content container within a catalog card.

    Each instance of a CardEntry provides a differ- ent resource where
    an attribute (often custom attributes) on the CardEntry element
    declar- es the difference between the resources, and where the
    attribute value aligns with a spec- ific preference/need from the
    candidate's PNP (or an assessment program's settings). For example,
    there could be multiple CardEntry nodes for different language
    versions for a pa- rticular support.
    """

    class Meta:
        name = "CardEntryDType"

    qti_html_content: Optional[HtmlcontentDtype] = field(
        default=None,
        metadata={
            "name": "qti-html-content",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_file_href: List[FileHrefCardDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-file-href",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    default: bool = field(
        default=False,
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


@dataclass
class Dtdtype(BaseSequenceXbaseDtype):
    """The 'dt' tag is a part of the HTML content.

    The 'dt' tag represents the term, or name, pa- rt of a term-
    description group in a description list (dl element).
    """

    class Meta:
        name = "DTDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-text-entry-interaction",
                    "type": TextEntryInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext",
                    "type": HotTextDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap",
                    "type": GapDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": TemplateInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inline-choice-interaction",
                    "type": InlineChoiceInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-end-attempt-interaction",
                    "type": EndAttemptInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-interaction",
                    "type": CustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class FeedbackContentBodyDtype:
    """This is the container for the HTML-based content to be presented as part of
    the feedback process in Items (excluding modal feedback and inline feedback).

    This wrapper was added as part of the QTI 3.0 revision.
    """

    class Meta:
        name = "FeedbackContentBodyDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-position-object-stage",
                    "type": PositionObjectStageDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-interaction",
                    "type": CustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-portable-custom-interaction",
                    "type": PortableCustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-drawing-interaction",
                    "type": DrawingInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap-match-interaction",
                    "type": GapMatchInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match-interaction",
                    "type": MatchInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-gap-match-interaction",
                    "type": GraphicGapMatchInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hotspot-interaction",
                    "type": HotspotInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-order-interaction",
                    "type": GraphicOrderInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-select-point-interaction",
                    "type": SelectPointInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-associate-interaction",
                    "type": GraphicAssociateInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-slider-interaction",
                    "type": SliderInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-choice-interaction",
                    "type": ChoiceInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-media-interaction",
                    "type": MediaInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext-interaction",
                    "type": HotTextInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-order-interaction",
                    "type": OrderInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-extended-text-interaction",
                    "type": ExtendedTextInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-upload-interaction",
                    "type": UploadInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-associate-interaction",
                    "type": AssociateInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-block",
                    "type": FeedbackBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": TemplateBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": Ol,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": Table,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "qti-template-inline",
                    "type": TemplateInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class LabelDtype(BaseSequenceXbaseDtype):
    """This allows the creation of human readable labels that will be placed close
    to the associ- ated displayed content artefacts.

    These labels are used with inline choice interactions.
    """

    class Meta:
        name = "LabelDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": TemplateInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class SimpleAssociableChoiceDtype(BaseSequenceDtype):
    """
    This is an ordered set of choices for the set.
    """

    class Meta:
        name = "SimpleAssociableChoiceDType"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    fixed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
        },
    )
    show_hide: Optional[SimpleAssociableChoiceDtypeShowHide] = field(
        default=None,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    match_group: List[str] = field(
        default_factory=list,
        metadata={
            "name": "match-group",
            "type": "Attribute",
            "tokens": True,
        },
    )
    match_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "match-max",
            "type": "Attribute",
            "required": True,
        },
    )
    match_min: int = field(
        default=0,
        metadata={
            "name": "match-min",
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-block",
                    "type": FeedbackBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": TemplateInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": TemplateBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": Ol,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": Table,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": Details,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class SimpleChoiceDtype(BaseSequenceDtype):
    """A simpleChoice is a choice that contains flowStatic objects.

    A simpleChoice must not cont- ain any nested interactions.
    """

    class Meta:
        name = "SimpleChoiceDType"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    fixed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
        },
    )
    show_hide: SimpleChoiceDtypeShowHide = field(
        default=SimpleChoiceDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-block",
                    "type": FeedbackBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": TemplateInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": TemplateBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": Ol,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": Table,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": Details,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class Tdhdtype(BaseSequenceDtype):
    """
    This class allows the defnition of the contents of the HTML 'td' and 'th' tags
    i.e. the t- able cells used within the table rows.
    """

    class Meta:
        name = "TDHDType"

    headers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: Optional[TdhdtypeScope] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rowspan: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    colspan: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[TdhdtypeAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: Optional[TdhdtypeValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-block",
                    "type": FeedbackBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext",
                    "type": HotTextDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": TemplateInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-block",
                    "type": TemplateBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-text-entry-interaction",
                    "type": TextEntryInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inline-choice-interaction",
                    "type": InlineChoiceInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-end-attempt-interaction",
                    "type": EndAttemptInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-interaction",
                    "type": CustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-portable-custom-interaction",
                    "type": PortableCustomInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-drawing-interaction",
                    "type": DrawingInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gap-match-interaction",
                    "type": GapMatchInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match-interaction",
                    "type": MatchInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-gap-match-interaction",
                    "type": GraphicGapMatchInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hotspot-interaction",
                    "type": HotspotInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-order-interaction",
                    "type": GraphicOrderInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-select-point-interaction",
                    "type": SelectPointInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-graphic-associate-interaction",
                    "type": GraphicAssociateInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-slider-interaction",
                    "type": SliderInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-choice-interaction",
                    "type": ChoiceInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-media-interaction",
                    "type": MediaInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-hottext-interaction",
                    "type": HotTextInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-order-interaction",
                    "type": OrderInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-extended-text-interaction",
                    "type": ExtendedTextInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-upload-interaction",
                    "type": UploadInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-associate-interaction",
                    "type": AssociateInteractionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": Ol,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": Table,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": Details,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class TemplateBlockContentBodyDtype:
    """
    This is the container for all of the content to be presented in the template
    block includ- ing all of the HTML-based content.
    """

    class Meta:
        name = "TemplateBlockContentBodyDType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": Ol,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "object",
                    "type": Object,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": Table,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "bdi",
                    "type": Bdi,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": ImsglobalXsdImsqtiasiV3P0AudioAudio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "label",
                    "type": Label,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": ParagraphP,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": SubSub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": W3Pkg2001Pkg10SynthesisParagraphAudio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "speak",
                    "type": Speak,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "picture",
                    "type": Picture,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "details",
                    "type": Details,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-template-block",
                    "type": TemplateBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-inline",
                    "type": TemplateInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-block",
                    "type": TemplateBlockFeedbackBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-feedback-inline",
                    "type": FeedbackInlineDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class SimpleMatchSetDtype:
    """
    This is the ordered set of choices for the match set.
    """

    class Meta:
        name = "SimpleMatchSetDType"

    qti_simple_associable_choice: List[SimpleAssociableChoiceDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-simple-associable-choice",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    id: Optional[str] = field(
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


@dataclass
class Dt(Dtdtype):
    class Meta:
        name = "dt"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Td(Tdhdtype):
    class Meta:
        name = "td"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Th(Tdhdtype):
    class Meta:
        name = "th"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Trdtype(BaseSequenceDtype):
    """
    This makes the HTML tag 'tr' available for the definition of tables.
    """

    class Meta:
        name = "TRDType"

    td_or_th: List[Union[Td, Th]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "td",
                    "type": Td,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "th",
                    "type": Th,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass
class Tr(Trdtype):
    class Meta:
        name = "tr"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class TablePartDtype(BaseSequenceDtype):
    """
    This allows the construction of the internal structures in the HTML Table tag,
    namely: the head, foot and body of the table.
    """

    class Meta:
        name = "TablePartDType"

    tr: List[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )


@dataclass
class Tbody(TablePartDtype):
    class Meta:
        name = "tbody"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Tfoot(TablePartDtype):
    class Meta:
        name = "tfoot"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class Thead(TablePartDtype):
    class Meta:
        name = "thead"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
