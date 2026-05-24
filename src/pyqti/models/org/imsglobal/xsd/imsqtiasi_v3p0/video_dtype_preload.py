from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class VideoDtypePreload(Enum):
    """
    This is the permitted set of values for the 'preload' attribute on the
    HTML5 'audio' and 'video' tags.
    """

    NONE = "none"
    AUTO = "auto"
    METADATA = "metadata"
