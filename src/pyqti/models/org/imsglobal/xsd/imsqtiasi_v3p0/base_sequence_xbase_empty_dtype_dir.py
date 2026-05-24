from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class BaseSequenceXbaseEmptyDtypeDir(Enum):
    """
    To define the direction of the text layout as part of the Bi-direction
    (bidi) element in HTML.
    """

    LTR = "ltr"
    RTL = "rtl"
    AUTO = "auto"
