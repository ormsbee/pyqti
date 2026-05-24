from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class CalculatorDtypeQtiCalculatorType(Enum):
    """
    The permitted values for the type of calculator that can be supplied as
    companion materia- ls.
    """

    BASIC = "basic"
    STANDARD = "standard"
    SCIENTIFIC = "scientific"
    GRAPHING = "graphing"
