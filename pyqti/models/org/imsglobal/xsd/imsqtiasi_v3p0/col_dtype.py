from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype import (
    BaseSequenceXbaseEmptyDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ColDtype(BaseSequenceXbaseEmptyDtype):
    """Provides the functionality of the HTML 'col' tag.

    If a 'col' tag has a parent and that is a colgroup tag that itself
    has a parent that is a table tag, then the col tag represents one or
    more columns in the column group represented by that colgroup. The
    tag may have a span content attribute specified, whose value must be
    a valid non-negative integer greater than zero. The col tag and its
    span attribute take part in the table model.
    """

    class Meta:
        name = "ColDType"

    span: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
