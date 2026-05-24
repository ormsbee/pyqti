from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class MathOperatorDtypeName(Enum):
    """
    The set of permitted names for the mathOperator expression.
    """

    SIN = "sin"
    COS = "cos"
    TAN = "tan"
    SEC = "sec"
    CSC = "csc"
    COT = "cot"
    ASIN = "asin"
    ACOS = "acos"
    ATAN = "atan"
    ATAN2 = "atan2"
    ASEC = "asec"
    ACSC = "acsc"
    ACOT = "acot"
    SINH = "sinh"
    COSH = "cosh"
    TANH = "tanh"
    SECH = "sech"
    CSCH = "csch"
    COTH = "coth"
    LOG = "log"
    LN = "ln"
    EXP = "exp"
    ABS = "abs"
    SIGNUM = "signum"
    FLOOR = "floor"
    CEIL = "ceil"
    TO_DEGREES = "toDegrees"
    TO_RADIANS = "toRadians"
