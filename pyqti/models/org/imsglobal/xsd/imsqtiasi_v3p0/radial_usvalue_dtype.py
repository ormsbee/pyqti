from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.radial_usvalue_dtype_unit import (
    RadialUsvalueDtypeUnit,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class RadialUsvalueDtype:
    """The container for the information about the increment size for a protractor.

    The value is in the associated type of non-SI unit.
    """

    class Meta:
        name = "RadialUSValueDType"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    unit: Optional[RadialUsvalueDtypeUnit] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
