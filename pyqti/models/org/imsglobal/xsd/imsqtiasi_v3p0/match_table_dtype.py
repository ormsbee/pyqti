from dataclasses import dataclass, field
from typing import List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.match_table_entry_dtype import (
    MatchTableEntryDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class MatchTableDtype:
    """
    A matchTable transforms a source integer by finding the first qti-match-table-
    entry with an exact match to the source.
    """

    class Meta:
        name = "MatchTableDType"

    qti_match_table_entry: List[MatchTableEntryDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-match-table-entry",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    default_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "default-value",
            "type": "Attribute",
        },
    )
