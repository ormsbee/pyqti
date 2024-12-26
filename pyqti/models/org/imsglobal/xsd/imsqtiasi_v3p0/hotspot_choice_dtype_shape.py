from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class HotspotChoiceDtypeShape(Enum):
    """The permitted set of values for the shape of the associated region.

    A value of a shape is always accompanied by coordinates (see coords
    and an associated image which provides a co- ntext for interpreting
    them).
    """

    CIRCLE = "circle"
    DEFAULT = "default"
    ELLIPSE = "ellipse"
    POLY = "poly"
    RECT = "rect"
