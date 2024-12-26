from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class SilinearValueDtypeUnit(Enum):
    """
    The permitted values for the SI length units.
    """

    MILLIMETER = "Millimeter"
    CENTIMETER = "Centimeter"
    METER = "Meter"
    KILOMETER = "Kilometer"
