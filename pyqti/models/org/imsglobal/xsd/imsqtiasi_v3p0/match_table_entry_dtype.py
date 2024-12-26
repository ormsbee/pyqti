from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.match_table_entry_dtype_target_value import (
    MatchTableEntryDtypeTargetValue,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class MatchTableEntryDtype(EmptyPrimitiveTypeDtype):
    """A qti-match-table transforms a source integer by finding the first qti-
    match-table-entry with an exact match to the source.

    The qti-match-table-entry allows the definition of each entry in the
    table.
    """

    class Meta:
        name = "MatchTableEntryDType"

    source_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "source-value",
            "type": "Attribute",
            "required": True,
        },
    )
    target_value: Optional[MatchTableEntryDtypeTargetValue] = field(
        default=None,
        metadata={
            "name": "target-value",
            "type": "Attribute",
            "required": True,
        },
    )
