from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.radial_usvalue_dtype_unit import (
    RadialUsvalueDtypeUnit,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class RadialUsvalueDtype:
    """
    The container for the information about the increment size for a
    protractor.

    The value is in the associated type of non-SI unit.
    """

    class Meta:
        name = "RadialUSValueDType"

    value: Decimal = field()
    unit: RadialUsvalueDtypeUnit = field(
        metadata={
            "type": "Attribute",
        }
    )
