from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


class HeightScale(Enum):
    """
    Descriptive values for height.
    """

    X_HIGH = "x-high"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    X_LOW = "x-low"
    DEFAULT = "default"
