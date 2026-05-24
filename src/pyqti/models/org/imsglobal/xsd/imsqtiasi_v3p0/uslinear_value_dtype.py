from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.uslinear_value_dtype_unit import (
    UslinearValueDtypeUnit,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class UslinearValueDtype:
    """
    The container for the information about the increment (length and unit)
    of a Rule.

    The v- alue is the length in the associated type of, non-SI, unit.
    """

    class Meta:
        name = "USLinearValueDType"

    value: Decimal = field()
    unit: UslinearValueDtypeUnit = field(
        metadata={
            "type": "Attribute",
        }
    )
