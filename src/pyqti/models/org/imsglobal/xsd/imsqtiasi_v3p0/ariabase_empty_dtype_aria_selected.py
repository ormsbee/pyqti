from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class AriabaseEmptyDtypeAriaSelected(Enum):
    """
    The permitted set of values for the aria-selected ARIA annotations.
    """

    TRUE = "true"
    FALSE = "false"
    UNDEFINED = "undefined"
