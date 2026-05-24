from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class UslinearValueDtypeUnit(Enum):
    """
    The permitted values for the non-SI length units.
    """

    INCH = "Inch"
    FOOT = "Foot"
    YARD = "Yard"
    MILE = "Mile"
