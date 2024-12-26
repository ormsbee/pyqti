from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

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


@dataclass
class BranchRuleDtype:
    """A branch-rule is a simple expression attached to an assessment-item-ref,
    assessment-secti- on or test-part that is evaluated after the item, section or
    part has been presented to t- he candidate.

    If the expression evaluates to 'true' the test jumps forward to the
    item, s- ection or part referred to by the target identifier. In the
    case of an item or section, t- he target must refer to an item or
    section in the same test-part that has not yet been pr- esented. For
    test-parts, the target must refer to another test-part.
    """

    class Meta:
        name = "BranchRuleDType"

    choice: Optional[
        Union[
            "BranchRuleDtype.QtiAnd",
            "BranchRuleDtype.QtiGt",
            "BranchRuleDtype.QtiNot",
            "BranchRuleDtype.QtiLt",
            "BranchRuleDtype.QtiGte",
            "BranchRuleDtype.QtiLte",
            "BranchRuleDtype.QtiOr",
            NumericLogic1ToManyDtype,
            "BranchRuleDtype.QtiDurationLt",
            "BranchRuleDtype.QtiDurationGte",
            "BranchRuleDtype.QtiSubtract",
            "BranchRuleDtype.QtiDivide",
            "BranchRuleDtype.QtiMultiple",
            "BranchRuleDtype.QtiOrdered",
            CustomOperatorDtype,
            "BranchRuleDtype.QtiRandom",
            SubstringDtype,
            EqualRoundedDtype,
            EmptyPrimitiveTypeDtype,
            "BranchRuleDtype.QtiDelete",
            "BranchRuleDtype.QtiMatch",
            IndexDtype,
            "BranchRuleDtype.QtiPower",
            EqualDtype,
            "BranchRuleDtype.QtiContains",
            "BranchRuleDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "BranchRuleDtype.QtiIntegerDivide",
            "BranchRuleDtype.QtiIntegerModulus",
            "BranchRuleDtype.QtiIsNull",
            "BranchRuleDtype.QtiMember",
            "BranchRuleDtype.QtiProduct",
            "BranchRuleDtype.QtiRound",
            "BranchRuleDtype.QtiTruncate",
            FieldValueDtype,
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "BranchRuleDtype.QtiIntegerToFloat",
            InsideDtype,
            BaseValueDtype,
            PatternMatchDtype,
            "BranchRuleDtype.QtiMapResponsePoint",
            "BranchRuleDtype.QtiMapResponse",
            StringMatchDtype,
            RepeatDtype,
            RoundToDtype,
            "BranchRuleDtype.QtiLcm",
            "BranchRuleDtype.QtiGcd",
            "BranchRuleDtype.QtiMin",
            "BranchRuleDtype.QtiMax",
            MathConstantDtype,
            StatsOperatorDtype,
            MathOperatorDtype,
            "BranchRuleDtype.QtiNumberCorrect",
            "BranchRuleDtype.QtiNumberIncorrect",
            "BranchRuleDtype.QtiNumberPresented",
            "BranchRuleDtype.QtiNumberResponded",
            "BranchRuleDtype.QtiNumberSelected",
            "BranchRuleDtype.QtiOutcomeMinimum",
            "BranchRuleDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("BranchRuleDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("BranchRuleDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("BranchRuleDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("BranchRuleDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("BranchRuleDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("BranchRuleDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("BranchRuleDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": NumericLogic1ToManyDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("BranchRuleDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("BranchRuleDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("BranchRuleDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("BranchRuleDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("BranchRuleDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("BranchRuleDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("BranchRuleDtype.QtiRandom"),
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
                    "type": ForwardRef("BranchRuleDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("BranchRuleDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("BranchRuleDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("BranchRuleDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("BranchRuleDtype.QtiContainerSize"),
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
                    "type": ForwardRef("BranchRuleDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("BranchRuleDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("BranchRuleDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("BranchRuleDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("BranchRuleDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("BranchRuleDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("BranchRuleDtype.QtiTruncate"),
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
                    "type": ForwardRef("BranchRuleDtype.QtiIntegerToFloat"),
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
                    "type": ForwardRef("BranchRuleDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("BranchRuleDtype.QtiMapResponse"),
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
                    "type": ForwardRef("BranchRuleDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("BranchRuleDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("BranchRuleDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("BranchRuleDtype.QtiMax"),
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
                    "type": ForwardRef("BranchRuleDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("BranchRuleDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("BranchRuleDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("BranchRuleDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("BranchRuleDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("BranchRuleDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("BranchRuleDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    target: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class QtiAnd(Logic1ToManyDtype):
        pass

    @dataclass
    class QtiGt(LogicPairDtype):
        pass

    @dataclass
    class QtiNot(LogicSingleDtype):
        pass

    @dataclass
    class QtiLt(LogicPairDtype):
        pass

    @dataclass
    class QtiGte(LogicPairDtype):
        pass

    @dataclass
    class QtiLte(LogicPairDtype):
        pass

    @dataclass
    class QtiOr(Logic1ToManyDtype):
        pass

    @dataclass
    class QtiDurationLt(LogicPairDtype):
        pass

    @dataclass
    class QtiDurationGte(LogicPairDtype):
        pass

    @dataclass
    class QtiSubtract(LogicPairDtype):
        pass

    @dataclass
    class QtiDivide(LogicPairDtype):
        pass

    @dataclass
    class QtiMultiple(Logic0ToManyDtype):
        pass

    @dataclass
    class QtiOrdered(Logic0ToManyDtype):
        pass

    @dataclass
    class QtiRandom(LogicSingleDtype):
        pass

    @dataclass
    class QtiDelete(LogicPairDtype):
        pass

    @dataclass
    class QtiMatch(LogicPairDtype):
        pass

    @dataclass
    class QtiPower(LogicPairDtype):
        pass

    @dataclass
    class QtiContains(LogicPairDtype):
        pass

    @dataclass
    class QtiContainerSize(LogicSingleDtype):
        pass

    @dataclass
    class QtiIntegerDivide(LogicPairDtype):
        pass

    @dataclass
    class QtiIntegerModulus(LogicPairDtype):
        pass

    @dataclass
    class QtiIsNull(LogicSingleDtype):
        pass

    @dataclass
    class QtiMember(LogicPairDtype):
        pass

    @dataclass
    class QtiProduct(Logic1ToManyDtype):
        pass

    @dataclass
    class QtiRound(LogicSingleDtype):
        pass

    @dataclass
    class QtiTruncate(LogicSingleDtype):
        pass

    @dataclass
    class QtiIntegerToFloat(LogicSingleDtype):
        pass

    @dataclass
    class QtiMapResponsePoint(MapResponseDtype):
        pass

    @dataclass
    class QtiMapResponse(MapResponseDtype):
        pass

    @dataclass
    class QtiLcm(Logic1ToManyDtype):
        pass

    @dataclass
    class QtiGcd(Logic1ToManyDtype):
        pass

    @dataclass
    class QtiMin(Logic1ToManyDtype):
        pass

    @dataclass
    class QtiMax(Logic1ToManyDtype):
        pass

    @dataclass
    class QtiNumberCorrect(NumberDtype):
        pass

    @dataclass
    class QtiNumberIncorrect(NumberDtype):
        pass

    @dataclass
    class QtiNumberPresented(NumberDtype):
        pass

    @dataclass
    class QtiNumberResponded(NumberDtype):
        pass

    @dataclass
    class QtiNumberSelected(NumberDtype):
        pass

    @dataclass
    class QtiOutcomeMinimum(OutcomeMinMaxDtype):
        pass

    @dataclass
    class QtiOutcomeMaximum(OutcomeMinMaxDtype):
        pass
