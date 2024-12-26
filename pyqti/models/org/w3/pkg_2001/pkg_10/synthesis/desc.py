from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass
class Desc:
    class Meta:
        name = "desc"
        namespace = "http://www.w3.org/2001/10/synthesis"

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
        },
    )
