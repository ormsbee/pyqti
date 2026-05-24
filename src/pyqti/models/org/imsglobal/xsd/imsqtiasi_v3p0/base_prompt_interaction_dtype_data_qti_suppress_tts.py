from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class BasePromptInteractionDtypeDataQtiSuppressTts(Enum):
    """
    This is the permitted set of values for the 'data-qti-suppress-tts'
    attribute which is us- ed to to instruct the delivery/presentation
    system on whether, or not, the associated con- tent should be read out
    loud to the candidate.
    """

    COMPUTER_READ_ALOUD = "computer-read-aloud"
    SCREEN_READER = "screen-reader"
    ALL = "all"
