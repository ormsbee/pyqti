from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_empty_dtype import (
    AriabaseEmptyDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype_data_qti_suppress_tts import (
    BaseSequenceXbaseEmptyDtypeDataQtiSuppressTts,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype_dir import (
    BaseSequenceXbaseEmptyDtypeDir,
)
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class BaseSequenceXbaseEmptyDtype(AriabaseEmptyDtype):
    """
    This is the base class for the HTML features and some QTI interactions
    that have no child- ren elements i.e. must be empty.

    This consists of a set of child characteristics.
    """

    class Meta:
        name = "BaseSequenceXBaseEmptyDType"

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
    w3_org_xml_1998_namespace_base: None | str = field(
        default=None,
        metadata={
            "name": "base",
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    dir: BaseSequenceXbaseEmptyDtypeDir = field(
        default=BaseSequenceXbaseEmptyDtypeDir.AUTO,
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
    data_qti_suppress_tts: (
        None | BaseSequenceXbaseEmptyDtypeDataQtiSuppressTts
    ) = field(
        default=None,
        metadata={
            "name": "data-qti-suppress-tts",
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
