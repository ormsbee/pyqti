from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class StatsOperatorDtypeName(Enum):
    """
    The set of permitted names for the statsOperator expression.
    """

    MEAN = "mean"
    SAMPLE_VARIANCE = "sampleVariance"
    SAMPLE_SD = "sampleSD"
    POP_VARIANCE = "popVariance"
    POP_SD = "popSD"
