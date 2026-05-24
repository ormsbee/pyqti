from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_variables_dtype_base_type import (
    TestVariablesDtypeBaseType,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class TestVariablesDtype(EmptyPrimitiveTypeDtype):
    """
    This is a QTI expression function.

    This expression, which can only be used in outcomes pr- ocessing,
    simultaneously looks up the value of an item variable in a sub-set of
    the items referred to in a test. Only variables with single cardinality
    are considered, all NULL va- lues are ignored. The result has
    cardinality multiple and base-type as specified below.
    """

    class Meta:
        name = "TestVariablesDType"

    section_identifier: None | str = field(
        default=None,
        metadata={
            "name": "section-identifier",
            "type": "Attribute",
        },
    )
    include_category: list[str] = field(
        default_factory=list,
        metadata={
            "name": "include-category",
            "type": "Attribute",
            "tokens": True,
        },
    )
    exclude_category: list[str] = field(
        default_factory=list,
        metadata={
            "name": "exclude-category",
            "type": "Attribute",
            "tokens": True,
        },
    )
    variable_identifier: str = field(
        metadata={
            "name": "variable-identifier",
            "type": "Attribute",
        }
    )
    weight_identifier: None | str = field(
        default=None,
        metadata={
            "name": "weight-identifier",
            "type": "Attribute",
        },
    )
    base_type: None | TestVariablesDtypeBaseType = field(
        default=None,
        metadata={
            "name": "base-type",
            "type": "Attribute",
        },
    )
