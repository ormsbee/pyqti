from dataclasses import dataclass, field
from typing import List, Optional, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.default_value_dtype import (
    DefaultValueDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.interpolation_table_dtype import (
    InterpolationTableDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.match_table_dtype import (
    MatchTableDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.outcome_declaration_dtype_base_type import (
    OutcomeDeclarationDtypeBaseType,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.outcome_declaration_dtype_cardinality import (
    OutcomeDeclarationDtypeCardinality,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.outcome_declaration_dtype_external_scored import (
    OutcomeDeclarationDtypeExternalScored,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.view_enum_dtype import (
    ViewEnumDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class OutcomeDeclarationDtype:
    """Outcome variables are declared by outcome declarations.

    Their value is set either from a default given in the declaration
    itself or by a responseRule during responseProcessing. I- tems that
    declare a numeric outcome variable representing the candidate's
    overall perform- ance on the item should use the outcome name
    'SCORE' for the variable. SCORE needs to be a float. Items that
    declare a maximum score (in multiple response choice interactions,
    for example) should do so by declaring the 'MAXSCORE' variable.
    MAXSCORE needs to be a float. Items or tests that want to make the
    fact that the candidate scored above a predefined th- reshold
    available as a variable should use the 'PASSED' variable. PASSED
    needs to be a bo- olean. At runtime, outcome variables are
    instantiated as part of an item session. Their v- alues may be
    initialized with a default value and/or set during
    responseProcessing. If no default value is given in the declaration
    then the outcome variable is initialized to NULL unless the outcome
    is of a numeric type (integer or float) in which case it is
    initialized to 0. Declared outcomes with numeric types should
    indicate their range of possible values using normalMaximum and
    normalMinimum, especially if this range differs from [0,1].
    """

    class Meta:
        name = "OutcomeDeclarationDType"

    qti_default_value: Optional[DefaultValueDtype] = field(
        default=None,
        metadata={
            "name": "qti-default-value",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_match_table_or_qti_interpolation_table: Optional[
        Union[MatchTableDtype, InterpolationTableDtype]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-match-table",
                    "type": MatchTableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-interpolation-table",
                    "type": InterpolationTableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    cardinality: Optional[OutcomeDeclarationDtypeCardinality] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    base_type: Optional[OutcomeDeclarationDtypeBaseType] = field(
        default=None,
        metadata={
            "name": "base-type",
            "type": "Attribute",
        },
    )
    view: List[ViewEnumDtype] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    interpretation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    long_interpretation: Optional[str] = field(
        default=None,
        metadata={
            "name": "long-interpretation",
            "type": "Attribute",
        },
    )
    normal_maximum: Optional[float] = field(
        default=None,
        metadata={
            "name": "normal-maximum",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    normal_minimum: Optional[float] = field(
        default=None,
        metadata={
            "name": "normal-minimum",
            "type": "Attribute",
        },
    )
    mastery_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "mastery-value",
            "type": "Attribute",
        },
    )
    external_scored: Optional[OutcomeDeclarationDtypeExternalScored] = field(
        default=None,
        metadata={
            "name": "external-scored",
            "type": "Attribute",
        },
    )
    variable_identifier_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "variable-identifier-ref",
            "type": "Attribute",
        },
    )
