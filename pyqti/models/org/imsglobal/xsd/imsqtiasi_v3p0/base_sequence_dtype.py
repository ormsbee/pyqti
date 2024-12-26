from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype import (
    AriabaseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_dtype_data_qti_suppress_tts import (
    BaseSequenceDtypeDataQtiSuppressTts,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_dtype_dir import (
    BaseSequenceDtypeDir,
)
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class BaseSequenceDtype(AriabaseDtype):
    """
    The BaseSequence class provides the base characteristics for some of the HTML
    tag and QTI interactions.
    """

    class Meta:
        name = "BaseSequenceDType"

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
    label_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "label",
            "type": "Attribute",
        },
    )
    dir: BaseSequenceDtypeDir = field(
        default=BaseSequenceDtypeDir.AUTO,
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
    data_qti_suppress_tts: Optional[BaseSequenceDtypeDataQtiSuppressTts] = (
        field(
            default=None,
            metadata={
                "name": "data-qti-suppress-tts",
                "type": "Attribute",
            },
        )
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
