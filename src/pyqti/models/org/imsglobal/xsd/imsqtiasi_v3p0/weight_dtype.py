from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class WeightDtype(EmptyPrimitiveTypeDtype):
    """
    The contribution of an individual item score to an overall test score
    typically varies fr- om test to test.

    The score of the item is said to be weighted. Weights are defined as
    part of each reference to an item (qti-assessment-item-ref) within a
    test.
    """

    class Meta:
        name = "WeightDType"

    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    value: float = field(
        metadata={
            "type": "Attribute",
        }
    )
