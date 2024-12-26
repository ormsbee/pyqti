from dataclasses import dataclass, field
from typing import Dict, ForwardRef, List, Optional, Union

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
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.equal_dtype_tolerance_mode import (
    EqualDtypeToleranceMode,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.equal_rounded_dtype_rounding_mode import (
    EqualRoundedDtypeRoundingMode,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.inside_dtype_shape import (
    InsideDtypeShape,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.map_response_dtype import (
    MapResponseDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.math_constant_dtype import (
    MathConstantDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.math_operator_dtype_name import (
    MathOperatorDtypeName,
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
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.round_to_dtype_rounding_mode import (
    RoundToDtypeRoundingMode,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.stats_operator_dtype_name import (
    StatsOperatorDtypeName,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.test_variables_dtype import (
    TestVariablesDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.variable_dtype import (
    VariableDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class AnyNdtype:
    """This is one of the expression functions. The 'anyN' operator takes one or
    more sub-expres- sions each with a base-type of boolean and single cardinality.
    The result is a single boo-

    lean which is true if at least min of the sub-expressions are true and at most max of the
    sub-expressions are true. If more than n - min sub-expressions are false (where n is the
    total number of sub-expressions) or more than max sub-expressions are true then the result
    is false. If one or more sub-expressions are NULL then it is possible that neither of the-
    se conditions is satisfied, in which case the operator results in NULL. For example, if m-
    in is 3 and max is 4 and the sub-expressions have values {true,true,false,NULL} then the
    operator results in NULL whereas {true,false,false,NULL} results in false and {true,true,-
    true,NULL} results in true. The result NULL indicates that the correct value for the oper-
    ator cannot be determined.
    """

    class Meta:
        name = "AnyNDType"

    choice: List[
        Union[
            "QtiAnd",
            "QtiGt",
            "QtiNot",
            "QtiLt",
            "QtiGte",
            "QtiLte",
            "QtiOr",
            "NumericLogic1ToManyDtype",
            "QtiDurationLt",
            "QtiDurationGte",
            "QtiSubtract",
            "QtiDivide",
            "QtiMultiple",
            "QtiOrdered",
            "CustomOperatorDtype",
            "QtiRandom",
            "SubstringDtype",
            "EqualRoundedDtype",
            EmptyPrimitiveTypeDtype,
            "QtiDelete",
            "QtiMatch",
            "IndexDtype",
            "QtiPower",
            "EqualDtype",
            "QtiContains",
            "QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            "AnyNdtype",
            "QtiIntegerDivide",
            "QtiIntegerModulus",
            "QtiIsNull",
            "QtiMember",
            "QtiProduct",
            "QtiRound",
            "QtiTruncate",
            "FieldValueDtype",
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "QtiIntegerToFloat",
            "InsideDtype",
            BaseValueDtype,
            "PatternMatchDtype",
            "AnyNdtype.QtiMapResponsePoint",
            "AnyNdtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "QtiLcm",
            "QtiGcd",
            "QtiMin",
            "QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "AnyNdtype.QtiNumberCorrect",
            "AnyNdtype.QtiNumberIncorrect",
            "AnyNdtype.QtiNumberPresented",
            "AnyNdtype.QtiNumberResponded",
            "AnyNdtype.QtiNumberSelected",
            "AnyNdtype.QtiOutcomeMinimum",
            "AnyNdtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": ForwardRef("CustomOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal-rounded",
                    "type": ForwardRef("EqualRoundedDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": ForwardRef("IndexDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": ForwardRef("EqualDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("QtiContainerSize"),
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
                    "type": ForwardRef("AnyNdtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-divide",
                    "type": ForwardRef("QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-field-value",
                    "type": ForwardRef("FieldValueDtype"),
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
                    "type": ForwardRef("QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inside",
                    "type": ForwardRef("InsideDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-pattern-match",
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef("AnyNdtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("AnyNdtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("AnyNdtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("AnyNdtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("AnyNdtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("AnyNdtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("AnyNdtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("AnyNdtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("AnyNdtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    min: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    max: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class QtiMapResponsePoint(MapResponseDtype):
        pass

    @dataclass
    class QtiMapResponse(MapResponseDtype):
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


@dataclass
class Logic1ToManyDtype:
    """
    This is the container for the combination of the one or more child expressions
    (see the E- xpressionGroup abstract class for the details on the permitted
    expressions).
    """

    class Meta:
        name = "Logic1toManyDType"

    choice: List[
        Union[
            "QtiAnd",
            "QtiGt",
            "QtiNot",
            "QtiLt",
            "QtiGte",
            "QtiLte",
            "QtiOr",
            "NumericLogic1ToManyDtype",
            "QtiDurationLt",
            "QtiDurationGte",
            "QtiSubtract",
            "QtiDivide",
            "QtiMultiple",
            "QtiOrdered",
            "CustomOperatorDtype",
            "QtiRandom",
            "SubstringDtype",
            "EqualRoundedDtype",
            EmptyPrimitiveTypeDtype,
            "QtiDelete",
            "QtiMatch",
            "IndexDtype",
            "QtiPower",
            "EqualDtype",
            "QtiContains",
            "QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "QtiIntegerDivide",
            "QtiIntegerModulus",
            "QtiIsNull",
            "QtiMember",
            "QtiProduct",
            "QtiRound",
            "QtiTruncate",
            "FieldValueDtype",
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "QtiIntegerToFloat",
            "InsideDtype",
            BaseValueDtype,
            "PatternMatchDtype",
            "Logic1ToManyDtype.QtiMapResponsePoint",
            "Logic1ToManyDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "QtiLcm",
            "QtiGcd",
            "QtiMin",
            "QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "Logic1ToManyDtype.QtiNumberCorrect",
            "Logic1ToManyDtype.QtiNumberIncorrect",
            "Logic1ToManyDtype.QtiNumberPresented",
            "Logic1ToManyDtype.QtiNumberResponded",
            "Logic1ToManyDtype.QtiNumberSelected",
            "Logic1ToManyDtype.QtiOutcomeMinimum",
            "Logic1ToManyDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": ForwardRef("CustomOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal-rounded",
                    "type": ForwardRef("EqualRoundedDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": ForwardRef("IndexDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": ForwardRef("EqualDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("QtiContainerSize"),
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
                    "type": ForwardRef("QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-field-value",
                    "type": ForwardRef("FieldValueDtype"),
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
                    "type": ForwardRef("QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inside",
                    "type": ForwardRef("InsideDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-pattern-match",
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef(
                        "Logic1ToManyDtype.QtiMapResponsePoint"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("Logic1ToManyDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("Logic1ToManyDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("Logic1ToManyDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("Logic1ToManyDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("Logic1ToManyDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("Logic1ToManyDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("Logic1ToManyDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("Logic1ToManyDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )

    @dataclass
    class QtiMapResponsePoint(MapResponseDtype):
        pass

    @dataclass
    class QtiMapResponse(MapResponseDtype):
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


@dataclass
class LogicPairDtype:
    """
    This is the container for the combination of the two child expressions (see the
    Expressio- nGroup abstract class for the details on the permitted expressions).
    """

    class Meta:
        name = "LogicPairDType"

    choice: List[
        Union[
            "LogicPairDtype.QtiAnd",
            "QtiGt",
            "QtiNot",
            "QtiLt",
            "QtiGte",
            "QtiLte",
            "LogicPairDtype.QtiOr",
            "NumericLogic1ToManyDtype",
            "QtiDurationLt",
            "QtiDurationGte",
            "QtiSubtract",
            "QtiDivide",
            "QtiMultiple",
            "QtiOrdered",
            "CustomOperatorDtype",
            "QtiRandom",
            "SubstringDtype",
            "EqualRoundedDtype",
            EmptyPrimitiveTypeDtype,
            "QtiDelete",
            "QtiMatch",
            "IndexDtype",
            "QtiPower",
            "EqualDtype",
            "QtiContains",
            "QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "QtiIntegerDivide",
            "QtiIntegerModulus",
            "QtiIsNull",
            "QtiMember",
            "LogicPairDtype.QtiProduct",
            "QtiRound",
            "QtiTruncate",
            "FieldValueDtype",
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "QtiIntegerToFloat",
            "InsideDtype",
            BaseValueDtype,
            "PatternMatchDtype",
            "LogicPairDtype.QtiMapResponsePoint",
            "LogicPairDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "LogicPairDtype.QtiLcm",
            "LogicPairDtype.QtiGcd",
            "LogicPairDtype.QtiMin",
            "LogicPairDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "LogicPairDtype.QtiNumberCorrect",
            "LogicPairDtype.QtiNumberIncorrect",
            "LogicPairDtype.QtiNumberPresented",
            "LogicPairDtype.QtiNumberResponded",
            "LogicPairDtype.QtiNumberSelected",
            "LogicPairDtype.QtiOutcomeMinimum",
            "LogicPairDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("LogicPairDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("LogicPairDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-custom-operator",
                    "type": ForwardRef("CustomOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-equal-rounded",
                    "type": ForwardRef("EqualRoundedDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-index",
                    "type": ForwardRef("IndexDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-equal",
                    "type": ForwardRef("EqualDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("QtiContainerSize"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-correct",
                    "type": CorrectDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-default",
                    "type": DefaultDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-any-n",
                    "type": AnyNdtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-divide",
                    "type": ForwardRef("QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("LogicPairDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-field-value",
                    "type": ForwardRef("FieldValueDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random-integer",
                    "type": RandomIntegerDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random-float",
                    "type": RandomFloatDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-variable",
                    "type": VariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-test-variables",
                    "type": TestVariablesDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-to-float",
                    "type": ForwardRef("QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-inside",
                    "type": ForwardRef("InsideDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-pattern-match",
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef("LogicPairDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("LogicPairDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("LogicPairDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("LogicPairDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("LogicPairDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("LogicPairDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("LogicPairDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("LogicPairDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("LogicPairDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("LogicPairDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("LogicPairDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("LogicPairDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("LogicPairDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
            ),
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )

    @dataclass
    class QtiAnd(Logic1ToManyDtype):
        pass

    @dataclass
    class QtiOr(Logic1ToManyDtype):
        pass

    @dataclass
    class QtiProduct(Logic1ToManyDtype):
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


@dataclass
class QtiAnd(Logic1ToManyDtype):
    class Meta:
        global_type = False


@dataclass
class QtiGcd(Logic1ToManyDtype):
    class Meta:
        global_type = False


@dataclass
class QtiLcm(Logic1ToManyDtype):
    class Meta:
        global_type = False


@dataclass
class QtiMax(Logic1ToManyDtype):
    class Meta:
        global_type = False


@dataclass
class QtiMin(Logic1ToManyDtype):
    class Meta:
        global_type = False


@dataclass
class QtiOr(Logic1ToManyDtype):
    class Meta:
        global_type = False


@dataclass
class QtiProduct(Logic1ToManyDtype):
    class Meta:
        global_type = False


@dataclass
class LogicSingleDtype:
    """
    This is the container for the combination of the single child expression (see
    the Express- ionGroup abstract class for the details on the permitted
    expressions).
    """

    class Meta:
        name = "LogicSingleDType"

    choice: Optional[
        Union[
            "LogicSingleDtype.QtiAnd",
            "LogicSingleDtype.QtiGt",
            "QtiNot",
            "LogicSingleDtype.QtiLt",
            "LogicSingleDtype.QtiGte",
            "LogicSingleDtype.QtiLte",
            "LogicSingleDtype.QtiOr",
            "NumericLogic1ToManyDtype",
            "LogicSingleDtype.QtiDurationLt",
            "LogicSingleDtype.QtiDurationGte",
            "LogicSingleDtype.QtiSubtract",
            "LogicSingleDtype.QtiDivide",
            "QtiMultiple",
            "QtiOrdered",
            "CustomOperatorDtype",
            "QtiRandom",
            "SubstringDtype",
            "EqualRoundedDtype",
            EmptyPrimitiveTypeDtype,
            "LogicSingleDtype.QtiDelete",
            "LogicSingleDtype.QtiMatch",
            "IndexDtype",
            "LogicSingleDtype.QtiPower",
            "EqualDtype",
            "LogicSingleDtype.QtiContains",
            "QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "LogicSingleDtype.QtiIntegerDivide",
            "LogicSingleDtype.QtiIntegerModulus",
            "QtiIsNull",
            "LogicSingleDtype.QtiMember",
            "LogicSingleDtype.QtiProduct",
            "QtiRound",
            "QtiTruncate",
            "FieldValueDtype",
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "QtiIntegerToFloat",
            "InsideDtype",
            BaseValueDtype,
            "PatternMatchDtype",
            "LogicSingleDtype.QtiMapResponsePoint",
            "LogicSingleDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "LogicSingleDtype.QtiLcm",
            "LogicSingleDtype.QtiGcd",
            "LogicSingleDtype.QtiMin",
            "LogicSingleDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "LogicSingleDtype.QtiNumberCorrect",
            "LogicSingleDtype.QtiNumberIncorrect",
            "LogicSingleDtype.QtiNumberPresented",
            "LogicSingleDtype.QtiNumberResponded",
            "LogicSingleDtype.QtiNumberSelected",
            "LogicSingleDtype.QtiOutcomeMinimum",
            "LogicSingleDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("LogicSingleDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("LogicSingleDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("LogicSingleDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("LogicSingleDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("LogicSingleDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("LogicSingleDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("LogicSingleDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("LogicSingleDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("LogicSingleDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("LogicSingleDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": ForwardRef("CustomOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal-rounded",
                    "type": ForwardRef("EqualRoundedDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("LogicSingleDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("LogicSingleDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": ForwardRef("IndexDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("LogicSingleDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": ForwardRef("EqualDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("LogicSingleDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("QtiContainerSize"),
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
                    "type": ForwardRef("LogicSingleDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("LogicSingleDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("LogicSingleDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("LogicSingleDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-field-value",
                    "type": ForwardRef("FieldValueDtype"),
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
                    "type": ForwardRef("QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inside",
                    "type": ForwardRef("InsideDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-pattern-match",
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef("LogicSingleDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("LogicSingleDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("LogicSingleDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("LogicSingleDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("LogicSingleDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("LogicSingleDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("LogicSingleDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("LogicSingleDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("LogicSingleDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("LogicSingleDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("LogicSingleDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("LogicSingleDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("LogicSingleDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )

    @dataclass
    class QtiAnd(Logic1ToManyDtype):
        pass

    @dataclass
    class QtiGt(LogicPairDtype):
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
    class QtiIntegerDivide(LogicPairDtype):
        pass

    @dataclass
    class QtiIntegerModulus(LogicPairDtype):
        pass

    @dataclass
    class QtiMember(LogicPairDtype):
        pass

    @dataclass
    class QtiProduct(Logic1ToManyDtype):
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


@dataclass
class QtiContains(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiDelete(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiDivide(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiDurationGte(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiDurationLt(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiGt(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiGte(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiIntegerDivide(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiIntegerModulus(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiLt(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiLte(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiMatch(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiMember(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiPower(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class QtiSubtract(LogicPairDtype):
    class Meta:
        global_type = False


@dataclass
class Logic0ToManyDtype:
    """
    This is the container for the combination of the zero or more child expressions
    (see the ExpressionGroup abstract class for the details on the permitted
    expressions).
    """

    class Meta:
        name = "Logic0toManyDType"

    choice: List[
        Union[
            "Logic0ToManyDtype.QtiAnd",
            "Logic0ToManyDtype.QtiGt",
            "Logic0ToManyDtype.QtiNot",
            "Logic0ToManyDtype.QtiLt",
            "Logic0ToManyDtype.QtiGte",
            "Logic0ToManyDtype.QtiLte",
            "Logic0ToManyDtype.QtiOr",
            "NumericLogic1ToManyDtype",
            "Logic0ToManyDtype.QtiDurationLt",
            "Logic0ToManyDtype.QtiDurationGte",
            "Logic0ToManyDtype.QtiSubtract",
            "Logic0ToManyDtype.QtiDivide",
            "QtiMultiple",
            "QtiOrdered",
            "CustomOperatorDtype",
            "Logic0ToManyDtype.QtiRandom",
            "SubstringDtype",
            "EqualRoundedDtype",
            EmptyPrimitiveTypeDtype,
            "Logic0ToManyDtype.QtiDelete",
            "Logic0ToManyDtype.QtiMatch",
            "IndexDtype",
            "Logic0ToManyDtype.QtiPower",
            "EqualDtype",
            "Logic0ToManyDtype.QtiContains",
            "Logic0ToManyDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "Logic0ToManyDtype.QtiIntegerDivide",
            "Logic0ToManyDtype.QtiIntegerModulus",
            "Logic0ToManyDtype.QtiIsNull",
            "Logic0ToManyDtype.QtiMember",
            "Logic0ToManyDtype.QtiProduct",
            "Logic0ToManyDtype.QtiRound",
            "Logic0ToManyDtype.QtiTruncate",
            "FieldValueDtype",
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "Logic0ToManyDtype.QtiIntegerToFloat",
            "InsideDtype",
            BaseValueDtype,
            "PatternMatchDtype",
            "Logic0ToManyDtype.QtiMapResponsePoint",
            "Logic0ToManyDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "Logic0ToManyDtype.QtiLcm",
            "Logic0ToManyDtype.QtiGcd",
            "Logic0ToManyDtype.QtiMin",
            "Logic0ToManyDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "Logic0ToManyDtype.QtiNumberCorrect",
            "Logic0ToManyDtype.QtiNumberIncorrect",
            "Logic0ToManyDtype.QtiNumberPresented",
            "Logic0ToManyDtype.QtiNumberResponded",
            "Logic0ToManyDtype.QtiNumberSelected",
            "Logic0ToManyDtype.QtiOutcomeMinimum",
            "Logic0ToManyDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("Logic0ToManyDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("Logic0ToManyDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("Logic0ToManyDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("Logic0ToManyDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("Logic0ToManyDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("Logic0ToManyDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("Logic0ToManyDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("Logic0ToManyDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("Logic0ToManyDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("Logic0ToManyDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("Logic0ToManyDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": ForwardRef("CustomOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("Logic0ToManyDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal-rounded",
                    "type": ForwardRef("EqualRoundedDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("Logic0ToManyDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("Logic0ToManyDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": ForwardRef("IndexDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("Logic0ToManyDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": ForwardRef("EqualDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("Logic0ToManyDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("Logic0ToManyDtype.QtiContainerSize"),
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
                    "type": ForwardRef("Logic0ToManyDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("Logic0ToManyDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("Logic0ToManyDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("Logic0ToManyDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("Logic0ToManyDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("Logic0ToManyDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("Logic0ToManyDtype.QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-field-value",
                    "type": ForwardRef("FieldValueDtype"),
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
                    "type": ForwardRef("Logic0ToManyDtype.QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inside",
                    "type": ForwardRef("InsideDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-pattern-match",
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef(
                        "Logic0ToManyDtype.QtiMapResponsePoint"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("Logic0ToManyDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("Logic0ToManyDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("Logic0ToManyDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("Logic0ToManyDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("Logic0ToManyDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("Logic0ToManyDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("Logic0ToManyDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("Logic0ToManyDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("Logic0ToManyDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("Logic0ToManyDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("Logic0ToManyDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("Logic0ToManyDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
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


@dataclass
class QtiContainerSize(LogicSingleDtype):
    class Meta:
        global_type = False


@dataclass
class QtiIntegerToFloat(LogicSingleDtype):
    class Meta:
        global_type = False


@dataclass
class QtiIsNull(LogicSingleDtype):
    class Meta:
        global_type = False


@dataclass
class QtiNot(LogicSingleDtype):
    class Meta:
        global_type = False


@dataclass
class QtiRandom(LogicSingleDtype):
    class Meta:
        global_type = False


@dataclass
class QtiRound(LogicSingleDtype):
    class Meta:
        global_type = False


@dataclass
class QtiTruncate(LogicSingleDtype):
    class Meta:
        global_type = False


@dataclass
class CustomOperatorDtype:
    """The custom operator provides an extension mechanism for defining operations
    not currently supported by this specification.

    It has been suggested that customOperator might be used to help link
    processing rules defined by this specification to instances of web-
    service b- ased processing engines. For example, a web-service which
    offered automated marking of fr- ee text responses. Implementors
    experimenting with this approach are encouraged to share information
    about their solutions to help determine the best way to achieve this
    type of processing.
    """

    class Meta:
        name = "CustomOperatorDType"

    choice: List[
        Union[
            "CustomOperatorDtype.QtiAnd",
            "CustomOperatorDtype.QtiGt",
            "CustomOperatorDtype.QtiNot",
            "CustomOperatorDtype.QtiLt",
            "CustomOperatorDtype.QtiGte",
            "CustomOperatorDtype.QtiLte",
            "CustomOperatorDtype.QtiOr",
            "NumericLogic1ToManyDtype",
            "CustomOperatorDtype.QtiDurationLt",
            "CustomOperatorDtype.QtiDurationGte",
            "CustomOperatorDtype.QtiSubtract",
            "CustomOperatorDtype.QtiDivide",
            "CustomOperatorDtype.QtiMultiple",
            "CustomOperatorDtype.QtiOrdered",
            "CustomOperatorDtype",
            "CustomOperatorDtype.QtiRandom",
            "SubstringDtype",
            "EqualRoundedDtype",
            EmptyPrimitiveTypeDtype,
            "CustomOperatorDtype.QtiDelete",
            "CustomOperatorDtype.QtiMatch",
            "IndexDtype",
            "CustomOperatorDtype.QtiPower",
            "EqualDtype",
            "CustomOperatorDtype.QtiContains",
            "CustomOperatorDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "CustomOperatorDtype.QtiIntegerDivide",
            "CustomOperatorDtype.QtiIntegerModulus",
            "CustomOperatorDtype.QtiIsNull",
            "CustomOperatorDtype.QtiMember",
            "CustomOperatorDtype.QtiProduct",
            "CustomOperatorDtype.QtiRound",
            "CustomOperatorDtype.QtiTruncate",
            "FieldValueDtype",
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "CustomOperatorDtype.QtiIntegerToFloat",
            "InsideDtype",
            BaseValueDtype,
            "PatternMatchDtype",
            "CustomOperatorDtype.QtiMapResponsePoint",
            "CustomOperatorDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "CustomOperatorDtype.QtiLcm",
            "CustomOperatorDtype.QtiGcd",
            "CustomOperatorDtype.QtiMin",
            "CustomOperatorDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "CustomOperatorDtype.QtiNumberCorrect",
            "CustomOperatorDtype.QtiNumberIncorrect",
            "CustomOperatorDtype.QtiNumberPresented",
            "CustomOperatorDtype.QtiNumberResponded",
            "CustomOperatorDtype.QtiNumberSelected",
            "CustomOperatorDtype.QtiOutcomeMinimum",
            "CustomOperatorDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("CustomOperatorDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("CustomOperatorDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("CustomOperatorDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("CustomOperatorDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("CustomOperatorDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("CustomOperatorDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("CustomOperatorDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("CustomOperatorDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("CustomOperatorDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("CustomOperatorDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("CustomOperatorDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("CustomOperatorDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("CustomOperatorDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": ForwardRef("CustomOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("CustomOperatorDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal-rounded",
                    "type": ForwardRef("EqualRoundedDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("CustomOperatorDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("CustomOperatorDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": ForwardRef("IndexDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("CustomOperatorDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": ForwardRef("EqualDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("CustomOperatorDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("CustomOperatorDtype.QtiContainerSize"),
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
                    "type": ForwardRef("CustomOperatorDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef(
                        "CustomOperatorDtype.QtiIntegerModulus"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("CustomOperatorDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("CustomOperatorDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("CustomOperatorDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("CustomOperatorDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("CustomOperatorDtype.QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-field-value",
                    "type": ForwardRef("FieldValueDtype"),
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
                    "type": ForwardRef(
                        "CustomOperatorDtype.QtiIntegerToFloat"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inside",
                    "type": ForwardRef("InsideDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-pattern-match",
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef(
                        "CustomOperatorDtype.QtiMapResponsePoint"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("CustomOperatorDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("CustomOperatorDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("CustomOperatorDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("CustomOperatorDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("CustomOperatorDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("CustomOperatorDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef(
                        "CustomOperatorDtype.QtiNumberIncorrect"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef(
                        "CustomOperatorDtype.QtiNumberPresented"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef(
                        "CustomOperatorDtype.QtiNumberResponded"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef(
                        "CustomOperatorDtype.QtiNumberSelected"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef(
                        "CustomOperatorDtype.QtiOutcomeMinimum"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef(
                        "CustomOperatorDtype.QtiOutcomeMaximum"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    definition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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


@dataclass
class QtiMultiple(Logic0ToManyDtype):
    class Meta:
        global_type = False


@dataclass
class QtiOrdered(Logic0ToManyDtype):
    class Meta:
        global_type = False


@dataclass
class EqualDtype:
    """The equal operator takes two sub-expressions which must both have single
    cardinality and have a numerical base-type.

    The result is a single boolean with a value of 'true' if the two
    expressions are numerically equal and 'false' if they are not. If
    either sub-expressi- on is NULL then the operator results in NULL.
    """

    class Meta:
        name = "EqualDType"

    choice: List[
        Union[
            "EqualDtype.QtiAnd",
            "EqualDtype.QtiGt",
            "EqualDtype.QtiNot",
            "EqualDtype.QtiLt",
            "EqualDtype.QtiGte",
            "EqualDtype.QtiLte",
            "EqualDtype.QtiOr",
            "NumericLogic1ToManyDtype",
            "EqualDtype.QtiDurationLt",
            "EqualDtype.QtiDurationGte",
            "EqualDtype.QtiSubtract",
            "EqualDtype.QtiDivide",
            "EqualDtype.QtiMultiple",
            "EqualDtype.QtiOrdered",
            CustomOperatorDtype,
            "EqualDtype.QtiRandom",
            "SubstringDtype",
            "EqualRoundedDtype",
            EmptyPrimitiveTypeDtype,
            "EqualDtype.QtiDelete",
            "EqualDtype.QtiMatch",
            "IndexDtype",
            "EqualDtype.QtiPower",
            "EqualDtype",
            "EqualDtype.QtiContains",
            "EqualDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "EqualDtype.QtiIntegerDivide",
            "EqualDtype.QtiIntegerModulus",
            "EqualDtype.QtiIsNull",
            "EqualDtype.QtiMember",
            "EqualDtype.QtiProduct",
            "EqualDtype.QtiRound",
            "EqualDtype.QtiTruncate",
            "FieldValueDtype",
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "EqualDtype.QtiIntegerToFloat",
            "InsideDtype",
            BaseValueDtype,
            "PatternMatchDtype",
            "EqualDtype.QtiMapResponsePoint",
            "EqualDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "EqualDtype.QtiLcm",
            "EqualDtype.QtiGcd",
            "EqualDtype.QtiMin",
            "EqualDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "EqualDtype.QtiNumberCorrect",
            "EqualDtype.QtiNumberIncorrect",
            "EqualDtype.QtiNumberPresented",
            "EqualDtype.QtiNumberResponded",
            "EqualDtype.QtiNumberSelected",
            "EqualDtype.QtiOutcomeMinimum",
            "EqualDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("EqualDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("EqualDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("EqualDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("EqualDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("EqualDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("EqualDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("EqualDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("EqualDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("EqualDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("EqualDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("EqualDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("EqualDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("EqualDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("EqualDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-equal-rounded",
                    "type": ForwardRef("EqualRoundedDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("EqualDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("EqualDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-index",
                    "type": ForwardRef("IndexDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("EqualDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-equal",
                    "type": ForwardRef("EqualDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("EqualDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("EqualDtype.QtiContainerSize"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-correct",
                    "type": CorrectDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-default",
                    "type": DefaultDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-any-n",
                    "type": AnyNdtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-divide",
                    "type": ForwardRef("EqualDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("EqualDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("EqualDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("EqualDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("EqualDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("EqualDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("EqualDtype.QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-field-value",
                    "type": ForwardRef("FieldValueDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random-integer",
                    "type": RandomIntegerDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random-float",
                    "type": RandomFloatDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-variable",
                    "type": VariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-test-variables",
                    "type": TestVariablesDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-to-float",
                    "type": ForwardRef("EqualDtype.QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-inside",
                    "type": ForwardRef("InsideDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-pattern-match",
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef("EqualDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("EqualDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("EqualDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("EqualDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("EqualDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("EqualDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("EqualDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("EqualDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("EqualDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("EqualDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("EqualDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("EqualDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("EqualDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
            ),
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    tolerance_mode: EqualDtypeToleranceMode = field(
        default=EqualDtypeToleranceMode.EXACT,
        metadata={
            "name": "tolerance-mode",
            "type": "Attribute",
        },
    )
    tolerance: List[Union[str, float]] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    include_lower_bound: bool = field(
        default=True,
        metadata={
            "name": "include-lower-bound",
            "type": "Attribute",
        },
    )
    include_upper_bound: bool = field(
        default=True,
        metadata={
            "name": "include-upper-bound",
            "type": "Attribute",
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


@dataclass
class EqualRoundedDtype:
    """The equalRounded operator takes two sub-expressions which must both have
    single cardinali- ty and have a numerical base-type.

    The result is a single boolean with a value of 'true' if the two
    expressions are numerically equal after rounding and 'false' if they
    are not. If either sub-expression is NULL then the operator results
    in NULL.
    """

    class Meta:
        name = "EqualRoundedDType"

    choice: List[
        Union[
            "EqualRoundedDtype.QtiAnd",
            "EqualRoundedDtype.QtiGt",
            "EqualRoundedDtype.QtiNot",
            "EqualRoundedDtype.QtiLt",
            "EqualRoundedDtype.QtiGte",
            "EqualRoundedDtype.QtiLte",
            "EqualRoundedDtype.QtiOr",
            "NumericLogic1ToManyDtype",
            "EqualRoundedDtype.QtiDurationLt",
            "EqualRoundedDtype.QtiDurationGte",
            "EqualRoundedDtype.QtiSubtract",
            "EqualRoundedDtype.QtiDivide",
            "EqualRoundedDtype.QtiMultiple",
            "EqualRoundedDtype.QtiOrdered",
            CustomOperatorDtype,
            "EqualRoundedDtype.QtiRandom",
            "SubstringDtype",
            "EqualRoundedDtype",
            EmptyPrimitiveTypeDtype,
            "EqualRoundedDtype.QtiDelete",
            "EqualRoundedDtype.QtiMatch",
            "IndexDtype",
            "EqualRoundedDtype.QtiPower",
            EqualDtype,
            "EqualRoundedDtype.QtiContains",
            "EqualRoundedDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "EqualRoundedDtype.QtiIntegerDivide",
            "EqualRoundedDtype.QtiIntegerModulus",
            "EqualRoundedDtype.QtiIsNull",
            "EqualRoundedDtype.QtiMember",
            "EqualRoundedDtype.QtiProduct",
            "EqualRoundedDtype.QtiRound",
            "EqualRoundedDtype.QtiTruncate",
            "FieldValueDtype",
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "EqualRoundedDtype.QtiIntegerToFloat",
            "InsideDtype",
            BaseValueDtype,
            "PatternMatchDtype",
            "EqualRoundedDtype.QtiMapResponsePoint",
            "EqualRoundedDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "EqualRoundedDtype.QtiLcm",
            "EqualRoundedDtype.QtiGcd",
            "EqualRoundedDtype.QtiMin",
            "EqualRoundedDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "EqualRoundedDtype.QtiNumberCorrect",
            "EqualRoundedDtype.QtiNumberIncorrect",
            "EqualRoundedDtype.QtiNumberPresented",
            "EqualRoundedDtype.QtiNumberResponded",
            "EqualRoundedDtype.QtiNumberSelected",
            "EqualRoundedDtype.QtiOutcomeMinimum",
            "EqualRoundedDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("EqualRoundedDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("EqualRoundedDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("EqualRoundedDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("EqualRoundedDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("EqualRoundedDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("EqualRoundedDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("EqualRoundedDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("EqualRoundedDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("EqualRoundedDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("EqualRoundedDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("EqualRoundedDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("EqualRoundedDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("EqualRoundedDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("EqualRoundedDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-equal-rounded",
                    "type": ForwardRef("EqualRoundedDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("EqualRoundedDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("EqualRoundedDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-index",
                    "type": ForwardRef("IndexDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("EqualRoundedDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("EqualRoundedDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("EqualRoundedDtype.QtiContainerSize"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-correct",
                    "type": CorrectDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-default",
                    "type": DefaultDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-any-n",
                    "type": AnyNdtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-divide",
                    "type": ForwardRef("EqualRoundedDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("EqualRoundedDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("EqualRoundedDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("EqualRoundedDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("EqualRoundedDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("EqualRoundedDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("EqualRoundedDtype.QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-field-value",
                    "type": ForwardRef("FieldValueDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random-integer",
                    "type": RandomIntegerDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random-float",
                    "type": RandomFloatDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-variable",
                    "type": VariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-test-variables",
                    "type": TestVariablesDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-to-float",
                    "type": ForwardRef("EqualRoundedDtype.QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-inside",
                    "type": ForwardRef("InsideDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-pattern-match",
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef(
                        "EqualRoundedDtype.QtiMapResponsePoint"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("EqualRoundedDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("EqualRoundedDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("EqualRoundedDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("EqualRoundedDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("EqualRoundedDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("EqualRoundedDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("EqualRoundedDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("EqualRoundedDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("EqualRoundedDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("EqualRoundedDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("EqualRoundedDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("EqualRoundedDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
            ),
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    rounding_mode: EqualRoundedDtypeRoundingMode = field(
        default=EqualRoundedDtypeRoundingMode.SIGNIFICANT_FIGURES,
        metadata={
            "name": "rounding-mode",
            "type": "Attribute",
        },
    )
    figures: Optional[object] = field(
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


@dataclass
class FieldValueDtype:
    """This is a QTI expression.

    The field value operator takes a sub-expression with a record c-
    ontainer value. The result is the value of the field with the
    specified field-identifier. If there is no field with that
    identifier then the result of the operator is NULL.
    """

    class Meta:
        name = "FieldValueDType"

    choice: Optional[
        Union[
            "FieldValueDtype.QtiAnd",
            "FieldValueDtype.QtiGt",
            "FieldValueDtype.QtiNot",
            "FieldValueDtype.QtiLt",
            "FieldValueDtype.QtiGte",
            "FieldValueDtype.QtiLte",
            "FieldValueDtype.QtiOr",
            "NumericLogic1ToManyDtype",
            "FieldValueDtype.QtiDurationLt",
            "FieldValueDtype.QtiDurationGte",
            "FieldValueDtype.QtiSubtract",
            "FieldValueDtype.QtiDivide",
            "FieldValueDtype.QtiMultiple",
            "FieldValueDtype.QtiOrdered",
            CustomOperatorDtype,
            "FieldValueDtype.QtiRandom",
            "SubstringDtype",
            EqualRoundedDtype,
            EmptyPrimitiveTypeDtype,
            "FieldValueDtype.QtiDelete",
            "FieldValueDtype.QtiMatch",
            "IndexDtype",
            "FieldValueDtype.QtiPower",
            EqualDtype,
            "FieldValueDtype.QtiContains",
            "FieldValueDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "FieldValueDtype.QtiIntegerDivide",
            "FieldValueDtype.QtiIntegerModulus",
            "FieldValueDtype.QtiIsNull",
            "FieldValueDtype.QtiMember",
            "FieldValueDtype.QtiProduct",
            "FieldValueDtype.QtiRound",
            "FieldValueDtype.QtiTruncate",
            "FieldValueDtype",
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "FieldValueDtype.QtiIntegerToFloat",
            "InsideDtype",
            BaseValueDtype,
            "PatternMatchDtype",
            "FieldValueDtype.QtiMapResponsePoint",
            "FieldValueDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "FieldValueDtype.QtiLcm",
            "FieldValueDtype.QtiGcd",
            "FieldValueDtype.QtiMin",
            "FieldValueDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "FieldValueDtype.QtiNumberCorrect",
            "FieldValueDtype.QtiNumberIncorrect",
            "FieldValueDtype.QtiNumberPresented",
            "FieldValueDtype.QtiNumberResponded",
            "FieldValueDtype.QtiNumberSelected",
            "FieldValueDtype.QtiOutcomeMinimum",
            "FieldValueDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("FieldValueDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("FieldValueDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("FieldValueDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("FieldValueDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("FieldValueDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("FieldValueDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("FieldValueDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("FieldValueDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("FieldValueDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("FieldValueDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("FieldValueDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("FieldValueDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("FieldValueDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("FieldValueDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
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
                    "type": ForwardRef("FieldValueDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("FieldValueDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": ForwardRef("IndexDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("FieldValueDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("FieldValueDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("FieldValueDtype.QtiContainerSize"),
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
                    "type": ForwardRef("FieldValueDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("FieldValueDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("FieldValueDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("FieldValueDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("FieldValueDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("FieldValueDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("FieldValueDtype.QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-field-value",
                    "type": ForwardRef("FieldValueDtype"),
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
                    "type": ForwardRef("FieldValueDtype.QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inside",
                    "type": ForwardRef("InsideDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-pattern-match",
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef("FieldValueDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("FieldValueDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("FieldValueDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("FieldValueDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("FieldValueDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("FieldValueDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("FieldValueDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("FieldValueDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("FieldValueDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("FieldValueDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("FieldValueDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("FieldValueDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("FieldValueDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    field_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "field-identifier",
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


@dataclass
class IndexDtype:
    """The index operator takes a sub-expression with an ordered container value
    and any base-ty- pe.

    The result is the nth value of the container. The result has the
    same base-type as the sub-expression but single cardinality. The
    first value of a container has index 1, the se- cond 2 and so on.
    'n' must be a positive integer. If 'n' exceeds the number of values
    in the container (or the sub-expression is NULL) then the result of
    the index operator is NU- LL. If 'n' is an identifier, it is the
    value of 'n' at runtime that is used.
    """

    class Meta:
        name = "IndexDType"

    choice: Optional[
        Union[
            "IndexDtype.QtiAnd",
            "IndexDtype.QtiGt",
            "IndexDtype.QtiNot",
            "IndexDtype.QtiLt",
            "IndexDtype.QtiGte",
            "IndexDtype.QtiLte",
            "IndexDtype.QtiOr",
            "NumericLogic1ToManyDtype",
            "IndexDtype.QtiDurationLt",
            "IndexDtype.QtiDurationGte",
            "IndexDtype.QtiSubtract",
            "IndexDtype.QtiDivide",
            "IndexDtype.QtiMultiple",
            "IndexDtype.QtiOrdered",
            CustomOperatorDtype,
            "IndexDtype.QtiRandom",
            "SubstringDtype",
            EqualRoundedDtype,
            EmptyPrimitiveTypeDtype,
            "IndexDtype.QtiDelete",
            "IndexDtype.QtiMatch",
            "IndexDtype",
            "IndexDtype.QtiPower",
            EqualDtype,
            "IndexDtype.QtiContains",
            "IndexDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "IndexDtype.QtiIntegerDivide",
            "IndexDtype.QtiIntegerModulus",
            "IndexDtype.QtiIsNull",
            "IndexDtype.QtiMember",
            "IndexDtype.QtiProduct",
            "IndexDtype.QtiRound",
            "IndexDtype.QtiTruncate",
            FieldValueDtype,
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "IndexDtype.QtiIntegerToFloat",
            "InsideDtype",
            BaseValueDtype,
            "PatternMatchDtype",
            "IndexDtype.QtiMapResponsePoint",
            "IndexDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "IndexDtype.QtiLcm",
            "IndexDtype.QtiGcd",
            "IndexDtype.QtiMin",
            "IndexDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "IndexDtype.QtiNumberCorrect",
            "IndexDtype.QtiNumberIncorrect",
            "IndexDtype.QtiNumberPresented",
            "IndexDtype.QtiNumberResponded",
            "IndexDtype.QtiNumberSelected",
            "IndexDtype.QtiOutcomeMinimum",
            "IndexDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("IndexDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("IndexDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("IndexDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("IndexDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("IndexDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("IndexDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("IndexDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("IndexDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("IndexDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("IndexDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("IndexDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("IndexDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("IndexDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("IndexDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
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
                    "type": ForwardRef("IndexDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("IndexDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": ForwardRef("IndexDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("IndexDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("IndexDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("IndexDtype.QtiContainerSize"),
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
                    "type": ForwardRef("IndexDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("IndexDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("IndexDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("IndexDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("IndexDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("IndexDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("IndexDtype.QtiTruncate"),
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
                    "type": ForwardRef("IndexDtype.QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inside",
                    "type": ForwardRef("InsideDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-pattern-match",
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef("IndexDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("IndexDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("IndexDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("IndexDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("IndexDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("IndexDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("IndexDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("IndexDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("IndexDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("IndexDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("IndexDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("IndexDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("IndexDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    n: Optional[object] = field(
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


@dataclass
class InsideDtype:
    """The inside operator takes a single sub-expression which must have a base-
    type of 'point'.

    The result is a single boolean with a value of 'true' if the given
    point is inside the ar- ea defined by shape and coords. If the sub-
    expression is a container the result is 'true' if any of the points
    are inside the area. If either sub-expression is NULL then the
    opera- tor results in NULL.
    """

    class Meta:
        name = "InsideDType"

    choice: Optional[
        Union[
            "InsideDtype.QtiAnd",
            "InsideDtype.QtiGt",
            "InsideDtype.QtiNot",
            "InsideDtype.QtiLt",
            "InsideDtype.QtiGte",
            "InsideDtype.QtiLte",
            "InsideDtype.QtiOr",
            "NumericLogic1ToManyDtype",
            "InsideDtype.QtiDurationLt",
            "InsideDtype.QtiDurationGte",
            "InsideDtype.QtiSubtract",
            "InsideDtype.QtiDivide",
            "InsideDtype.QtiMultiple",
            "InsideDtype.QtiOrdered",
            CustomOperatorDtype,
            "InsideDtype.QtiRandom",
            "SubstringDtype",
            EqualRoundedDtype,
            EmptyPrimitiveTypeDtype,
            "InsideDtype.QtiDelete",
            "InsideDtype.QtiMatch",
            IndexDtype,
            "InsideDtype.QtiPower",
            EqualDtype,
            "InsideDtype.QtiContains",
            "InsideDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "InsideDtype.QtiIntegerDivide",
            "InsideDtype.QtiIntegerModulus",
            "InsideDtype.QtiIsNull",
            "InsideDtype.QtiMember",
            "InsideDtype.QtiProduct",
            "InsideDtype.QtiRound",
            "InsideDtype.QtiTruncate",
            FieldValueDtype,
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "InsideDtype.QtiIntegerToFloat",
            "InsideDtype",
            BaseValueDtype,
            "PatternMatchDtype",
            "InsideDtype.QtiMapResponsePoint",
            "InsideDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "InsideDtype.QtiLcm",
            "InsideDtype.QtiGcd",
            "InsideDtype.QtiMin",
            "InsideDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "InsideDtype.QtiNumberCorrect",
            "InsideDtype.QtiNumberIncorrect",
            "InsideDtype.QtiNumberPresented",
            "InsideDtype.QtiNumberResponded",
            "InsideDtype.QtiNumberSelected",
            "InsideDtype.QtiOutcomeMinimum",
            "InsideDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("InsideDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("InsideDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("InsideDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("InsideDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("InsideDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("InsideDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("InsideDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("InsideDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("InsideDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("InsideDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("InsideDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("InsideDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("InsideDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("InsideDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
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
                    "type": ForwardRef("InsideDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("InsideDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("InsideDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("InsideDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("InsideDtype.QtiContainerSize"),
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
                    "type": ForwardRef("InsideDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("InsideDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("InsideDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("InsideDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("InsideDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("InsideDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("InsideDtype.QtiTruncate"),
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
                    "type": ForwardRef("InsideDtype.QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-inside",
                    "type": ForwardRef("InsideDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-pattern-match",
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef("InsideDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("InsideDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("InsideDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("InsideDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("InsideDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("InsideDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("InsideDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("InsideDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("InsideDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("InsideDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("InsideDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("InsideDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("InsideDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    shape: Optional[InsideDtypeShape] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    coords: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"(([0-9]+%?[,]){2}([0-9]+%?))|(([0-9]+%?[,]){3}([0-9]+%?))|(([0-9]+%?[,]){2}(([0-9]+%?[,]){2})+([0-9]+%?[,])([0-9]+%?))",
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


@dataclass
class MathOperatorDtype:
    """The mathOperator operator takes 1 or more sub-expressions which all have
    single cardinali- ty and have numerical base-types.

    The trigonometric functions, sin, cos and tan, take one argument in
    radians, which evaluates to a single float. Other functions take one
    numerical argument. Further functions might take more than one
    numerical argument, e.g. atan2 (two argument arc tan). The result is
    a single float, except for the functions signum, floor a- nd ceil,
    which return a single integer. If any of the sub-expressions is
    NULL, the result is NULL. If any of the sub-expressions falls
    outside the natural domain of the function c- alled by mathOperator,
    e.g. log(0) or asin(2), then the result is NULL.
    """

    class Meta:
        name = "MathOperatorDType"

    choice: List[
        Union[
            "MathOperatorDtype.QtiAnd",
            "MathOperatorDtype.QtiGt",
            "MathOperatorDtype.QtiNot",
            "MathOperatorDtype.QtiLt",
            "MathOperatorDtype.QtiGte",
            "MathOperatorDtype.QtiLte",
            "MathOperatorDtype.QtiOr",
            "NumericLogic1ToManyDtype",
            "MathOperatorDtype.QtiDurationLt",
            "MathOperatorDtype.QtiDurationGte",
            "MathOperatorDtype.QtiSubtract",
            "MathOperatorDtype.QtiDivide",
            "MathOperatorDtype.QtiMultiple",
            "MathOperatorDtype.QtiOrdered",
            CustomOperatorDtype,
            "MathOperatorDtype.QtiRandom",
            "SubstringDtype",
            EqualRoundedDtype,
            EmptyPrimitiveTypeDtype,
            "MathOperatorDtype.QtiDelete",
            "MathOperatorDtype.QtiMatch",
            IndexDtype,
            "MathOperatorDtype.QtiPower",
            EqualDtype,
            "MathOperatorDtype.QtiContains",
            "MathOperatorDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "MathOperatorDtype.QtiIntegerDivide",
            "MathOperatorDtype.QtiIntegerModulus",
            "MathOperatorDtype.QtiIsNull",
            "MathOperatorDtype.QtiMember",
            "MathOperatorDtype.QtiProduct",
            "MathOperatorDtype.QtiRound",
            "MathOperatorDtype.QtiTruncate",
            FieldValueDtype,
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "MathOperatorDtype.QtiIntegerToFloat",
            InsideDtype,
            BaseValueDtype,
            "PatternMatchDtype",
            "MathOperatorDtype.QtiMapResponsePoint",
            "MathOperatorDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "MathOperatorDtype.QtiLcm",
            "MathOperatorDtype.QtiGcd",
            "MathOperatorDtype.QtiMin",
            "MathOperatorDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            "MathOperatorDtype",
            "MathOperatorDtype.QtiNumberCorrect",
            "MathOperatorDtype.QtiNumberIncorrect",
            "MathOperatorDtype.QtiNumberPresented",
            "MathOperatorDtype.QtiNumberResponded",
            "MathOperatorDtype.QtiNumberSelected",
            "MathOperatorDtype.QtiOutcomeMinimum",
            "MathOperatorDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("MathOperatorDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("MathOperatorDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("MathOperatorDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("MathOperatorDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("MathOperatorDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("MathOperatorDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("MathOperatorDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("MathOperatorDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("MathOperatorDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("MathOperatorDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("MathOperatorDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("MathOperatorDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("MathOperatorDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("MathOperatorDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
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
                    "type": ForwardRef("MathOperatorDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("MathOperatorDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("MathOperatorDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("MathOperatorDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("MathOperatorDtype.QtiContainerSize"),
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
                    "type": ForwardRef("MathOperatorDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("MathOperatorDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("MathOperatorDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("MathOperatorDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("MathOperatorDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("MathOperatorDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("MathOperatorDtype.QtiTruncate"),
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
                    "type": ForwardRef("MathOperatorDtype.QtiIntegerToFloat"),
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
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef(
                        "MathOperatorDtype.QtiMapResponsePoint"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("MathOperatorDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("MathOperatorDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("MathOperatorDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("MathOperatorDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("MathOperatorDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": ForwardRef("MathOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("MathOperatorDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("MathOperatorDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("MathOperatorDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("MathOperatorDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("MathOperatorDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("MathOperatorDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("MathOperatorDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    name: Optional[MathOperatorDtypeName] = field(
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


@dataclass
class NumericLogic1ToManyDtype:
    """This is the container for the combination of the one or more child numeric
    expressions (s-

    ee the NumericExpressionGroup abstract class for the details on the
    permitted expressions- ).
    """

    class Meta:
        name = "NumericLogic1toManyDType"

    choice: List[
        Union[
            "NumericLogic1ToManyDtype",
            "NumericLogic1ToManyDtype.QtiSubtract",
            "NumericLogic1ToManyDtype.QtiDivide",
            "NumericLogic1ToManyDtype.QtiMultiple",
            "NumericLogic1ToManyDtype.QtiOrdered",
            CustomOperatorDtype,
            "NumericLogic1ToManyDtype.QtiRandom",
            EmptyPrimitiveTypeDtype,
            "NumericLogic1ToManyDtype.QtiDelete",
            IndexDtype,
            "NumericLogic1ToManyDtype.QtiPower",
            "NumericLogic1ToManyDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            "NumericLogic1ToManyDtype.QtiIntegerDivide",
            "NumericLogic1ToManyDtype.QtiIntegerModulus",
            "NumericLogic1ToManyDtype.QtiProduct",
            "NumericLogic1ToManyDtype.QtiRound",
            "NumericLogic1ToManyDtype.QtiTruncate",
            FieldValueDtype,
            RandomIntegerDtype,
            VariableDtype,
            TestVariablesDtype,
            "NumericLogic1ToManyDtype.QtiIntegerToFloat",
            BaseValueDtype,
            "NumericLogic1ToManyDtype.QtiMapResponsePoint",
            "NumericLogic1ToManyDtype.QtiMapResponse",
            "RepeatDtype",
            "RoundToDtype",
            "NumericLogic1ToManyDtype.QtiLcm",
            "NumericLogic1ToManyDtype.QtiGcd",
            "NumericLogic1ToManyDtype.QtiMin",
            "NumericLogic1ToManyDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            MathOperatorDtype,
            RandomFloatDtype,
            "NumericLogic1ToManyDtype.QtiNumberCorrect",
            "NumericLogic1ToManyDtype.QtiNumberIncorrect",
            "NumericLogic1ToManyDtype.QtiNumberPresented",
            "NumericLogic1ToManyDtype.QtiNumberResponded",
            "NumericLogic1ToManyDtype.QtiNumberSelected",
            "NumericLogic1ToManyDtype.QtiOutcomeMinimum",
            "NumericLogic1ToManyDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-sum",
                    "type": ForwardRef("NumericLogic1ToManyDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiContainerSize"
                    ),
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
                    "name": "qti-integer-divide",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiIntegerDivide"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiIntegerModulus"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiTruncate"),
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
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiIntegerToFloat"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiMapResponsePoint"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiMapResponse"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("NumericLogic1ToManyDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": MathOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random-float",
                    "type": RandomFloatDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiNumberCorrect"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiNumberIncorrect"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiNumberPresented"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiNumberResponded"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiNumberSelected"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiOutcomeMinimum"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef(
                        "NumericLogic1ToManyDtype.QtiOutcomeMaximum"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )

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
    class QtiPower(LogicPairDtype):
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


@dataclass
class PatternMatchDtype:
    """The patternMatch operator takes a sub-expression which must have single
    cardinality and a base-type of string.

    The result is a single boolean with a value of 'true' if the sub-
    exp- ression matches the regular expression given by pattern and
    'false' if it does not. If the sub-expression is NULL then the
    operator results in NULL.
    """

    class Meta:
        name = "PatternMatchDType"

    choice: Optional[
        Union[
            "PatternMatchDtype.QtiAnd",
            "PatternMatchDtype.QtiGt",
            "PatternMatchDtype.QtiNot",
            "PatternMatchDtype.QtiLt",
            "PatternMatchDtype.QtiGte",
            "PatternMatchDtype.QtiLte",
            "PatternMatchDtype.QtiOr",
            NumericLogic1ToManyDtype,
            "PatternMatchDtype.QtiDurationLt",
            "PatternMatchDtype.QtiDurationGte",
            "PatternMatchDtype.QtiSubtract",
            "PatternMatchDtype.QtiDivide",
            "PatternMatchDtype.QtiMultiple",
            "PatternMatchDtype.QtiOrdered",
            CustomOperatorDtype,
            "PatternMatchDtype.QtiRandom",
            "SubstringDtype",
            EqualRoundedDtype,
            EmptyPrimitiveTypeDtype,
            "PatternMatchDtype.QtiDelete",
            "PatternMatchDtype.QtiMatch",
            IndexDtype,
            "PatternMatchDtype.QtiPower",
            EqualDtype,
            "PatternMatchDtype.QtiContains",
            "PatternMatchDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "PatternMatchDtype.QtiIntegerDivide",
            "PatternMatchDtype.QtiIntegerModulus",
            "PatternMatchDtype.QtiIsNull",
            "PatternMatchDtype.QtiMember",
            "PatternMatchDtype.QtiProduct",
            "PatternMatchDtype.QtiRound",
            "PatternMatchDtype.QtiTruncate",
            FieldValueDtype,
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "PatternMatchDtype.QtiIntegerToFloat",
            InsideDtype,
            BaseValueDtype,
            "PatternMatchDtype",
            "PatternMatchDtype.QtiMapResponsePoint",
            "PatternMatchDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "PatternMatchDtype.QtiLcm",
            "PatternMatchDtype.QtiGcd",
            "PatternMatchDtype.QtiMin",
            "PatternMatchDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            MathOperatorDtype,
            "PatternMatchDtype.QtiNumberCorrect",
            "PatternMatchDtype.QtiNumberIncorrect",
            "PatternMatchDtype.QtiNumberPresented",
            "PatternMatchDtype.QtiNumberResponded",
            "PatternMatchDtype.QtiNumberSelected",
            "PatternMatchDtype.QtiOutcomeMinimum",
            "PatternMatchDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("PatternMatchDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("PatternMatchDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("PatternMatchDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("PatternMatchDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("PatternMatchDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("PatternMatchDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("PatternMatchDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": NumericLogic1ToManyDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("PatternMatchDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("PatternMatchDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("PatternMatchDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("PatternMatchDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("PatternMatchDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("PatternMatchDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("PatternMatchDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
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
                    "type": ForwardRef("PatternMatchDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("PatternMatchDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("PatternMatchDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("PatternMatchDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("PatternMatchDtype.QtiContainerSize"),
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
                    "type": ForwardRef("PatternMatchDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("PatternMatchDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("PatternMatchDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("PatternMatchDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("PatternMatchDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("PatternMatchDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("PatternMatchDtype.QtiTruncate"),
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
                    "type": ForwardRef("PatternMatchDtype.QtiIntegerToFloat"),
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
                    "type": ForwardRef("PatternMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef(
                        "PatternMatchDtype.QtiMapResponsePoint"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("PatternMatchDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("PatternMatchDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("PatternMatchDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("PatternMatchDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("PatternMatchDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": MathOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("PatternMatchDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("PatternMatchDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("PatternMatchDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("PatternMatchDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("PatternMatchDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("PatternMatchDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("PatternMatchDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    pattern: Optional[object] = field(
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


@dataclass
class RepeatDtype:
    """This is a QTI expression function.

    The repeat operator takes one or more sub-expressions, all of which
    must have either single or ordered cardinality and the same base-
    type. The r- esult is an ordered container having the same base-type
    as its sub-expressions. The conta- iner is filled sequentially by
    evaluating each sub-expression in turn and adding the resu- lting
    single values to the container, iterating this process number-
    repeats times in tota- l. If number-repeats refers to a variable
    whose value is less than 1, the value of the wh- ole expression is
    NULL. Any sub-expressions evaluating to NULL are ignored. If all
    sub-ex- pressions are NULL then the result is NULL.
    """

    class Meta:
        name = "RepeatDType"

    choice: List[
        Union[
            "RepeatDtype.QtiAnd",
            "RepeatDtype.QtiGt",
            "RepeatDtype.QtiNot",
            "RepeatDtype.QtiLt",
            "RepeatDtype.QtiGte",
            "RepeatDtype.QtiLte",
            "RepeatDtype.QtiOr",
            NumericLogic1ToManyDtype,
            "RepeatDtype.QtiDurationLt",
            "RepeatDtype.QtiDurationGte",
            "RepeatDtype.QtiSubtract",
            "RepeatDtype.QtiDivide",
            "RepeatDtype.QtiMultiple",
            "RepeatDtype.QtiOrdered",
            CustomOperatorDtype,
            "RepeatDtype.QtiRandom",
            "SubstringDtype",
            EqualRoundedDtype,
            EmptyPrimitiveTypeDtype,
            "RepeatDtype.QtiDelete",
            "RepeatDtype.QtiMatch",
            IndexDtype,
            "RepeatDtype.QtiPower",
            EqualDtype,
            "RepeatDtype.QtiContains",
            "RepeatDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "RepeatDtype.QtiIntegerDivide",
            "RepeatDtype.QtiIntegerModulus",
            "RepeatDtype.QtiIsNull",
            "RepeatDtype.QtiMember",
            "RepeatDtype.QtiProduct",
            "RepeatDtype.QtiRound",
            "RepeatDtype.QtiTruncate",
            FieldValueDtype,
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "RepeatDtype.QtiIntegerToFloat",
            InsideDtype,
            BaseValueDtype,
            PatternMatchDtype,
            "RepeatDtype.QtiMapResponsePoint",
            "RepeatDtype.QtiMapResponse",
            "StringMatchDtype",
            "RepeatDtype",
            "RoundToDtype",
            "RepeatDtype.QtiLcm",
            "RepeatDtype.QtiGcd",
            "RepeatDtype.QtiMin",
            "RepeatDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            MathOperatorDtype,
            "RepeatDtype.QtiNumberCorrect",
            "RepeatDtype.QtiNumberIncorrect",
            "RepeatDtype.QtiNumberPresented",
            "RepeatDtype.QtiNumberResponded",
            "RepeatDtype.QtiNumberSelected",
            "RepeatDtype.QtiOutcomeMinimum",
            "RepeatDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("RepeatDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("RepeatDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("RepeatDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("RepeatDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("RepeatDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("RepeatDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("RepeatDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": NumericLogic1ToManyDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("RepeatDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("RepeatDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("RepeatDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("RepeatDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("RepeatDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("RepeatDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("RepeatDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
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
                    "type": ForwardRef("RepeatDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("RepeatDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("RepeatDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("RepeatDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("RepeatDtype.QtiContainerSize"),
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
                    "type": ForwardRef("RepeatDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("RepeatDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("RepeatDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("RepeatDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("RepeatDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("RepeatDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("RepeatDtype.QtiTruncate"),
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
                    "type": ForwardRef("RepeatDtype.QtiIntegerToFloat"),
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
                    "type": ForwardRef("RepeatDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("RepeatDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": ForwardRef("RepeatDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("RepeatDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("RepeatDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("RepeatDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("RepeatDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": MathOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("RepeatDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("RepeatDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("RepeatDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("RepeatDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("RepeatDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("RepeatDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("RepeatDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    number_repeats: Optional[object] = field(
        default=None,
        metadata={
            "name": "number-repeats",
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


@dataclass
class RoundToDtype:
    """The roundTo operator takes one sub-expression which must have single
    cardinality and a nu- merical base-type.

    The result is a single float with the value nearest to that of the
    exp- ression's value such that when converted to a decimal string it
    represents the expression rounded by the specified rounding method
    to the specified precision. If the sub-expression is NULL, then the
    result is NULL. If the sub-expression is INF, then the result is
    INF. If the sub-expression is -INF, then the result is -INF. If the
    argument is NaN, then the res- ult is NULL. When rounding to n
    significant figures, the deciding digit is the (n+1)th di- git
    counting from the first non-zero digit from the left in the number.
    If the deciding d- igit is 5 or greater, the nth digit is increased
    by 1 and all digits to its right are dis- carded; if the deciding
    digit is less than 5, all digits to the right of the nth digit are
    discarded. When rounding to n decimal places, the deciding digit is
    the (n+1)th digit cou- nting to the right from the decimal point. If
    the deciding digit is 5 or greater, the nth digit is increased by 1
    and all digits to its right are discarded; if the deciding digit is
    less than 5, all digits to the right of the nth digit are discarded.
    """

    class Meta:
        name = "RoundToDType"

    choice: Optional[
        Union[
            "RoundToDtype.QtiAnd",
            "RoundToDtype.QtiGt",
            "RoundToDtype.QtiNot",
            "RoundToDtype.QtiLt",
            "RoundToDtype.QtiGte",
            "RoundToDtype.QtiLte",
            "RoundToDtype.QtiOr",
            NumericLogic1ToManyDtype,
            "RoundToDtype.QtiDurationLt",
            "RoundToDtype.QtiDurationGte",
            "RoundToDtype.QtiSubtract",
            "RoundToDtype.QtiDivide",
            "RoundToDtype.QtiMultiple",
            "RoundToDtype.QtiOrdered",
            CustomOperatorDtype,
            "RoundToDtype.QtiRandom",
            "SubstringDtype",
            EqualRoundedDtype,
            EmptyPrimitiveTypeDtype,
            "RoundToDtype.QtiDelete",
            "RoundToDtype.QtiMatch",
            IndexDtype,
            "RoundToDtype.QtiPower",
            EqualDtype,
            "RoundToDtype.QtiContains",
            "RoundToDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "RoundToDtype.QtiIntegerDivide",
            "RoundToDtype.QtiIntegerModulus",
            "RoundToDtype.QtiIsNull",
            "RoundToDtype.QtiMember",
            "RoundToDtype.QtiProduct",
            "RoundToDtype.QtiRound",
            "RoundToDtype.QtiTruncate",
            FieldValueDtype,
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "RoundToDtype.QtiIntegerToFloat",
            InsideDtype,
            BaseValueDtype,
            PatternMatchDtype,
            "RoundToDtype.QtiMapResponsePoint",
            "RoundToDtype.QtiMapResponse",
            "StringMatchDtype",
            RepeatDtype,
            "RoundToDtype",
            "RoundToDtype.QtiLcm",
            "RoundToDtype.QtiGcd",
            "RoundToDtype.QtiMin",
            "RoundToDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            MathOperatorDtype,
            "RoundToDtype.QtiNumberCorrect",
            "RoundToDtype.QtiNumberIncorrect",
            "RoundToDtype.QtiNumberPresented",
            "RoundToDtype.QtiNumberResponded",
            "RoundToDtype.QtiNumberSelected",
            "RoundToDtype.QtiOutcomeMinimum",
            "RoundToDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("RoundToDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("RoundToDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("RoundToDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("RoundToDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("RoundToDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("RoundToDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("RoundToDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": NumericLogic1ToManyDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("RoundToDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("RoundToDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("RoundToDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("RoundToDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("RoundToDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("RoundToDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("RoundToDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
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
                    "type": ForwardRef("RoundToDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("RoundToDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("RoundToDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("RoundToDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("RoundToDtype.QtiContainerSize"),
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
                    "type": ForwardRef("RoundToDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("RoundToDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("RoundToDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("RoundToDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("RoundToDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("RoundToDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("RoundToDtype.QtiTruncate"),
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
                    "type": ForwardRef("RoundToDtype.QtiIntegerToFloat"),
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
                    "type": ForwardRef("RoundToDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("RoundToDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-repeat",
                    "type": RepeatDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round-to",
                    "type": ForwardRef("RoundToDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("RoundToDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("RoundToDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("RoundToDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("RoundToDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": MathOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("RoundToDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("RoundToDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("RoundToDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("RoundToDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("RoundToDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("RoundToDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("RoundToDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    rounding_mode: Optional[RoundToDtypeRoundingMode] = field(
        default=None,
        metadata={
            "name": "rounding-mode",
            "type": "Attribute",
            "required": True,
        },
    )
    figures: Optional[object] = field(
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


@dataclass
class StatsOperatorDtype:
    """The statsOperator operator takes 1 sub-expression which is a container of
    multiple or ord- ered cardinality and has a numerical base-type.

    The result is a single float. If the sub-- expression or any value
    contained therein is NULL, the result is NULL. If any value conta-
    ined in the sub-expression is not a numerical value, then the result
    is NULL.
    """

    class Meta:
        name = "StatsOperatorDType"

    choice: Optional[
        Union[
            "StatsOperatorDtype.QtiAnd",
            "StatsOperatorDtype.QtiGt",
            "StatsOperatorDtype.QtiNot",
            "StatsOperatorDtype.QtiLt",
            "StatsOperatorDtype.QtiGte",
            "StatsOperatorDtype.QtiLte",
            "StatsOperatorDtype.QtiOr",
            NumericLogic1ToManyDtype,
            "StatsOperatorDtype.QtiDurationLt",
            "StatsOperatorDtype.QtiDurationGte",
            "StatsOperatorDtype.QtiSubtract",
            "StatsOperatorDtype.QtiDivide",
            "StatsOperatorDtype.QtiMultiple",
            "StatsOperatorDtype.QtiOrdered",
            CustomOperatorDtype,
            "StatsOperatorDtype.QtiRandom",
            "SubstringDtype",
            EqualRoundedDtype,
            EmptyPrimitiveTypeDtype,
            "StatsOperatorDtype.QtiDelete",
            "StatsOperatorDtype.QtiMatch",
            IndexDtype,
            "StatsOperatorDtype.QtiPower",
            EqualDtype,
            "StatsOperatorDtype.QtiContains",
            "StatsOperatorDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "StatsOperatorDtype.QtiIntegerDivide",
            "StatsOperatorDtype.QtiIntegerModulus",
            "StatsOperatorDtype.QtiIsNull",
            "StatsOperatorDtype.QtiMember",
            "StatsOperatorDtype.QtiProduct",
            "StatsOperatorDtype.QtiRound",
            "StatsOperatorDtype.QtiTruncate",
            FieldValueDtype,
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "StatsOperatorDtype.QtiIntegerToFloat",
            InsideDtype,
            BaseValueDtype,
            PatternMatchDtype,
            "StatsOperatorDtype.QtiMapResponsePoint",
            "StatsOperatorDtype.QtiMapResponse",
            "StringMatchDtype",
            RepeatDtype,
            RoundToDtype,
            "StatsOperatorDtype.QtiLcm",
            "StatsOperatorDtype.QtiGcd",
            "StatsOperatorDtype.QtiMin",
            "StatsOperatorDtype.QtiMax",
            MathConstantDtype,
            "StatsOperatorDtype",
            MathOperatorDtype,
            "StatsOperatorDtype.QtiNumberCorrect",
            "StatsOperatorDtype.QtiNumberIncorrect",
            "StatsOperatorDtype.QtiNumberPresented",
            "StatsOperatorDtype.QtiNumberResponded",
            "StatsOperatorDtype.QtiNumberSelected",
            "StatsOperatorDtype.QtiOutcomeMinimum",
            "StatsOperatorDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("StatsOperatorDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("StatsOperatorDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("StatsOperatorDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("StatsOperatorDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("StatsOperatorDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("StatsOperatorDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("StatsOperatorDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-sum",
                    "type": NumericLogic1ToManyDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("StatsOperatorDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("StatsOperatorDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("StatsOperatorDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("StatsOperatorDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("StatsOperatorDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("StatsOperatorDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("StatsOperatorDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
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
                    "type": ForwardRef("StatsOperatorDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("StatsOperatorDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("StatsOperatorDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("StatsOperatorDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("StatsOperatorDtype.QtiContainerSize"),
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
                    "type": ForwardRef("StatsOperatorDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("StatsOperatorDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("StatsOperatorDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("StatsOperatorDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("StatsOperatorDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("StatsOperatorDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("StatsOperatorDtype.QtiTruncate"),
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
                    "type": ForwardRef("StatsOperatorDtype.QtiIntegerToFloat"),
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
                    "type": ForwardRef(
                        "StatsOperatorDtype.QtiMapResponsePoint"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("StatsOperatorDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
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
                    "type": ForwardRef("StatsOperatorDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("StatsOperatorDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("StatsOperatorDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("StatsOperatorDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-stats-operator",
                    "type": ForwardRef("StatsOperatorDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-math-operator",
                    "type": MathOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("StatsOperatorDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef(
                        "StatsOperatorDtype.QtiNumberIncorrect"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef(
                        "StatsOperatorDtype.QtiNumberPresented"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef(
                        "StatsOperatorDtype.QtiNumberResponded"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("StatsOperatorDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("StatsOperatorDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("StatsOperatorDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    name: Optional[StatsOperatorDtypeName] = field(
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


@dataclass
class StringMatchDtype:
    """The stringMatch operator takes two sub-expressions which must have single
    and a base-type of string.

    The result is a single boolean with a value of true if the two
    strings match a- ccording to the comparison rules defined by the
    attributes below and false if they don't. If either sub-expression
    is NULL then the operator results in NULL.
    """

    class Meta:
        name = "StringMatchDType"

    choice: List[
        Union[
            "StringMatchDtype.QtiAnd",
            "StringMatchDtype.QtiGt",
            "StringMatchDtype.QtiNot",
            "StringMatchDtype.QtiLt",
            "StringMatchDtype.QtiGte",
            "StringMatchDtype.QtiLte",
            "StringMatchDtype.QtiOr",
            NumericLogic1ToManyDtype,
            "StringMatchDtype.QtiDurationLt",
            "StringMatchDtype.QtiDurationGte",
            "StringMatchDtype.QtiSubtract",
            "StringMatchDtype.QtiDivide",
            "StringMatchDtype.QtiMultiple",
            "StringMatchDtype.QtiOrdered",
            CustomOperatorDtype,
            "StringMatchDtype.QtiRandom",
            "SubstringDtype",
            EqualRoundedDtype,
            EmptyPrimitiveTypeDtype,
            "StringMatchDtype.QtiDelete",
            "StringMatchDtype.QtiMatch",
            IndexDtype,
            "StringMatchDtype.QtiPower",
            EqualDtype,
            "StringMatchDtype.QtiContains",
            "StringMatchDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "StringMatchDtype.QtiIntegerDivide",
            "StringMatchDtype.QtiIntegerModulus",
            "StringMatchDtype.QtiIsNull",
            "StringMatchDtype.QtiMember",
            "StringMatchDtype.QtiProduct",
            "StringMatchDtype.QtiRound",
            "StringMatchDtype.QtiTruncate",
            FieldValueDtype,
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "StringMatchDtype.QtiIntegerToFloat",
            InsideDtype,
            BaseValueDtype,
            PatternMatchDtype,
            "StringMatchDtype.QtiMapResponsePoint",
            "StringMatchDtype.QtiMapResponse",
            "StringMatchDtype",
            RepeatDtype,
            RoundToDtype,
            "StringMatchDtype.QtiLcm",
            "StringMatchDtype.QtiGcd",
            "StringMatchDtype.QtiMin",
            "StringMatchDtype.QtiMax",
            MathConstantDtype,
            StatsOperatorDtype,
            MathOperatorDtype,
            "StringMatchDtype.QtiNumberCorrect",
            "StringMatchDtype.QtiNumberIncorrect",
            "StringMatchDtype.QtiNumberPresented",
            "StringMatchDtype.QtiNumberResponded",
            "StringMatchDtype.QtiNumberSelected",
            "StringMatchDtype.QtiOutcomeMinimum",
            "StringMatchDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("StringMatchDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("StringMatchDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("StringMatchDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("StringMatchDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("StringMatchDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("StringMatchDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("StringMatchDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-sum",
                    "type": NumericLogic1ToManyDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("StringMatchDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("StringMatchDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("StringMatchDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("StringMatchDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("StringMatchDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("StringMatchDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("StringMatchDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-equal-rounded",
                    "type": EqualRoundedDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("StringMatchDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("StringMatchDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("StringMatchDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("StringMatchDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("StringMatchDtype.QtiContainerSize"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-correct",
                    "type": CorrectDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-default",
                    "type": DefaultDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-any-n",
                    "type": AnyNdtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-divide",
                    "type": ForwardRef("StringMatchDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("StringMatchDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("StringMatchDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("StringMatchDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("StringMatchDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("StringMatchDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("StringMatchDtype.QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-field-value",
                    "type": FieldValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random-integer",
                    "type": RandomIntegerDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random-float",
                    "type": RandomFloatDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-variable",
                    "type": VariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-test-variables",
                    "type": TestVariablesDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-to-float",
                    "type": ForwardRef("StringMatchDtype.QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-inside",
                    "type": InsideDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-pattern-match",
                    "type": PatternMatchDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef("StringMatchDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("StringMatchDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-string-match",
                    "type": ForwardRef("StringMatchDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-repeat",
                    "type": RepeatDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-round-to",
                    "type": RoundToDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("StringMatchDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("StringMatchDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("StringMatchDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("StringMatchDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-stats-operator",
                    "type": StatsOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-math-operator",
                    "type": MathOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("StringMatchDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("StringMatchDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("StringMatchDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("StringMatchDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("StringMatchDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("StringMatchDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("StringMatchDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
            ),
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    case_sensitive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "case-sensitive",
            "type": "Attribute",
            "required": True,
        },
    )
    substring: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
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


@dataclass
class SubstringDtype:
    """The substring operator takes two sub-expressions which must both have an
    effective base-t- ype of string and single cardinality.

    The result is a single boolean with a value of true if the first
    expression is a substring of the second expression and false if it
    isn't. If either sub-expression is NULL then the result of the
    operator is NULL.
    """

    class Meta:
        name = "SubstringDType"

    choice: List[
        Union[
            "SubstringDtype.QtiAnd",
            "SubstringDtype.QtiGt",
            "SubstringDtype.QtiNot",
            "SubstringDtype.QtiLt",
            "SubstringDtype.QtiGte",
            "SubstringDtype.QtiLte",
            "SubstringDtype.QtiOr",
            NumericLogic1ToManyDtype,
            "SubstringDtype.QtiDurationLt",
            "SubstringDtype.QtiDurationGte",
            "SubstringDtype.QtiSubtract",
            "SubstringDtype.QtiDivide",
            "SubstringDtype.QtiMultiple",
            "SubstringDtype.QtiOrdered",
            CustomOperatorDtype,
            "SubstringDtype.QtiRandom",
            "SubstringDtype",
            EqualRoundedDtype,
            EmptyPrimitiveTypeDtype,
            "SubstringDtype.QtiDelete",
            "SubstringDtype.QtiMatch",
            IndexDtype,
            "SubstringDtype.QtiPower",
            EqualDtype,
            "SubstringDtype.QtiContains",
            "SubstringDtype.QtiContainerSize",
            CorrectDtype,
            DefaultDtype,
            AnyNdtype,
            "SubstringDtype.QtiIntegerDivide",
            "SubstringDtype.QtiIntegerModulus",
            "SubstringDtype.QtiIsNull",
            "SubstringDtype.QtiMember",
            "SubstringDtype.QtiProduct",
            "SubstringDtype.QtiRound",
            "SubstringDtype.QtiTruncate",
            FieldValueDtype,
            RandomIntegerDtype,
            RandomFloatDtype,
            VariableDtype,
            TestVariablesDtype,
            "SubstringDtype.QtiIntegerToFloat",
            InsideDtype,
            BaseValueDtype,
            PatternMatchDtype,
            "SubstringDtype.QtiMapResponsePoint",
            "SubstringDtype.QtiMapResponse",
            StringMatchDtype,
            RepeatDtype,
            RoundToDtype,
            "SubstringDtype.QtiLcm",
            "SubstringDtype.QtiGcd",
            "SubstringDtype.QtiMin",
            "SubstringDtype.QtiMax",
            MathConstantDtype,
            StatsOperatorDtype,
            MathOperatorDtype,
            "SubstringDtype.QtiNumberCorrect",
            "SubstringDtype.QtiNumberIncorrect",
            "SubstringDtype.QtiNumberPresented",
            "SubstringDtype.QtiNumberResponded",
            "SubstringDtype.QtiNumberSelected",
            "SubstringDtype.QtiOutcomeMinimum",
            "SubstringDtype.QtiOutcomeMaximum",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-and",
                    "type": ForwardRef("SubstringDtype.QtiAnd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gt",
                    "type": ForwardRef("SubstringDtype.QtiGt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-not",
                    "type": ForwardRef("SubstringDtype.QtiNot"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lt",
                    "type": ForwardRef("SubstringDtype.QtiLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gte",
                    "type": ForwardRef("SubstringDtype.QtiGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lte",
                    "type": ForwardRef("SubstringDtype.QtiLte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-or",
                    "type": ForwardRef("SubstringDtype.QtiOr"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-sum",
                    "type": NumericLogic1ToManyDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-duration-lt",
                    "type": ForwardRef("SubstringDtype.QtiDurationLt"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-duration-gte",
                    "type": ForwardRef("SubstringDtype.QtiDurationGte"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-subtract",
                    "type": ForwardRef("SubstringDtype.QtiSubtract"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-divide",
                    "type": ForwardRef("SubstringDtype.QtiDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-multiple",
                    "type": ForwardRef("SubstringDtype.QtiMultiple"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-ordered",
                    "type": ForwardRef("SubstringDtype.QtiOrdered"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-custom-operator",
                    "type": CustomOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random",
                    "type": ForwardRef("SubstringDtype.QtiRandom"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-substring",
                    "type": ForwardRef("SubstringDtype"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-equal-rounded",
                    "type": EqualRoundedDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-null",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-delete",
                    "type": ForwardRef("SubstringDtype.QtiDelete"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-match",
                    "type": ForwardRef("SubstringDtype.QtiMatch"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-index",
                    "type": IndexDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-power",
                    "type": ForwardRef("SubstringDtype.QtiPower"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-equal",
                    "type": EqualDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-contains",
                    "type": ForwardRef("SubstringDtype.QtiContains"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-container-size",
                    "type": ForwardRef("SubstringDtype.QtiContainerSize"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-correct",
                    "type": CorrectDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-default",
                    "type": DefaultDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-any-n",
                    "type": AnyNdtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-divide",
                    "type": ForwardRef("SubstringDtype.QtiIntegerDivide"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-modulus",
                    "type": ForwardRef("SubstringDtype.QtiIntegerModulus"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-is-null",
                    "type": ForwardRef("SubstringDtype.QtiIsNull"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-member",
                    "type": ForwardRef("SubstringDtype.QtiMember"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-product",
                    "type": ForwardRef("SubstringDtype.QtiProduct"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-round",
                    "type": ForwardRef("SubstringDtype.QtiRound"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-truncate",
                    "type": ForwardRef("SubstringDtype.QtiTruncate"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-field-value",
                    "type": FieldValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random-integer",
                    "type": RandomIntegerDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-random-float",
                    "type": RandomFloatDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-variable",
                    "type": VariableDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-test-variables",
                    "type": TestVariablesDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-integer-to-float",
                    "type": ForwardRef("SubstringDtype.QtiIntegerToFloat"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-inside",
                    "type": InsideDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-base-value",
                    "type": BaseValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-pattern-match",
                    "type": PatternMatchDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-map-response-point",
                    "type": ForwardRef("SubstringDtype.QtiMapResponsePoint"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-map-response",
                    "type": ForwardRef("SubstringDtype.QtiMapResponse"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-string-match",
                    "type": StringMatchDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-repeat",
                    "type": RepeatDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-round-to",
                    "type": RoundToDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-lcm",
                    "type": ForwardRef("SubstringDtype.QtiLcm"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-gcd",
                    "type": ForwardRef("SubstringDtype.QtiGcd"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-min",
                    "type": ForwardRef("SubstringDtype.QtiMin"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-max",
                    "type": ForwardRef("SubstringDtype.QtiMax"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-math-constant",
                    "type": MathConstantDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-stats-operator",
                    "type": StatsOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-math-operator",
                    "type": MathOperatorDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-correct",
                    "type": ForwardRef("SubstringDtype.QtiNumberCorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-incorrect",
                    "type": ForwardRef("SubstringDtype.QtiNumberIncorrect"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-presented",
                    "type": ForwardRef("SubstringDtype.QtiNumberPresented"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-responded",
                    "type": ForwardRef("SubstringDtype.QtiNumberResponded"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-number-selected",
                    "type": ForwardRef("SubstringDtype.QtiNumberSelected"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-outcome-minimum",
                    "type": ForwardRef("SubstringDtype.QtiOutcomeMinimum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
                {
                    "name": "qti-outcome-maximum",
                    "type": ForwardRef("SubstringDtype.QtiOutcomeMaximum"),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                    "max_occurs": 2,
                },
            ),
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    case_sensitive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "case-sensitive",
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
