from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class TdhdtypeAlign(Enum):
    """
    Provides the permitted set of values for the 'align' attribute in the HTML
    markup i.e. how the associated object is horizontally aligned on the page.
    """

    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"
