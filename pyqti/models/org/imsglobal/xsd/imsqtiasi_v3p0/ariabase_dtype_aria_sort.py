from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class AriabaseDtypeAriaSort(Enum):
    """
    The permitted set of values for the aria-sort ARIA annotations.
    """

    ASCENDING = "ascending"
    DESCENDING = "descending"
    NONE = "none"
    OTHER = "other"
