from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.radial_sivalue_dtype_unit import (
    RadialSivalueDtypeUnit,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class RadialSivalueDtype:
    """
    The container for the information about the increment size for a
    protractor.

    The value is in the associated type of SI unit.
    """

    class Meta:
        name = "RadialSIValueDType"

    value: Decimal = field()
    unit: RadialSivalueDtypeUnit = field(
        metadata={
            "type": "Attribute",
        }
    )
