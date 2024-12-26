from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class RadialUsvalueDtypeUnit(Enum):
    """
    The permitted values for the non-SI radial units.
    """

    DEGREE = "Degree"
    MINUTE = "Minute"
    SECOND = "Second"
