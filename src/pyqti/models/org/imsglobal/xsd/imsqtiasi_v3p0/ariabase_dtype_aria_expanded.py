from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class AriabaseDtypeAriaExpanded(Enum):
    """
    The permitted set of values for the aria-expanded ARIA annotations.
    """

    TRUE = "true"
    FALSE = "false"
    UNDEFINED = "undefined"
