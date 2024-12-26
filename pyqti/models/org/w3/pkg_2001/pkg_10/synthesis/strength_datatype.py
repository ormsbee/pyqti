from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


class StrengthDatatype(Enum):
    NONE = "none"
    X_WEAK = "x-weak"
    WEAK = "weak"
    MEDIUM = "medium"
    STRONG = "strong"
    X_STRONG = "x-strong"
