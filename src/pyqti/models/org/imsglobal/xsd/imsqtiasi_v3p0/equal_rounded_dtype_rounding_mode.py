from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class EqualRoundedDtypeRoundingMode(Enum):
    """
    Definition of the rounding modes to be used on numeric calculations.
    """

    DECIMAL_PLACES = "decimalPlaces"
    SIGNIFICANT_FIGURES = "significantFigures"
