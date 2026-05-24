from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class Desc:
    class Meta:
        name = "desc"
        namespace = "http://www.w3.org/2001/10/synthesis"

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
        },
    )
