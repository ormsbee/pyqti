from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class RubricBlockDtypeValue(Enum):
    INSTRUCTIONS = "instructions"
    SCORING = "scoring"
    NAVIGATION = "navigation"
