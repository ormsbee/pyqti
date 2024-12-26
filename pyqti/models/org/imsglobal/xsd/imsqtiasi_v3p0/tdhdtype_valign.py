from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class TdhdtypeValign(Enum):
    """
    Provides the permitted set of values for the 'valign' attribute in the HTML
    markup i.e. h- ow the associated object is vertically aligned on the page.
    """

    BOTTOM = "bottom"
    MIDDLE = "middle"
    TOP = "top"
    BASELINE = "baseline"
