from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef
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


@dataclass(kw_only=True)
class Paragraph:
    class Meta:
        name = "paragraph"

    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    onlangfailure: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"changevoice|ignoretext|ignorelang|processorchoice",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
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


@dataclass(kw_only=True)
class Sentence:
    class Meta:
        name = "sentence"

    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    onlangfailure: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"changevoice|ignoretext|ignorelang|processorchoice",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
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


@dataclass(kw_only=True)
class TokenType:
    class Meta:
        name = "tokenType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    onlangfailure: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"changevoice|ignoretext|ignorelang|processorchoice",
        },
    )
    role: list[QName] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
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


@dataclass(kw_only=True)
class P(Paragraph):
    class Meta:
        name = "p"
        namespace = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class S(Sentence):
    class Meta:
        name = "s"
        namespace = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class Token(TokenType):
    class Meta:
        name = "token"
        namespace = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class W(TokenType):
    class Meta:
        name = "w"
        namespace = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class Voice:
    class Meta:
        name = "voice"
        namespace = "http://www.w3.org/2001/10/synthesis"

    gender: None | GenderDatatype = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    age: None | int | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 0,
        },
    )
    variant: None | int | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 0,
        },
    )
    name: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "max_length": 0,
            "pattern": r"\S+",
            "tokens": True,
        },
    )
    languages: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "max_length": 0,
            "tokens": True,
        },
    )
    required: list[str] = field(
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
    ordering: list[str] = field(
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
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
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


@dataclass(kw_only=True)
class Prosody:
    class Meta:
        name = "prosody"
        namespace = "http://www.w3.org/2001/10/synthesis"

    pitch: None | str | HeightScale = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)Hz",
        },
    )
    contour: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "pattern": r"\(([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)%,(([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)Hz|[+\-]([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)Hz|[+\-]?([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)%|[+\-]([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)st|x-high|high|medium|low|x-low|default)\)",
            "tokens": True,
        },
    )
    range: None | str | HeightScale = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)Hz",
        },
    )
    rate: None | Decimal | str | SpeedScale = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": Decimal("0"),
            "pattern": r"([0-9]+|[0-9]+.[0-9]*|[0-9]*.[0-9]+)%",
        },
    )
    duration: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\+)?([0-9]*\.)?[0-9]+(ms|s)",
        },
    )
    volume: str | VolumeScale = field(
        default="+0.0dB",
        metadata={
            "type": "Attribute",
            "pattern": r"(\+|-)?([0-9]*\.)?[0-9]+dB",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
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


@dataclass(kw_only=True)
class Audio:
    class Meta:
        name = "audio"
        namespace = "http://www.w3.org/2001/10/synthesis"

    src: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fetchtimeout: None | str = field(
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
    maxage: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maxstale: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
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


@dataclass(kw_only=True)
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
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
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


@dataclass(kw_only=True)
class LookupType:
    class Meta:
        name = "lookupType"

    ref: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
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


@dataclass(kw_only=True)
class Lookup(LookupType):
    class Meta:
        name = "lookup"
        namespace = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class LangType:
    class Meta:
        name = "langType"

    lang: str | LangValue = field(
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    onlangfailure: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"changevoice|ignoretext|ignorelang|processorchoice",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
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


@dataclass(kw_only=True)
class Lang(LangType):
    class Meta:
        name = "lang"
        namespace = "http://www.w3.org/2001/10/synthesis"
