from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class TestFeedbackDtypeAccess(Enum):
    """
    The permitted set of values for defining the time at which the test
    feedback to the candi- date.
    """

    AT_END = "atEnd"
    DURING = "during"
