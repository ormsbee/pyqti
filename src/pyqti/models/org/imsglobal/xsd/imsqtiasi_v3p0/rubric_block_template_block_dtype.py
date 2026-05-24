from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    CatalogInfoDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_dtype import (
    BaseSequenceXbaseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.rubric_block_template_block_content_body_dtype import (
    RubricBlockTemplateBlockContentBodyDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.rubric_block_template_block_dtype_show_hide import (
    RubricBlockTemplateBlockDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.style_sheet_dtype import (
    StyleSheetDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class RubricBlockTemplateBlockDtype(BaseSequenceXbaseDtype):
    """
    This is the container for the rubric content that is used in the
    context of template block content.
    """

    class Meta:
        name = "RubricBlockTemplateBlockDType"

    qti_stylesheet: list[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_content_body: None | RubricBlockTemplateBlockContentBodyDtype = field(
        default=None,
        metadata={
            "name": "qti-content-body",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_catalog_info: None | CatalogInfoDtype = field(
        default=None,
        metadata={
            "name": "qti-catalog-info",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    template_identifier: str = field(
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
        }
    )
    show_hide: RubricBlockTemplateBlockDtypeShowHide = field(
        default=RubricBlockTemplateBlockDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
