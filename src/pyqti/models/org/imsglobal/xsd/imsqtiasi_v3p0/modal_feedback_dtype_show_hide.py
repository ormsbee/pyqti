from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class ModalFeedbackDtypeShowHide(Enum):
    """
    The set of values for whether or not the associated object should be
    displayed or hidden.
    """

    SHOW = "show"
    HIDE = "hide"
