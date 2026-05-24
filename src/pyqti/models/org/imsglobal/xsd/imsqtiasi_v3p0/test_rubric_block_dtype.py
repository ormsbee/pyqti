from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    CatalogInfoDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_dtype import (
    BaseSequenceXbaseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.printed_variable_dtype import (
    PrintedVariableDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.style_sheet_dtype import (
    StyleSheetDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_rubric_block_content_body_dtype import (
    TestRubricBlockContentBodyDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_rubric_block_dtype_value import (
    TestRubricBlockDtypeValue,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.view_enum_dtype import (
    ViewEnumDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class TestRubricBlockDtype(BaseSequenceXbaseDtype):
    """
    The container for the test-level and section-level rubric block
    content.

    A rubric block i- dentifies part of the content that represents
    instructions to one or more of the actors t- hat view the test. Rubric
    Blocks MUST NOT be nested within other Rubric Blocks.
    """

    class Meta:
        name = "TestRubricBlockDType"

    qti_stylesheet: list[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_content_body: TestRubricBlockContentBodyDtype = field(
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
    qti_printed_variable: None | PrintedVariableDtype = field(
        default=None,
        metadata={
            "name": "qti-printed-variable",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    view: list[ViewEnumDtype] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    use: None | TestRubricBlockDtypeValue = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
