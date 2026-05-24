from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.any_ndtype import (
    AnyNdtype,
    CustomOperatorDtype,
    EqualDtype,
    EqualRoundedDtype,
    FieldValueDtype,
    IndexDtype,
    InsideDtype,
    Logic0ToManyDtype,
    Logic1ToManyDtype,
    LogicPairDtype,
    LogicSingleDtype,
    MathOperatorDtype,
    NumericLogic1ToManyDtype,
    PatternMatchDtype,
    RepeatDtype,
    RoundToDtype,
    StatsOperatorDtype,
    StringMatchDtype,
    SubstringDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_value_dtype import (
    BaseValueDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.correct_dtype import (
    CorrectDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.default_dtype import (
    DefaultDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.lookup_outcome_value_dtype import (
    LookupOutcomeValueDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.map_response_dtype import (
    MapResponseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.math_constant_dtype import (
    MathConstantDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.number_dtype import (
    NumberDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.outcome_min_max_dtype import (
    OutcomeMinMaxDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.random_float_dtype import (
    RandomFloatDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.random_integer_dtype import (
    RandomIntegerDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.set_value_dtype import (
    SetValueDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_variables_dtype import (
    TestVariablesDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.variable_dtype import (
    VariableDtype,
)
from pyqti.models.org.w3.pkg_2001.xinclude.include_type import Include

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class ResponseConditionDtype:
    """
    This enables the 'If..Then..Else' rules to be defined for the response
    processing.

    If the expression given in a responseIf or responseElseIf evaluates to
    'true' then the sub-rules contained within it are followed and any
    following responseElseIf or responseElse parts a- re ignored for this
    response condition. If the expression given in a responseIf or respon-
    seElseIf does not evaluate to 'true' then consideration passes to the
    next responseElseIf or, if there are no more responseElseIf parts then
    the sub-rules of the responseElse are followed (if specified).
    """

    class Meta:
        name = "ResponseConditionDType"

    qti_response_if: ResponseIfDtype = field(
        metadata={
            "name": "qti-response-if",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        }
    )
    qti_response_else_if: list[ResponseIfDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-response-else-if",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_response_else: None | ResponseElseDtype = field(
        default=None,
        metadata={
            "name": "qti-response-else",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )


@dataclass(kw_only=True)
class ResponseProcessingFragmentDtype:
    """
    A responseProcessingFragment is a simple group of responseRules which
    are grouped together in order to allow them to be managed as a separate
    resource.

    It should not be used for any other purpose. Note that a response
    processing template allows a system to carry out resp- onse processing
    without having to parse the individual response processing rules. On
    the other hand, a responseProcessing element containing a reference to
    an externally defined response processing fragment must be parsed to
    determine the actions to carry out.
    """

    class Meta:
        name = "ResponseProcessingFragmentDType"

    choice: list[
        Include
        | ResponseConditionDtype
        | ResponseProcessingFragmentDtype
        | SetValueDtype
        | EmptyPrimitiveTypeDtype
        | LookupOutcomeValueDtype
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-response-condition",
                    "type": ResponseConditionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-response-processing-fragment",
                    "type": ForwardRef("ResponseProcessingFragmentDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-outcome-value",
                    "type": SetValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-exit-response",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lookup-outcome-value",
                    "type": LookupOutcomeValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ResponseElseDtype:
    """
    This provides the 'Else' clause of the 'If..Then..Else' for the
    response processing funct- ionality.

    If the expression given in a responseIf or responseElseIf evaluates to
    'true' t- hen the sub-rules contained within it are followed and any
    following responseElseIf or re- sponseElse parts are ignored for this
    response condition. If the expression given in a re- sponseIf or
    responseElseIf does not evaluate to 'true' then consideration passes to
    the n- ext responseElseIf or, if there are no more responseElseIf parts
    then the sub-rules of the responseElse are followed (if specified).
    """

    class Meta:
        name = "ResponseElseDType"

    choice: list[
        Include
        | ResponseConditionDtype
        | ResponseProcessingFragmentDtype
        | SetValueDtype
        | EmptyPrimitiveTypeDtype
        | LookupOutcomeValueDtype
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-response-condition",
                    "type": ResponseConditionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-response-processing-fragment",
                    "type": ResponseProcessingFragmentDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-outcome-value",
                    "type": SetValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-exit-response",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lookup-outcome-value",
                    "type": LookupOutcomeValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ResponseIfDtype:
    """
    This provides the 'If' and 'ElseIf' clauses of the 'If..Then..Else' for
    the response proc- essing functionality.

    A responseIf part consists of an expression which must have an effe-
    ctive base-type of boolean and single cardinality. For more information
    about the runtime data model employed see Expressions (Section 2). It
    also contains a set of sub-rules. If the expression is 'true' then the
    sub-rules are processed, otherwise they are skipped (in- cluding if the
    expression is NULL) and the following responseElseIf or responseElse
    parts (if any) are considered instead.
    """

    class Meta:
        name = "ResponseIfDType"

    choice: (
        None
        | ResponseIfDtype.QtiAnd
        | ResponseIfDtype.QtiGt
        | ResponseIfDtype.QtiNot
        | ResponseIfDtype.QtiLt
        | ResponseIfDtype.QtiGte
        | ResponseIfDtype.QtiLte
        | ResponseIfDtype.QtiOr
        | NumericLogic1ToManyDtype
        | ResponseIfDtype.QtiDurationLt
        | ResponseIfDtype.QtiDurationGte
        | ResponseIfDtype.QtiSubtract
        | ResponseIfDtype.QtiDivide
        | ResponseIfDtype.QtiMultiple
        | ResponseIfDtype.QtiOrdered
        | CustomOperatorDtype
        | ResponseIfDtype.QtiRandom
        | SubstringDtype
        | EqualRoundedDtype
        | EmptyPrimitiveTypeDtype
        | ResponseIfDtype.QtiDelete
        | ResponseIfDtype.QtiMatch
        | IndexDtype
        | ResponseIfDtype.QtiPower
        | EqualDtype
        | ResponseIfDtype.QtiContains
        | ResponseIfDtype.QtiContainerSize
        | CorrectDtype
        | DefaultDtype
        | AnyNdtype
        | ResponseIfDtype.QtiIntegerDivide
        | ResponseIfDtype.QtiIntegerModulus
        | ResponseIfDtype.QtiIsNull
        | ResponseIfDtype.QtiMember
        | ResponseIfDtype.QtiProduct
        | ResponseIfDtype.QtiRound
        | ResponseIfDtype.QtiTruncate
        | FieldValueDtype
        | RandomIntegerDtype
        | RandomFloatDtype
        | VariableDtype
        | TestVariablesDtype
        | ResponseIfDtype.QtiIntegerToFloat
        | InsideDtype
        | BaseValueDtype
        | PatternMatchDtype
        | ResponseIfDtype.QtiMapResponsePoint
        | ResponseIfDtype.QtiMapResponse
        | StringMatchDtype
        | RepeatDtype
        | RoundToDtype
        | ResponseIfDtype.QtiLcm
        | ResponseIfDtype.QtiGcd
        | ResponseIfDtype.QtiMin
        | ResponseIfDtype.QtiMax
        | MathConstantDtype
        | StatsOperatorDtype
        | MathOperatorDtype
        | ResponseIfDtype.QtiNumberCorrect
        | ResponseIfDtype.QtiNumberIncorrect
        | ResponseIfDtype.QtiNumberPresented
        | ResponseIfDtype.QtiNumberResponded
        | ResponseIfDtype.QtiNumberSelected
        | ResponseIfDtype.QtiOutcomeMinimum
        | ResponseIfDtype.QtiOutcomeMaximum
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("ResponseIfDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("ResponseIfDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("ResponseIfDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("ResponseIfDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("ResponseIfDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("ResponseIfDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("ResponseIfDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": NumericLogic1ToManyDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("ResponseIfDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("ResponseIfDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("ResponseIfDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("ResponseIfDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("ResponseIfDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("ResponseIfDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("ResponseIfDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": SubstringDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal-rounded",
                    "type": EqualRoundedDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("ResponseIfDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("ResponseIfDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("ResponseIfDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("ResponseIfDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("ResponseIfDtype.QtiContainerSize"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-correct",
                    "type": CorrectDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-default",
                    "type": DefaultDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-any-n",
                    "type": AnyNdtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-divide",
                    "type": ForwardRef("ResponseIfDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("ResponseIfDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("ResponseIfDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("ResponseIfDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("ResponseIfDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("ResponseIfDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("ResponseIfDtype.QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-field-value",
                    "type": FieldValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random-integer",
                    "type": RandomIntegerDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random-float",
                    "type": RandomFloatDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-variable",
                    "type": VariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-test-variables",
                    "type": TestVariablesDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-to-float",
                    "type": ForwardRef("ResponseIfDtype.QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inside",
                    "type": InsideDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-pattern-match",
                    "type": PatternMatchDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef("ResponseIfDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("ResponseIfDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": StringMatchDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": RepeatDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": RoundToDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("ResponseIfDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("ResponseIfDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("ResponseIfDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("ResponseIfDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": StatsOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": MathOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("ResponseIfDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("ResponseIfDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("ResponseIfDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("ResponseIfDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("ResponseIfDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("ResponseIfDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("ResponseIfDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    choice_1: list[
        Include
        | ResponseConditionDtype
        | ResponseProcessingFragmentDtype
        | SetValueDtype
        | EmptyPrimitiveTypeDtype
        | LookupOutcomeValueDtype
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-response-condition",
                    "type": ResponseConditionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-response-processing-fragment",
                    "type": ResponseProcessingFragmentDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-outcome-value",
                    "type": SetValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-exit-response",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lookup-outcome-value",
                    "type": LookupOutcomeValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class QtiAnd(Logic1ToManyDtype):
        pass

    @dataclass(kw_only=True)
    class QtiGt(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiNot(LogicSingleDtype):
        pass

    @dataclass(kw_only=True)
    class QtiLt(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiGte(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiLte(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiOr(Logic1ToManyDtype):
        pass

    @dataclass(kw_only=True)
    class QtiDurationLt(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiDurationGte(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiSubtract(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiDivide(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiMultiple(Logic0ToManyDtype):
        pass

    @dataclass(kw_only=True)
    class QtiOrdered(Logic0ToManyDtype):
        pass

    @dataclass(kw_only=True)
    class QtiRandom(LogicSingleDtype):
        pass

    @dataclass(kw_only=True)
    class QtiDelete(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiMatch(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiPower(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiContains(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiContainerSize(LogicSingleDtype):
        pass

    @dataclass(kw_only=True)
    class QtiIntegerDivide(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiIntegerModulus(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiIsNull(LogicSingleDtype):
        pass

    @dataclass(kw_only=True)
    class QtiMember(LogicPairDtype):
        pass

    @dataclass(kw_only=True)
    class QtiProduct(Logic1ToManyDtype):
        pass

    @dataclass(kw_only=True)
    class QtiRound(LogicSingleDtype):
        pass

    @dataclass(kw_only=True)
    class QtiTruncate(LogicSingleDtype):
        pass

    @dataclass(kw_only=True)
    class QtiIntegerToFloat(LogicSingleDtype):
        pass

    @dataclass(kw_only=True)
    class QtiMapResponsePoint(MapResponseDtype):
        pass

    @dataclass(kw_only=True)
    class QtiMapResponse(MapResponseDtype):
        pass

    @dataclass(kw_only=True)
    class QtiLcm(Logic1ToManyDtype):
        pass

    @dataclass(kw_only=True)
    class QtiGcd(Logic1ToManyDtype):
        pass

    @dataclass(kw_only=True)
    class QtiMin(Logic1ToManyDtype):
        pass

    @dataclass(kw_only=True)
    class QtiMax(Logic1ToManyDtype):
        pass

    @dataclass(kw_only=True)
    class QtiNumberCorrect(NumberDtype):
        pass

    @dataclass(kw_only=True)
    class QtiNumberIncorrect(NumberDtype):
        pass

    @dataclass(kw_only=True)
    class QtiNumberPresented(NumberDtype):
        pass

    @dataclass(kw_only=True)
    class QtiNumberResponded(NumberDtype):
        pass

    @dataclass(kw_only=True)
    class QtiNumberSelected(NumberDtype):
        pass

    @dataclass(kw_only=True)
    class QtiOutcomeMinimum(OutcomeMinMaxDtype):
        pass

    @dataclass(kw_only=True)
    class QtiOutcomeMaximum(OutcomeMinMaxDtype):
        pass
