from dataclasses import dataclass, field
from typing import List, Optional, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    Address,
    Article,
    Aside,
    AssociateInteractionDtype,
    Blockquote,
    ChoiceInteractionDtype,
    Div,
    Dl,
    DrawingInteractionDtype,
    ExtendedTextInteractionDtype,
    FeedbackBlockDtype,
    Figure,
    Footer,
    GapMatchInteractionDtype,
    GraphicAssociateInteractionDtype,
    GraphicGapMatchInteractionDtype,
    GraphicOrderInteractionDtype,
    Header,
    HotspotInteractionDtype,
    HotTextInteractionDtype,
    MatchInteractionDtype,
    MediaInteractionDtype,
    Nav,
    Ol,
    OrderInteractionDtype,
    P,
    PortableCustomInteractionDtype,
    PositionObjectStageDtype,
    Pre,
    Section,
    SelectPointInteractionDtype,
    SliderInteractionDtype,
    Table,
    TemplateBlockDtype,
    Ul,
    UploadInteractionDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.audio import Audio
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.custom_interaction_dtype import (
    CustomInteractionDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.hr import Hr
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.item_body_dtype_dir import (
    ItemBodyDtypeDir,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.rubric_block_dtype import (
    RubricBlockDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.video import Video
from pyqti.models.org.w3.pkg_1998.math.math_ml.math import Math
from pyqti.models.org.w3.pkg_2001.xinclude.include_type import Include
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ItemBodyDtype:
    """The item body contains the text, graphics, media objects and interactions
    that describe t- he item's content and information about how it is structured.

    The body is presented by co- mbining it with stylesheet information,
    either explicitly or implicitly using the default style rules of the
    delivery or authoring system. The body must be presented to the
    candid- ate when the associated item session is in the interacting
    state. In this state, the cand- idate must be able to interact with
    each of the visible interactions and therefore set or update the
    values of the associated response variables. The body may be
    presented to the candidate when the item session is in the closed or
    review state. In these states, althou- gh the candidate's responses
    should be visible, the interactions must be disabled so as to
    prevent the candidate from setting or updating the values of the
    associated response vari- ables. Finally, the body may be presented
    to the candidate in the solution state, in which case the correct
    values of the response variables must be visible and the associated
    inte- ractions disabled. The content model employed by this
    specification uses many concepts ta- ken directly from [XHTML, 10].
    In effect, this part of the specification defines a profile of
    XHTML. Only some of the elements defined in XHTML are allowable in
    an assessmentItem a- nd of those that are, some have additional
    constraints placed on their attributes. Only t- hose elements from
    XHTML that are explicitly defined within this specification can be
    use- d. See XHTML Elements for details. Finally, this specification
    defines some new elements which are used to represent the
    interactions and to control the display of Integrated Fee- dback and
    content restricted to one or more of the defined content views.
    """

    class Meta:
        name = "ItemBodyDType"

    choice: List[
        Union[
            RubricBlockDtype,
            PositionObjectStageDtype,
            CustomInteractionDtype,
            PortableCustomInteractionDtype,
            DrawingInteractionDtype,
            GapMatchInteractionDtype,
            MatchInteractionDtype,
            GraphicGapMatchInteractionDtype,
            HotspotInteractionDtype,
            GraphicOrderInteractionDtype,
            SelectPointInteractionDtype,
            GraphicAssociateInteractionDtype,
            SliderInteractionDtype,
            ChoiceInteractionDtype,
            MediaInteractionDtype,
            HotTextInteractionDtype,
            OrderInteractionDtype,
            ExtendedTextInteractionDtype,
            UploadInteractionDtype,
            AssociateInteractionDtype,
            FeedbackBlockDtype,
            TemplateBlockDtype,
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
            Ol,
            Ul,
            Hr,
            Blockquote,
            Table,
            Div,
            Article,
            Aside,
            Audio,
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
                    "name": "qti-rubric-block",
                    "type": RubricBlockDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
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
                    "type": Audio,
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
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
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
    dir: ItemBodyDtypeDir = field(
        default=ItemBodyDtypeDir.AUTO,
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
