from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class TestPartDtypeNavigationMode(Enum):
    """
    The navigation mode determines the general paths that the candidate may take
    throught the test.
    """

    LINEAR = "linear"
    NONLINEAR = "nonlinear"
