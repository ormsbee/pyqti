from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class ParamDtypeValuetype(Enum):
    """
    The type of parameters that may be associated with the HTML object.
    """

    DATA = "DATA"
    REF = "REF"
