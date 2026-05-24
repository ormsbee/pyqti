from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


class VolumeScale(Enum):
    """
    descriptive values for volume.
    """

    SILENT = "silent"
    X_SOFT = "x-soft"
    SOFT = "soft"
    MEDIUM = "medium"
    LOUD = "loud"
    X_LOUD = "x-loud"
    DEFAULT = "default"
