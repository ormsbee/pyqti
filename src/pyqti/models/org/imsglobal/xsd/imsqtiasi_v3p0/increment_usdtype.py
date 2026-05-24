from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.radial_usvalue_dtype import (
    RadialUsvalueDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class IncrementUsdtype:
    """
    The container for the information about the protractor defined in terms
    of US units.
    """

    class Meta:
        name = "IncrementUSDType"

    qti_minor_increment: None | RadialUsvalueDtype = field(
        default=None,
        metadata={
            "name": "qti-minor-increment",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_major_increment: RadialUsvalueDtype = field(
        metadata={
            "name": "qti-major-increment",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        }
    )
