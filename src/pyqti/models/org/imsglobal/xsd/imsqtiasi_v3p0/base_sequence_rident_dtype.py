from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype import (
    AriabaseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_rident_dtype_data_qti_suppress_tts import (
    BaseSequenceRidentDtypeDataQtiSuppressTts,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_rident_dtype_dir import (
    BaseSequenceRidentDtypeDir,
)
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class BaseSequenceRidentDtype(AriabaseDtype):
    """
    The BaseSequenceRIdent class provides the base characteristics (as per
    the BaseSequence p- lus 'rident') for some of the QTI interactions.
    """

    class Meta:
        name = "BaseSequenceRIdentDType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    lang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    w3_org_xml_1998_namespace_lang: None | str | LangValue = field(
        default=None,
        metadata={
            "name": "lang",
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    label: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    response_identifier: str = field(
        metadata={
            "name": "response-identifier",
            "type": "Attribute",
        }
    )
    dir: BaseSequenceRidentDtypeDir = field(
        default=BaseSequenceRidentDtypeDir.AUTO,
        metadata={
            "type": "Attribute",
        },
    )
    data_catalog_idref: None | str = field(
        default=None,
        metadata={
            "name": "data-catalog-idref",
            "type": "Attribute",
        },
    )
    data_qti_suppress_tts: None | BaseSequenceRidentDtypeDataQtiSuppressTts = (
        field(
            default=None,
            metadata={
                "name": "data-qti-suppress-tts",
                "type": "Attribute",
            },
        )
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
