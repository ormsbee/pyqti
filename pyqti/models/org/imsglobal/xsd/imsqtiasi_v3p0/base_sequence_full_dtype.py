from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype import (
    AriabaseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_full_dtype_data_qti_suppress_tts import (
    BaseSequenceFullDtypeDataQtiSuppressTts,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_full_dtype_dir import (
    BaseSequenceFullDtypeDir,
)
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class BaseSequenceFullDtype(AriabaseDtype):
    """
    The BaseSequenceFull class provides the base characteristics for some of the
    QTI interact- ions that support the full set of base characteristics.
    """

    class Meta:
        name = "BaseSequenceFullDType"

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
    response_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "response-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    dir: BaseSequenceFullDtypeDir = field(
        default=BaseSequenceFullDtypeDir.AUTO,
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
        BaseSequenceFullDtypeDataQtiSuppressTts
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
