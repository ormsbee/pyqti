from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    CatalogInfoDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_dtype import (
    BaseSequenceXbaseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.rubric_block_content_body_dtype import (
    RubricBlockContentBodyDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.rubric_block_dtype_value import (
    RubricBlockDtypeValue,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.style_sheet_dtype import (
    StyleSheetDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.view_enum_dtype import (
    ViewEnumDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class RubricBlockDtype(BaseSequenceXbaseDtype):
    """
    The container for the rubric block content.

    A rubric block identifies part of the content that represents
    instructions to one or more of the actors that view the item. Although
    ru- bric blocks are defined as simpleBlocks they must not contain
    interactions but may contain template blocks. Rubric Blocks MUST NOT be
    nested within other Rubric Blocks.
    """

    class Meta:
        name = "RubricBlockDType"

    qti_stylesheet: list[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_content_body: RubricBlockContentBodyDtype = field(
        metadata={
            "name": "qti-content-body",
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
    use: RubricBlockDtypeValue = field(
        metadata={
            "type": "Attribute",
        }
    )
    view: list[ViewEnumDtype] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
