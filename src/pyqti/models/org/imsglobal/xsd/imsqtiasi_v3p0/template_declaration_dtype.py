from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.default_value_dtype import (
    DefaultValueDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_declaration_dtype_base_type import (
    TemplateDeclarationDtypeBaseType,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_declaration_dtype_cardinality import (
    TemplateDeclarationDtypeCardinality,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class TemplateDeclarationDtype:
    """
    Template declarations declare item variables that are to be used
    specifically for the pur- poses of cloning items.

    They can have their value set only during templateProcessing. They are
    referred to within the itemBody in order to individualize the clone and
    possibly also within the responseProcessing rules if the cloning
    process affects the way the item is sc- ored.
    """

    class Meta:
        name = "TemplateDeclarationDType"

    qti_default_value: None | DefaultValueDtype = field(
        default=None,
        metadata={
            "name": "qti-default-value",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    cardinality: TemplateDeclarationDtypeCardinality = field(
        metadata={
            "type": "Attribute",
        }
    )
    base_type: None | TemplateDeclarationDtypeBaseType = field(
        default=None,
        metadata={
            "name": "base-type",
            "type": "Attribute",
        },
    )
    param_variable: bool = field(
        default=False,
        metadata={
            "name": "param-variable",
            "type": "Attribute",
        },
    )
    math_variable: bool = field(
        default=False,
        metadata={
            "name": "math-variable",
            "type": "Attribute",
        },
    )
