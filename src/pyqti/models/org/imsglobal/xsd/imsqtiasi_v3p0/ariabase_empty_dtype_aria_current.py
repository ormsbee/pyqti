from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class AriabaseEmptyDtypeAriaCurrent(Enum):
    """
    This is the permitted vocabulary for the 'aria-current' characteristic.

    The 'aria-current' attribute is used when an element within a set of
    related elements is visually styled to indicate it is the current item
    in the set.
    """

    PAGE = "page"
    STEP = "step"
    LOCATION = "location"
    DATE = "date"
    TIME = "time"
    TRUE = "true"
    FALSE = "false"
    UNDEFINED = "undefined"
