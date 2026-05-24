from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class ChoiceInteractionDtypeOrientation(Enum):
    """
    The orientation attribute provides a hint to rendering systems that the
    associated struct- ures have an inherent vertical or horizontal
    interpretation.
    """

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
