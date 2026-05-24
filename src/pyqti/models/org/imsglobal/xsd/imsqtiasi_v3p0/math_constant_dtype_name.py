from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class MathConstantDtypeName(Enum):
    """
    The set of mathematical constants available to the mathematical
    expressions.
    """

    PI = "pi"
    E = "e"
