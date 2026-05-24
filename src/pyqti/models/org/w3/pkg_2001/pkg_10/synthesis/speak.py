from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.break_mod import Break
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.mark import Mark
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.paragraph import (
    Audio,
    Emphasis,
    Lang,
    Lookup,
    P,
    Prosody,
    S,
    Token,
    Voice,
    W,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.phoneme import Phoneme
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.say_as import SayAs
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.ssml_lexicon import (
    SsmlLexicon,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.ssml_meta import SsmlMeta
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.ssml_metadata import (
    SsmlMetadata,
)
from pyqti.models.org.w3.pkg_2001.pkg_10.synthesis.sub import Sub
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class Speak:
    class Meta:
        name = "speak"
        namespace = "http://www.w3.org/2001/10/synthesis"

    version: None | str = field(
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
    base: None | str = field(
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
    startmark: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    endmark: None | str = field(
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
                    "name": "meta",
                    "type": SsmlMeta,
                },
                {
                    "name": "metadata",
                    "type": SsmlMetadata,
                },
                {
                    "name": "lexicon",
                    "type": SsmlLexicon,
                },
                {
                    "name": "lang",
                    "type": Lang,
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
                    "type": Emphasis,
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
                    "name": "s",
                    "type": S,
                },
                {
                    "name": "p",
                    "type": P,
                },
                {
                    "name": "lookup",
                    "type": Lookup,
                },
            ),
        },
    )
