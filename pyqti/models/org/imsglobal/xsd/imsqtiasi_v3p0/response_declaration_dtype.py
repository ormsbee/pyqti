from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.area_mapping_dtype import (
    AreaMappingDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.correct_response_dtype import (
    CorrectResponseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.default_value_dtype import (
    DefaultValueDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.mapping_dtype import (
    MappingDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.response_declaration_dtype_base_type import (
    ResponseDeclarationDtypeBaseType,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.response_declaration_dtype_cardinality import (
    ResponseDeclarationDtypeCardinality,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ResponseDeclarationDtype:
    """Response variables are declared by response declarations and bound to
    interactions in the itemBody.

    Each response variable declared may be bound to one and only one
    interaction. At runtime, response variables are instantiated as part
    of an item session. Their values are always initialized to NULL (no
    value) regardless of whether or not a default value is giv- en in
    the declaration. A response variable with a NULL value indicates
    that the candidate has not offered a response, either because they
    have not attempted the item at all or bec- ause they have attempted
    it and chosen not to provide a response. If a default value has been
    provided for a response variable then the variable is set to this
    value at the start of the first attempt. If the candidate never
    attempts the item, in other words, the item session passes straight
    from the initial state to the closed state without going through the
    interacting state, then the response variable remains NULL and the
    default value is n- ever used.
    """

    class Meta:
        name = "ResponseDeclarationDType"

    qti_default_value: Optional[DefaultValueDtype] = field(
        default=None,
        metadata={
            "name": "qti-default-value",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_correct_response: Optional[CorrectResponseDtype] = field(
        default=None,
        metadata={
            "name": "qti-correct-response",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_mapping: Optional[MappingDtype] = field(
        default=None,
        metadata={
            "name": "qti-mapping",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_area_mapping: Optional[AreaMappingDtype] = field(
        default=None,
        metadata={
            "name": "qti-area-mapping",
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
    cardinality: Optional[ResponseDeclarationDtypeCardinality] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    base_type: Optional[ResponseDeclarationDtypeBaseType] = field(
        default=None,
        metadata={
            "name": "base-type",
            "type": "Attribute",
        },
    )
