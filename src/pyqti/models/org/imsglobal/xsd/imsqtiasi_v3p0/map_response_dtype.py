from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class MapResponseDtype(EmptyPrimitiveTypeDtype):
    """
    This is a QTI expression function.

    This expression looks up the value of a response varia- ble and then
    transforms it using the associated mapping, which must have been
    declared. T- he result is a single float. If the response variable has
    single cardinality then the val- ue returned is simply the mapped
    target value from the map. If the response variable has multiple or
    ordered cardinality then the value returned is the sum of the mapped
    target v- alues. This expression cannot be applied to variables of
    record cardinality. For example, if a mapping associates the
    identifiers {A,B,C,D} with the values {0,1,0.5,0} respectively then
    mapResponse will map the single value 'C' to the numeric value 0.5 and
    the set of va- lues {C,B} to the value 1.5. If a container contains
    multiple instances of the same value then that value is counted once
    only. To continue the example above {B,B,C} would still m- ap to 1.5
    and not 2.5.
    """

    class Meta:
        name = "MapResponseDType"

    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
