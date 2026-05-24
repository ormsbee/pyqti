from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


class GenderDatatype(Enum):
    MALE = "male"
    FEMALE = "female"
    NEUTRAL = "neutral"
    VALUE = ""
