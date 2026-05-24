from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class AriabaseDtypeAriaChecked(Enum):
    """
    The permitted set of values for the aria-checked ARIA annotations.
    """

    TRUE = "true"
    FALSE = "false"
    MIXED = "mixed"
    UNDEFINED = "undefined"
