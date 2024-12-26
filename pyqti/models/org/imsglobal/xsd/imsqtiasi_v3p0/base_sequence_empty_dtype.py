from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_empty_dtype import (
    AriabaseEmptyDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_empty_dtype_data_qti_suppress_tts import (
    BaseSequenceEmptyDtypeDataQtiSuppressTts,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_empty_dtype_dir import (
    BaseSequenceEmptyDtypeDir,
)
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class BaseSequenceEmptyDtype(AriabaseEmptyDtype):
    """This class provides the base characteristics for some of the HTML tag and
    QTI interactions which MUST NOT have any child tags.

    This class provides the base characteristics for some of the HTML
    tag and QTI interactions which MUST NOT have any child tags.
    """

    class Meta:
        name = "BaseSequenceEmptyDType"

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
    dir: BaseSequenceEmptyDtypeDir = field(
        default=BaseSequenceEmptyDtypeDir.AUTO,
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
        BaseSequenceEmptyDtypeDataQtiSuppressTts
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
