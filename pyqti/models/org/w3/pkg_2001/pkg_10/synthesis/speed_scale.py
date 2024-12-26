from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


class SpeedScale(Enum):
    """
    Descriptive values for speed.
    """

    X_FAST = "x-fast"
    FAST = "fast"
    MEDIUM = "medium"
    SLOW = "slow"
    X_SLOW = "x-slow"
    DEFAULT = "default"
