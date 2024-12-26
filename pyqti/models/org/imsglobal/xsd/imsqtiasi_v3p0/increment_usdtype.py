from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.radial_usvalue_dtype import (
    RadialUsvalueDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class IncrementUsdtype:
    """
    The container for the information about the protractor defined in terms of US
    units.
    """

    class Meta:
        name = "IncrementUSDType"

    qti_minor_increment: Optional[RadialUsvalueDtype] = field(
        default=None,
        metadata={
            "name": "qti-minor-increment",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_major_increment: Optional[RadialUsvalueDtype] = field(
        default=None,
        metadata={
            "name": "qti-major-increment",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
