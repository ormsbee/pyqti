from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class AriabaseDtypeAriaLive(Enum):
    """
    The permitted set of values for the aria-live ARIA annotations.
    """

    OFF = "off"
    POLITE = "polite"
    ASSERTIVE = "assertive"
