from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class AriarelevantListDtype(Enum):
    ADDITIONS = "additions"
    REMOVALS = "removals"
    TEXT = "text"
    ALL = "all"
    ADDITIONS_TEXT = "additions text"
