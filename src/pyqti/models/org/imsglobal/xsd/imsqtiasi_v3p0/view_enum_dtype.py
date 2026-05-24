from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class ViewEnumDtype(Enum):
    AUTHOR = "author"
    CANDIDATE = "candidate"
    PROCTOR = "proctor"
    SCORER = "scorer"
    TEST_CONSTRUCTOR = "testConstructor"
    TUTOR = "tutor"
