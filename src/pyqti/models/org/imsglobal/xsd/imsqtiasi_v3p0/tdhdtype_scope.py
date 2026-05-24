from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class TdhdtypeScope(Enum):
    """
    The set of permitted values for the scope of a Table Cell.
    """

    COL = "col"
    COLGROUP = "colgroup"
    ROW = "row"
    ROWGROUP = "rowgroup"
