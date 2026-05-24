from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    A,
    Abbr,
    Acronym,
    Address,
    Article,
    Aside,
    B,
    Bdi,
    Bdo,
    Big,
    Blockquote,
    Cite,
    Code,
    Details,
    Dfn,
    Div,
    Dl,
    Em,
    Figure,
    Footer,
    Header,
    HotTextDtype,
    I,
    Kbd,
    Label,
    Nav,
    Object,
    Ol,
    Pre,
    Q,
    Ruby,
    Samp,
    Section,
    Small,
    Span,
    Strong,
    Sup,
    Table,
    TemplateBlockDtype,
    TemplateInlineDtype,
    Tt,
    Ul,
    Var,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    P as ImsglobalXsdImsqtiasiV3P0AdtypeP,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    Sub as ImsglobalXsdImsqtiasiV3P0AdtypeSub,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.audio import (
    Audio as ImsglobalXsdImsqtiasiV3P0AudioAudio,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.br import Br
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.hr import Hr
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.img import Img
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.picture import Picture
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.printed_variable_dtype import (
    PrintedVariableDtype,
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
    P as W3Pkg2001Pkg10SynthesisParagraphP,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.phoneme import Phoneme
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.say_as import SayAs
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.speak import Speak
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.sub import (
    Sub as W3Pkg2001Pkg10SynthesisSubSub,
)
from pyqti.models.org.w3.pkg_2001.xinclude.include_type import Include

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class FeedbackFlowContentBodyDtype:
    """
    This is the container for the HTML-based content to be presented as
    part of the feedback process in Items (modal feedback mode only).

    This wrapper was added as part of the QTI 3.0 revision.
    """

    class Meta:
        name = "FeedbackFlowContentBodyDType"

    content: list[object] = field(
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
                    "name": "qti-hottext",
                    "type": HotTextDtype,
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
                    "type": ImsglobalXsdImsqtiasiV3P0AdtypeP,
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
                    "type": ImsglobalXsdImsqtiasiV3P0AdtypeSub,
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
                    "type": W3Pkg2001Pkg10SynthesisParagraphP,
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
                    "type": W3Pkg2001Pkg10SynthesisSubSub,
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
