from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class EqualDtypeToleranceMode(Enum):
    """
    The tolerance mode determines whether the comparison is done exactly, using an
    absolute r- ange or a relative range.
    """

    ABSOLUTE = "absolute"
    EXACT = "exact"
    RELATIVE = "relative"
