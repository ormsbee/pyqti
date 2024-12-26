from dataclasses import dataclass, field
from typing import List, Optional

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


@dataclass
class RubricBlockTemplateBlockDtype(BaseSequenceXbaseDtype):
    """
    This is the container for the rubric content that is used in the context of
    template block content.
    """

    class Meta:
        name = "RubricBlockTemplateBlockDType"

    qti_stylesheet: List[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_content_body: Optional[RubricBlockTemplateBlockContentBodyDtype] = (
        field(
            default=None,
            metadata={
                "name": "qti-content-body",
                "type": "Element",
                "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            },
        )
    )
    qti_catalog_info: Optional[CatalogInfoDtype] = field(
        default=None,
        metadata={
            "name": "qti-catalog-info",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    show_hide: RubricBlockTemplateBlockDtypeShowHide = field(
        default=RubricBlockTemplateBlockDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
