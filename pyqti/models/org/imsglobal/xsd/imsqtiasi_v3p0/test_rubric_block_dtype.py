from dataclasses import dataclass, field
from typing import List, Optional

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


@dataclass
class TestRubricBlockDtype(BaseSequenceXbaseDtype):
    """The container for the test-level and section-level rubric block content.

    A rubric block i- dentifies part of the content that represents
    instructions to one or more of the actors t- hat view the test.
    Rubric Blocks MUST NOT be nested within other Rubric Blocks.
    """

    class Meta:
        name = "TestRubricBlockDType"

    qti_stylesheet: List[StyleSheetDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-stylesheet",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_content_body: Optional[TestRubricBlockContentBodyDtype] = field(
        default=None,
        metadata={
            "name": "qti-content-body",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
    qti_catalog_info: Optional[CatalogInfoDtype] = field(
        default=None,
        metadata={
            "name": "qti-catalog-info",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_printed_variable: Optional[PrintedVariableDtype] = field(
        default=None,
        metadata={
            "name": "qti-printed-variable",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    view: List[ViewEnumDtype] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    use: Optional[TestRubricBlockDtypeValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
