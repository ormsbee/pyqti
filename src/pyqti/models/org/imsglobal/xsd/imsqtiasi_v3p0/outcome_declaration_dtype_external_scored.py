from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class OutcomeDeclarationDtypeExternalScored(Enum):
    """
    Identifies the set of modes for the exernal scoring of the Item.
    """

    EXTERNAL_MACHINE = "externalMachine"
    HUMAN = "human"
