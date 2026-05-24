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
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_variables_dtype import (
    TestVariablesDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.variable_dtype import (
    VariableDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class SetValueDtype:
    """
    The setValue rule sets the value of a variable (response, outcome or
    template) to the val- ue obtained from the associated expression.

    A variable can be updated with reference to a previously assigned
    value, in other words, the variable being set may appear in the expre-
    ssion where it takes the value previously assigned to it. Special care
    is required when u- sing the numeric base-types because floating point
    values can not be assigned to integer variables and vice-versa. The
    truncate, round or integerToFloat operators must be used to achieve
    numeric type conversion.
    """

    class Meta:
        name = "SetValueDType"

    choice: (
        None
        | SetValueDtype.QtiAnd
        | SetValueDtype.QtiGt
        | SetValueDtype.QtiNot
        | SetValueDtype.QtiLt
        | SetValueDtype.QtiGte
        | SetValueDtype.QtiLte
        | SetValueDtype.QtiOr
        | NumericLogic1ToManyDtype
        | SetValueDtype.QtiDurationLt
        | SetValueDtype.QtiDurationGte
        | SetValueDtype.QtiSubtract
        | SetValueDtype.QtiDivide
        | SetValueDtype.QtiMultiple
        | SetValueDtype.QtiOrdered
        | CustomOperatorDtype
        | SetValueDtype.QtiRandom
        | SubstringDtype
        | EqualRoundedDtype
        | EmptyPrimitiveTypeDtype
        | SetValueDtype.QtiDelete
        | SetValueDtype.QtiMatch
        | IndexDtype
        | SetValueDtype.QtiPower
        | EqualDtype
        | SetValueDtype.QtiContains
        | SetValueDtype.QtiContainerSize
        | CorrectDtype
        | DefaultDtype
        | AnyNdtype
        | SetValueDtype.QtiIntegerDivide
        | SetValueDtype.QtiIntegerModulus
        | SetValueDtype.QtiIsNull
        | SetValueDtype.QtiMember
        | SetValueDtype.QtiProduct
        | SetValueDtype.QtiRound
        | SetValueDtype.QtiTruncate
        | FieldValueDtype
        | RandomIntegerDtype
        | RandomFloatDtype
        | VariableDtype
        | TestVariablesDtype
        | SetValueDtype.QtiIntegerToFloat
        | InsideDtype
        | BaseValueDtype
        | PatternMatchDtype
        | SetValueDtype.QtiMapResponsePoint
        | SetValueDtype.QtiMapResponse
        | StringMatchDtype
        | RepeatDtype
        | RoundToDtype
        | SetValueDtype.QtiLcm
        | SetValueDtype.QtiGcd
        | SetValueDtype.QtiMin
        | SetValueDtype.QtiMax
        | MathConstantDtype
        | StatsOperatorDtype
        | MathOperatorDtype
        | SetValueDtype.QtiNumberCorrect
        | SetValueDtype.QtiNumberIncorrect
        | SetValueDtype.QtiNumberPresented
        | SetValueDtype.QtiNumberResponded
        | SetValueDtype.QtiNumberSelected
        | SetValueDtype.QtiOutcomeMinimum
        | SetValueDtype.QtiOutcomeMaximum
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("SetValueDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("SetValueDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("SetValueDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("SetValueDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("SetValueDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("SetValueDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("SetValueDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": NumericLogic1ToManyDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("SetValueDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("SetValueDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("SetValueDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("SetValueDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("SetValueDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("SetValueDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("SetValueDtype.QtiRandom"),
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
                    "type": ForwardRef("SetValueDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("SetValueDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("SetValueDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("SetValueDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("SetValueDtype.QtiContainerSize"),
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
                    "type": ForwardRef("SetValueDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("SetValueDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("SetValueDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("SetValueDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("SetValueDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("SetValueDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("SetValueDtype.QtiTruncate"),
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
                    "type": ForwardRef("SetValueDtype.QtiIntegerToFloat"),
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
                    "type": ForwardRef("SetValueDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("SetValueDtype.QtiMapResponse"),
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
                    "type": ForwardRef("SetValueDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("SetValueDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("SetValueDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("SetValueDtype.QtiMax"),
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
                    "type": ForwardRef("SetValueDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("SetValueDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("SetValueDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("SetValueDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("SetValueDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("SetValueDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("SetValueDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
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
