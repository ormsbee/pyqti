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
class OutcomeConditionDtype:
    """
    This enables the 'If..Then..Else' rules to be defined for the outcome
    processing.

    If the expression given in a outcomeIf or outcomeElseIf evaluates to
    'true' then the sub-rules c- ontained within it are followed and any
    following outcomeElseIf or outcomeElse parts are ignored for this
    outcome condition. If the expression given in a outcomeIf or
    outcomeElse- If does not evaluate to 'true' then consideration passes
    to the next outcomeElseIf or, if there are no more outcomeElseIf parts
    then the sub-rules of the outcomeElse are followed (if specified).
    """

    class Meta:
        name = "OutcomeConditionDType"

    qti_outcome_if: OutcomeIfDtype = field(
        metadata={
            "name": "qti-outcome-if",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        }
    )
    qti_outcome_else_if: list[OutcomeIfDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-outcome-else-if",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_outcome_else: None | OutcomeElseDtype = field(
        default=None,
        metadata={
            "name": "qti-outcome-else",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )


@dataclass(kw_only=True)
class OutcomeProcessingFragmentDtype:
    """
    An outcomeProcessingFragment is a simple group of outcomeRules which
    are grouped together in order to allow them to be managed as a separate
    resource.

    It should not be used for any other purpose.
    """

    class Meta:
        name = "OutcomeProcessingFragmentDType"

    choice: list[
        LookupOutcomeValueDtype
        | OutcomeProcessingFragmentDtype
        | SetValueDtype
        | Include
        | EmptyPrimitiveTypeDtype
        | OutcomeConditionDtype
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-lookup-outcome-value",
                    "type": LookupOutcomeValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-processing-fragment",
                    "type": ForwardRef("OutcomeProcessingFragmentDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-outcome-value",
                    "type": SetValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-exit-test",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-condition",
                    "type": OutcomeConditionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class OutcomeElseDtype:
    """
    This provides the else part of the 'if..then..elseif..else' structure
    for outcomes proces- sing.
    """

    class Meta:
        name = "OutcomeElseDType"

    choice: list[
        LookupOutcomeValueDtype
        | OutcomeProcessingFragmentDtype
        | SetValueDtype
        | Include
        | EmptyPrimitiveTypeDtype
        | OutcomeConditionDtype
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-lookup-outcome-value",
                    "type": LookupOutcomeValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-processing-fragment",
                    "type": OutcomeProcessingFragmentDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-outcome-value",
                    "type": SetValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-exit-test",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-condition",
                    "type": OutcomeConditionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class OutcomeIfDtype:
    """
    An outcomeIf part consists of an expression which must have an
    effective base-type of boo- lean and single cardinality.

    For more information about the runtime data model employed s- ee
    Expressions (Section 2). It also contains a set of sub-rules. If the
    expression is true then the sub-rules are processed, otherwise they are
    skipped (including if the expression is NULL) and the following
    outcomeElseIf or outcomeElse parts (if any) are considered ins- tead.
    """

    class Meta:
        name = "OutcomeIfDType"

    choice: (
        None
        | OutcomeIfDtype.QtiAnd
        | OutcomeIfDtype.QtiGt
        | OutcomeIfDtype.QtiNot
        | OutcomeIfDtype.QtiLt
        | OutcomeIfDtype.QtiGte
        | OutcomeIfDtype.QtiLte
        | OutcomeIfDtype.QtiOr
        | NumericLogic1ToManyDtype
        | OutcomeIfDtype.QtiDurationLt
        | OutcomeIfDtype.QtiDurationGte
        | OutcomeIfDtype.QtiSubtract
        | OutcomeIfDtype.QtiDivide
        | OutcomeIfDtype.QtiMultiple
        | OutcomeIfDtype.QtiOrdered
        | CustomOperatorDtype
        | OutcomeIfDtype.QtiRandom
        | SubstringDtype
        | EqualRoundedDtype
        | EmptyPrimitiveTypeDtype
        | OutcomeIfDtype.QtiDelete
        | OutcomeIfDtype.QtiMatch
        | IndexDtype
        | OutcomeIfDtype.QtiPower
        | EqualDtype
        | OutcomeIfDtype.QtiContains
        | OutcomeIfDtype.QtiContainerSize
        | CorrectDtype
        | DefaultDtype
        | AnyNdtype
        | OutcomeIfDtype.QtiIntegerDivide
        | OutcomeIfDtype.QtiIntegerModulus
        | OutcomeIfDtype.QtiIsNull
        | OutcomeIfDtype.QtiMember
        | OutcomeIfDtype.QtiProduct
        | OutcomeIfDtype.QtiRound
        | OutcomeIfDtype.QtiTruncate
        | FieldValueDtype
        | RandomIntegerDtype
        | RandomFloatDtype
        | VariableDtype
        | TestVariablesDtype
        | OutcomeIfDtype.QtiIntegerToFloat
        | InsideDtype
        | BaseValueDtype
        | PatternMatchDtype
        | OutcomeIfDtype.QtiMapResponsePoint
        | OutcomeIfDtype.QtiMapResponse
        | StringMatchDtype
        | RepeatDtype
        | RoundToDtype
        | OutcomeIfDtype.QtiLcm
        | OutcomeIfDtype.QtiGcd
        | OutcomeIfDtype.QtiMin
        | OutcomeIfDtype.QtiMax
        | MathConstantDtype
        | StatsOperatorDtype
        | MathOperatorDtype
        | OutcomeIfDtype.QtiNumberCorrect
        | OutcomeIfDtype.QtiNumberIncorrect
        | OutcomeIfDtype.QtiNumberPresented
        | OutcomeIfDtype.QtiNumberResponded
        | OutcomeIfDtype.QtiNumberSelected
        | OutcomeIfDtype.QtiOutcomeMinimum
        | OutcomeIfDtype.QtiOutcomeMaximum
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("OutcomeIfDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("OutcomeIfDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("OutcomeIfDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("OutcomeIfDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("OutcomeIfDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("OutcomeIfDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("OutcomeIfDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": NumericLogic1ToManyDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("OutcomeIfDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("OutcomeIfDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("OutcomeIfDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("OutcomeIfDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("OutcomeIfDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("OutcomeIfDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("OutcomeIfDtype.QtiRandom"),
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
                    "type": ForwardRef("OutcomeIfDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("OutcomeIfDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("OutcomeIfDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("OutcomeIfDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("OutcomeIfDtype.QtiContainerSize"),
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
                    "type": ForwardRef("OutcomeIfDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("OutcomeIfDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("OutcomeIfDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("OutcomeIfDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("OutcomeIfDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("OutcomeIfDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("OutcomeIfDtype.QtiTruncate"),
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
                    "type": ForwardRef("OutcomeIfDtype.QtiIntegerToFloat"),
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
                    "type": ForwardRef("OutcomeIfDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("OutcomeIfDtype.QtiMapResponse"),
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
                    "type": ForwardRef("OutcomeIfDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("OutcomeIfDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("OutcomeIfDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("OutcomeIfDtype.QtiMax"),
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
                    "type": ForwardRef("OutcomeIfDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("OutcomeIfDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("OutcomeIfDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("OutcomeIfDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("OutcomeIfDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("OutcomeIfDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("OutcomeIfDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    choice_1: list[
        LookupOutcomeValueDtype
        | OutcomeProcessingFragmentDtype
        | SetValueDtype
        | Include
        | EmptyPrimitiveTypeDtype
        | OutcomeConditionDtype
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-lookup-outcome-value",
                    "type": LookupOutcomeValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-processing-fragment",
                    "type": OutcomeProcessingFragmentDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-outcome-value",
                    "type": SetValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-exit-test",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-condition",
                    "type": OutcomeConditionDtype,
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
