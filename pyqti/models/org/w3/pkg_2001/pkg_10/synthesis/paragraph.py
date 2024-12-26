from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict, ForwardRef, List, Optional, Union
from xml.etree.ElementTree import QName

from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.break_mod import Break
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.desc import Desc
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.gender_datatype import (
    GenderDatatype,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.height_scale import (
    HeightScale,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.level_datatype import (
    LevelDatatype,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.mark import Mark
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.phoneme import Phoneme
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.say_as import SayAs
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.speed_scale import (
    SpeedScale,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.sub import Sub
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.volume_scale import (
    VolumeScale,
)
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass
class Paragraph:
    class Meta:
        name = "paragraph"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    onlangfailure: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"changevoice|ignoretext|ignorelang|processorchoice",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
                    "name": "lang",
                    "type": ForwardRef("Lang"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "w",
                    "type": ForwardRef("W"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "token",
                    "type": ForwardRef("Token"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": ForwardRef("Emphasis"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": ForwardRef("Audio"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": ForwardRef("Prosody"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": ForwardRef("Voice"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": ForwardRef("S"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "lookup",
                    "type": ForwardRef("Lookup"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class Sentence:
    class Meta:
        name = "sentence"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    onlangfailure: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"changevoice|ignoretext|ignorelang|processorchoice",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
                    "name": "lang",
                    "type": ForwardRef("Lang"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "w",
                    "type": ForwardRef("W"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "token",
                    "type": ForwardRef("Token"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": ForwardRef("Emphasis"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "audio",
                    "type": ForwardRef("Audio"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": ForwardRef("Prosody"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": ForwardRef("Voice"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "lookup",
                    "type": ForwardRef("Lookup"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class TokenType:
    class Meta:
        name = "tokenType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    onlangfailure: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"changevoice|ignoretext|ignorelang|processorchoice",
        },
    )
    role: List[QName] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
                    "name": "audio",
                    "type": ForwardRef("Audio"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": ForwardRef("Emphasis"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": ForwardRef("Prosody"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": ForwardRef("Voice"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class P(Paragraph):
    class Meta:
        name = "p"
        namespace = "http://www.w3.org/2001/10/synthesis"


@dataclass
class S(Sentence):
    class Meta:
        name = "s"
        namespace = "http://www.w3.org/2001/10/synthesis"


@dataclass
class Token(TokenType):
    class Meta:
        name = "token"
        namespace = "http://www.w3.org/2001/10/synthesis"


@dataclass
class W(TokenType):
    class Meta:
        name = "w"
        namespace = "http://www.w3.org/2001/10/synthesis"


@dataclass
class Voice:
    class Meta:
        name = "voice"
        namespace = "http://www.w3.org/2001/10/synthesis"

    gender: Optional[GenderDatatype] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    age: Optional[Union[int, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 0,
        },
    )
    variant: Optional[Union[int, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 0,
        },
    )
    name: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "max_length": 0,
            "pattern": r"\S+",
            "tokens": True,
        },
    )
    languages: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "max_length": 0,
            "tokens": True,
        },
    )
    required: List[str] = field(
        default_factory=lambda: [
            "languages",
        ],
        metadata={
            "type": "Attribute",
            "max_length": 0,
            "pattern": r"name|languages|gender|age|variant",
            "tokens": True,
        },
    )
    ordering: List[str] = field(
        default_factory=lambda: [
            "languages",
        ],
        metadata={
            "type": "Attribute",
            "max_length": 0,
            "pattern": r"name|languages|gender|age|variant",
            "tokens": True,
        },
    )
    onvoicefailure: str = field(
        default="priorityselect",
        metadata={
            "type": "Attribute",
            "pattern": r"priorityselect|keepexisting|processorchoice",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
                    "name": "lang",
                    "type": ForwardRef("Lang"),
                },
                {
                    "name": "w",
                    "type": W,
                },
                {
                    "name": "token",
                    "type": Token,
                },
                {
                    "name": "mark",
                    "type": Mark,
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "emphasis",
                    "type": ForwardRef("Emphasis"),
                },
                {
                    "name": "audio",
                    "type": ForwardRef("Audio"),
                },
                {
                    "name": "prosody",
                    "type": ForwardRef("Prosody"),
                },
                {
                    "name": "voice",
                    "type": ForwardRef("Voice"),
                },
                {
                    "name": "s",
                    "type": S,
                },
                {
                    "name": "p",
                    "type": P,
                },
                {
                    "name": "lookup",
                    "type": ForwardRef("Lookup"),
                },
            ),
        },
    )


@dataclass
class Prosody:
    class Meta:
        name = "prosody"
        namespace = "http://www.w3.org/2001/10/synthesis"

    pitch: Optional[Union[str, HeightScale]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)Hz",
        },
    )
    contour: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "pattern": r"\(([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)%,(([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)Hz|[+\-]([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)Hz|[+\-]?([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)%|[+\-]([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)st|x-high|high|medium|low|x-low|default)\)",
            "tokens": True,
        },
    )
    range: Optional[Union[str, HeightScale]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)Hz",
        },
    )
    rate: Optional[Union[Decimal, str, SpeedScale]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": Decimal("0"),
            "pattern": r"([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)%",
        },
    )
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\+)?([0-9]*\.)?[0-9]+(ms|s)",
        },
    )
    volume: Union[str, VolumeScale] = field(
        default="+0.0dB",
        metadata={
            "type": "Attribute",
            "pattern": r"(\+|-)?([0-9]*\.)?[0-9]+dB",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
                    "name": "lang",
                    "type": ForwardRef("Lang"),
                },
                {
                    "name": "w",
                    "type": W,
                },
                {
                    "name": "token",
                    "type": Token,
                },
                {
                    "name": "mark",
                    "type": Mark,
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "emphasis",
                    "type": ForwardRef("Emphasis"),
                },
                {
                    "name": "audio",
                    "type": ForwardRef("Audio"),
                },
                {
                    "name": "prosody",
                    "type": ForwardRef("Prosody"),
                },
                {
                    "name": "voice",
                    "type": Voice,
                },
                {
                    "name": "s",
                    "type": S,
                },
                {
                    "name": "p",
                    "type": P,
                },
                {
                    "name": "lookup",
                    "type": ForwardRef("Lookup"),
                },
            ),
        },
    )


@dataclass
class Audio:
    class Meta:
        name = "audio"
        namespace = "http://www.w3.org/2001/10/synthesis"

    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fetchtimeout: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\+)?([0-9]*\.)?[0-9]+(ms|s)",
        },
    )
    fetchhint: str = field(
        default="prefetch",
        metadata={
            "type": "Attribute",
            "pattern": r"safe|prefetch",
        },
    )
    maxage: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maxstale: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
                    "name": "lang",
                    "type": ForwardRef("Lang"),
                },
                {
                    "name": "w",
                    "type": W,
                },
                {
                    "name": "token",
                    "type": Token,
                },
                {
                    "name": "mark",
                    "type": Mark,
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "emphasis",
                    "type": ForwardRef("Emphasis"),
                },
                {
                    "name": "audio",
                    "type": ForwardRef("Audio"),
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                },
                {
                    "name": "voice",
                    "type": Voice,
                },
                {
                    "name": "s",
                    "type": S,
                },
                {
                    "name": "p",
                    "type": P,
                },
                {
                    "name": "lookup",
                    "type": ForwardRef("Lookup"),
                },
                {
                    "name": "desc",
                    "type": Desc,
                },
            ),
        },
    )


@dataclass
class Emphasis:
    class Meta:
        name = "emphasis"
        namespace = "http://www.w3.org/2001/10/synthesis"

    level: LevelDatatype = field(
        default=LevelDatatype.MODERATE,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
                    "name": "lang",
                    "type": ForwardRef("Lang"),
                },
                {
                    "name": "w",
                    "type": W,
                },
                {
                    "name": "token",
                    "type": Token,
                },
                {
                    "name": "mark",
                    "type": Mark,
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "emphasis",
                    "type": ForwardRef("Emphasis"),
                },
                {
                    "name": "audio",
                    "type": Audio,
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                },
                {
                    "name": "voice",
                    "type": Voice,
                },
                {
                    "name": "lookup",
                    "type": ForwardRef("Lookup"),
                },
            ),
        },
    )


@dataclass
class LookupType:
    class Meta:
        name = "lookupType"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
                    "name": "audio",
                    "type": Audio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "lang",
                    "type": ForwardRef("Lang"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "lookup",
                    "type": ForwardRef("Lookup"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "token",
                    "type": Token,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "w",
                    "type": W,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class Lookup(LookupType):
    class Meta:
        name = "lookup"
        namespace = "http://www.w3.org/2001/10/synthesis"


@dataclass
class LangType:
    class Meta:
        name = "langType"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    onlangfailure: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"changevoice|ignoretext|ignorelang|processorchoice",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
                    "name": "audio",
                    "type": Audio,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "break",
                    "type": Break,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "lang",
                    "type": ForwardRef("Lang"),
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "lookup",
                    "type": Lookup,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "mark",
                    "type": Mark,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "phoneme",
                    "type": Phoneme,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "prosody",
                    "type": Prosody,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "say-as",
                    "type": SayAs,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "token",
                    "type": Token,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "voice",
                    "type": Voice,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
                {
                    "name": "w",
                    "type": W,
                    "namespace": "http://www.w3.org/2001/10/synthesis",
                },
            ),
        },
    )


@dataclass
class Lang(LangType):
    class Meta:
        name = "lang"
        namespace = "http://www.w3.org/2001/10/synthesis"
