from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class TestPartDtypeSubmissionMode(Enum):
    """
    The submission mode determines when the candidate's responses are submitted for
    response processing.
    """

    INDIVIDUAL = "individual"
    SIMULTANEOUS = "simultaneous"
