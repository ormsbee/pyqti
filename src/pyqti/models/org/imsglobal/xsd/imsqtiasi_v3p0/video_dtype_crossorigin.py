from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class VideoDtypeCrossorigin(Enum):
    """
    The permitted set of values for the Cross Origin Resource Sharing ARIA
    settings.
    """

    ANONYMOUS = "anonymous"
    USE_CREDENTIALS = "use-credentials"
