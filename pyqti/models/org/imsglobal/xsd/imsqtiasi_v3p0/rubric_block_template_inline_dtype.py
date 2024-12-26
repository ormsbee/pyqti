from dataclasses import dataclass, field
from typing import List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    A,
    Abbr,
    Acronym,
    B,
    Bdi,
    Bdo,
    Big,
    Cite,
    Code,
    Dfn,
    Em,
    I,
    Kbd,
    Label,
    Object,
    Q,
    Ruby,
    Samp,
    Small,
    Span,
    Strong,
    Sup,
    Tt,
    Var,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    Sub as ImsglobalXsdImsqtiasiV3P0AdtypeSub,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_dtype import (
    BaseSequenceXbaseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.br import Br
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.img import Img
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.picture import Picture
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.printed_variable_dtype import (
    PrintedVariableDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.rubric_block_template_inline_dtype_show_hide import (
    RubricBlockTemplateInlineDtypeShowHide,
)
from pyqti.models.org.w3.pkg_1998.math.math_ml.math import Math
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.break_mod import Break
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.mark import Mark
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.paragraph import (
    Audio,
    Emphasis,
    P,
    Prosody,
    S,
    Voice,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.phoneme import Phoneme
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.say_as import SayAs
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.speak import Speak
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.sub import (
    Sub as W3Pkg2001Pkg10SynthesisSubSub,
)
from pyqti.models.org.w3.pkg_2001.xinclude.include_type import Include

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class RubricBlockTemplateInlineDtype(BaseSequenceXbaseDtype):
    """
    This is the container for the rubric content that is used in the context of a
    template in- line content.
    """

    class Meta:
        name = "RubricBlockTemplateInlineDType"

    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    show_hide: RubricBlockTemplateInlineDtypeShowHide = field(
        default=RubricBlockTemplateInlineDtypeShowHide.SHOW,
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
                    "type": P,
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
                    "type": Audio,
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
                    "name": "qti-printed-variable",
                    "type": PrintedVariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
