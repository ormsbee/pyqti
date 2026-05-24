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
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_constraint_dtype import (
    TemplateConstraintDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_variables_dtype import (
    TestVariablesDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.variable_dtype import (
    VariableDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class TemplateConditionDtype:
    """
    This class enables the definition of the template processing
    'If..Then..Else' clause.

    If the expression given in the templateIf or templateElseIf evaluates
    to 'true' then the sub- -rules contained within it are followed and any
    following templateElseIf or templateElse parts are ignored for this
    template condition. If the expression given in the templateIf or
    templateElseIf does not evaluate to 'true' then consideration passes to
    the next templ- ateElseIf or, if there are no more templateElseIf parts
    then the sub-rules of the templat- eElse are followed (if specified).
    """

    class Meta:
        name = "TemplateConditionDType"

    qti_template_if: TemplateIfDtype = field(
        metadata={
            "name": "qti-template-if",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        }
    )
    qti_template_else_if: list[TemplateIfDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-template-else-if",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_template_else: None | TemplateElseDtype = field(
        default=None,
        metadata={
            "name": "qti-template-else",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )


@dataclass(kw_only=True)
class TemplateElseDtype:
    """
    This enables the definition of the 'Else' clause of the
    'If..Then..Else' rule construction when defining a template.
    """

    class Meta:
        name = "TemplateElseDType"

    choice: list[
        TemplateElseDtype.QtiSetTemplateValue
        | EmptyPrimitiveTypeDtype
        | TemplateConditionDtype
        | TemplateElseDtype.QtiSetDefaultValue
        | TemplateElseDtype.QtiSetCorrectResponse
        | TemplateConstraintDtype
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-set-template-value",
                    "type": ForwardRef(
                        "TemplateElseDtype.QtiSetTemplateValue"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-exit-template",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-condition",
                    "type": TemplateConditionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-default-value",
                    "type": ForwardRef("TemplateElseDtype.QtiSetDefaultValue"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-correct-response",
                    "type": ForwardRef(
                        "TemplateElseDtype.QtiSetCorrectResponse"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-constraint",
                    "type": TemplateConstraintDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class QtiSetTemplateValue(SetValueDtype):
        pass

    @dataclass(kw_only=True)
    class QtiSetDefaultValue(SetValueDtype):
        pass

    @dataclass(kw_only=True)
    class QtiSetCorrectResponse(SetValueDtype):
        pass


@dataclass(kw_only=True)
class TemplateIfDtype:
    """
    This provides the 'If' and 'ElseIf' clauses of the 'If..Then..Else' for
    the template proc- essing functionality.

    A qti-response-if part consists of an expression which must have an
    effective base-type of boolean and single cardinality. For more
    information about the run- time data model employed see Expressions
    (Section 2). It also contains a set of sub-rules. If the expression is
    true then the sub-rules are processed, otherwise they are skipped (i-
    ncluding if the expression is NULL) and the following
    qti-template-else-if or qti-templat- e-else parts (if any) are
    considered instead.
    """

    class Meta:
        name = "TemplateIfDType"

    choice: (
        None
        | TemplateIfDtype.QtiAnd
        | TemplateIfDtype.QtiGt
        | TemplateIfDtype.QtiNot
        | TemplateIfDtype.QtiLt
        | TemplateIfDtype.QtiGte
        | TemplateIfDtype.QtiLte
        | TemplateIfDtype.QtiOr
        | NumericLogic1ToManyDtype
        | TemplateIfDtype.QtiDurationLt
        | TemplateIfDtype.QtiDurationGte
        | TemplateIfDtype.QtiSubtract
        | TemplateIfDtype.QtiDivide
        | TemplateIfDtype.QtiMultiple
        | TemplateIfDtype.QtiOrdered
        | CustomOperatorDtype
        | TemplateIfDtype.QtiRandom
        | SubstringDtype
        | EqualRoundedDtype
        | EmptyPrimitiveTypeDtype
        | TemplateIfDtype.QtiDelete
        | TemplateIfDtype.QtiMatch
        | IndexDtype
        | TemplateIfDtype.QtiPower
        | EqualDtype
        | TemplateIfDtype.QtiContains
        | TemplateIfDtype.QtiContainerSize
        | CorrectDtype
        | DefaultDtype
        | AnyNdtype
        | TemplateIfDtype.QtiIntegerDivide
        | TemplateIfDtype.QtiIntegerModulus
        | TemplateIfDtype.QtiIsNull
        | TemplateIfDtype.QtiMember
        | TemplateIfDtype.QtiProduct
        | TemplateIfDtype.QtiRound
        | TemplateIfDtype.QtiTruncate
        | FieldValueDtype
        | RandomIntegerDtype
        | RandomFloatDtype
        | VariableDtype
        | TestVariablesDtype
        | TemplateIfDtype.QtiIntegerToFloat
        | InsideDtype
        | BaseValueDtype
        | PatternMatchDtype
        | TemplateIfDtype.QtiMapResponsePoint
        | TemplateIfDtype.QtiMapResponse
        | StringMatchDtype
        | RepeatDtype
        | RoundToDtype
        | TemplateIfDtype.QtiLcm
        | TemplateIfDtype.QtiGcd
        | TemplateIfDtype.QtiMin
        | TemplateIfDtype.QtiMax
        | MathConstantDtype
        | StatsOperatorDtype
        | MathOperatorDtype
        | TemplateIfDtype.QtiNumberCorrect
        | TemplateIfDtype.QtiNumberIncorrect
        | TemplateIfDtype.QtiNumberPresented
        | TemplateIfDtype.QtiNumberResponded
        | TemplateIfDtype.QtiNumberSelected
        | TemplateIfDtype.QtiOutcomeMinimum
        | TemplateIfDtype.QtiOutcomeMaximum
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("TemplateIfDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("TemplateIfDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("TemplateIfDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("TemplateIfDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("TemplateIfDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("TemplateIfDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("TemplateIfDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": NumericLogic1ToManyDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("TemplateIfDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("TemplateIfDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("TemplateIfDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("TemplateIfDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("TemplateIfDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("TemplateIfDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("TemplateIfDtype.QtiRandom"),
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
                    "type": ForwardRef("TemplateIfDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("TemplateIfDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("TemplateIfDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("TemplateIfDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("TemplateIfDtype.QtiContainerSize"),
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
                    "type": ForwardRef("TemplateIfDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("TemplateIfDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("TemplateIfDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("TemplateIfDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("TemplateIfDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("TemplateIfDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("TemplateIfDtype.QtiTruncate"),
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
                    "type": ForwardRef("TemplateIfDtype.QtiIntegerToFloat"),
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
                    "type": ForwardRef("TemplateIfDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("TemplateIfDtype.QtiMapResponse"),
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
                    "type": ForwardRef("TemplateIfDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("TemplateIfDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("TemplateIfDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("TemplateIfDtype.QtiMax"),
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
                    "type": ForwardRef("TemplateIfDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("TemplateIfDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("TemplateIfDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("TemplateIfDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("TemplateIfDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("TemplateIfDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("TemplateIfDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    choice_1: list[
        TemplateIfDtype.QtiSetTemplateValue
        | EmptyPrimitiveTypeDtype
        | TemplateConditionDtype
        | TemplateIfDtype.QtiSetDefaultValue
        | TemplateIfDtype.QtiSetCorrectResponse
        | TemplateConstraintDtype
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-set-template-value",
                    "type": ForwardRef("TemplateIfDtype.QtiSetTemplateValue"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-exit-template",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-condition",
                    "type": TemplateConditionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-default-value",
                    "type": ForwardRef("TemplateIfDtype.QtiSetDefaultValue"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-correct-response",
                    "type": ForwardRef(
                        "TemplateIfDtype.QtiSetCorrectResponse"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-constraint",
                    "type": TemplateConstraintDtype,
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

    @dataclass(kw_only=True)
    class QtiSetTemplateValue(SetValueDtype):
        pass

    @dataclass(kw_only=True)
    class QtiSetDefaultValue(SetValueDtype):
        pass

    @dataclass(kw_only=True)
    class QtiSetCorrectResponse(SetValueDtype):
        pass
