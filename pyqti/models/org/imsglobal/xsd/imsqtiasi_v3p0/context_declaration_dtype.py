from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.context_declaration_dtype_base_type import (
    ContextDeclarationDtypeBaseType,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.context_declaration_dtype_cardinality import (
    ContextDeclarationDtypeCardinality,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.default_value_dtype import (
    DefaultValueDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ContextDeclarationDtype:
    """Context variables, variables declared by context declarations, are global in
    scope in the information model.

    Context variables may be referenced in template processing, in
    response processing, and in outcome processing. Context variables
    are typically used to inject the "context" under which an item or
    test session is operating. There is one built-in context variable
    named "QTI_CONTEXT" with record cardinality. The built-in
    QTI_CONTEXT variable m- ust be fully resolved prior to any further
    processing.
    """

    class Meta:
        name = "ContextDeclarationDType"

    qti_default_value: Optional[DefaultValueDtype] = field(
        default=None,
        metadata={
            "name": "qti-default-value",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    cardinality: Optional[ContextDeclarationDtypeCardinality] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    base_type: Optional[ContextDeclarationDtypeBaseType] = field(
        default=None,
        metadata={
            "name": "base-type",
            "type": "Attribute",
        },
    )
