from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class AriabaseDtypeAriaInvalid(Enum):
    """
    The permitted set of values for the aria-invalid ARIA annotations.
    """

    TRUE = "true"
    FALSE = "false"
    GRAMMAR = "grammar"
    SPELLING = "spelling"
