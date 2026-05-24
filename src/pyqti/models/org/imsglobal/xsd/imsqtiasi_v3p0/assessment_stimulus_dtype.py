from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    CatalogInfoDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.stimulus_body_dtype import (
    StimulusBodyDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.style_sheet_dtype import (
    StyleSheetDtype,
)
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class AssessmentStimulusDtype:
    """
    An assessment stimulus object is the used to enable content to be
    shared by several Asses- sment Items.

    The key feature is that this shared stimulus content must be supplied
    in the same context for each of the Assessment Items that make use of
    it. The assessment stimulus approach provides a mechanism to allow the
    stimulus content to be managed independently.
    """

    class Meta:
        name = "AssessmentStimulusDType"

    qti_stylesheet: list[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_stimulus_body: StimulusBodyDtype = field(
        metadata={
            "name": "qti-stimulus-body",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        }
    )
    qti_catalog_info: None | CatalogInfoDtype = field(
        default=None,
        metadata={
            "name": "qti-catalog-info",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    title: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    label: None | str = field(
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
    tool_name: None | str = field(
        default=None,
        metadata={
            "name": "tool-name",
            "type": "Attribute",
        },
    )
    tool_version: None | str = field(
        default=None,
        metadata={
            "name": "tool-version",
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
