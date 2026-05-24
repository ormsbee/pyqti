from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.silinear_value_dtype_unit import (
    SilinearValueDtypeUnit,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class SilinearValueDtype:
    """
    The container for the information about the increment (length and unit)
    of a Rule.

    The v- alue is the length in the associated type of SI unit.
    """

    class Meta:
        name = "SILinearValueDType"

    value: Decimal = field()
    unit: SilinearValueDtypeUnit = field(
        metadata={
            "type": "Attribute",
        }
    )
