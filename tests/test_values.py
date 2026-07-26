"""QTI's value semantics: NULL, coercion, and match."""

import pytest

from pyqti.errors import QtiTypeError, UnsupportedQtiFeature
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.response_declaration_dtype_base_type import (  # noqa: E501
    ResponseDeclarationDtypeBaseType,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.value_dtype_base_type import (
    ValueDtypeBaseType,
)
from pyqti.values import (
    BaseType,
    Cardinality,
    base_type_from,
    cardinality_from,
    cast_value,
    coerce_value,
    is_null,
    qti_match,
)


def test_duplicate_generated_enums_normalise_to_one_type():
    """xsdata generated ``base-type`` seven times; they must all normalise.

    ``ResponseDeclarationDtypeBaseType.FLOAT != ValueDtypeBaseType.FLOAT`` in Python,
    which is why nothing may compare the generated enums directly.
    """
    assert ResponseDeclarationDtypeBaseType.FLOAT != ValueDtypeBaseType.FLOAT

    assert base_type_from(ResponseDeclarationDtypeBaseType.FLOAT) is BaseType.FLOAT
    assert base_type_from(ValueDtypeBaseType.FLOAT) is BaseType.FLOAT
    assert base_type_from("identifier") is BaseType.IDENTIFIER
    assert base_type_from(None) is None

    assert cardinality_from("single") is Cardinality.SINGLE


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (None, True),
        ((), True),
        ([], True),
        ({}, True),
        (0, False),
        (0.0, False),
        (False, False),
        ("", False),
        ("A", False),
    ],
)
def test_is_null(value, expected):
    """NULL is not falsiness. ``0``, ``False`` and ``""`` are real QTI values."""
    assert is_null(value) is expected


@pytest.mark.parametrize(
    ("base_type", "text", "expected"),
    [
        (BaseType.FLOAT, "1", 1.0),
        (BaseType.INTEGER, "42", 42),
        (BaseType.IDENTIFIER, "A", "A"),
        (BaseType.STRING, " hi ", "hi"),
        (BaseType.BOOLEAN, "true", True),
        (BaseType.BOOLEAN, "0", False),
        (BaseType.DURATION, "2.5", 2.5),
        (None, "raw", "raw"),
        (BaseType.FLOAT, None, None),
    ],
)
def test_coerce_value(base_type, text, expected):
    assert coerce_value(base_type, text) == expected


def test_coerce_float_produces_a_real_float():
    """``<qti-value>1</qti-value>`` under a float declaration must not stay ``"1"``."""
    result = coerce_value(BaseType.FLOAT, "1")
    assert type(result) is float


def test_coerce_rejects_bad_text():
    with pytest.raises(QtiTypeError):
        coerce_value(BaseType.FLOAT, "not a number")
    with pytest.raises(QtiTypeError):
        coerce_value(BaseType.BOOLEAN, "maybe")


def test_coerce_refuses_unimplemented_base_types():
    """Structured base types are refused rather than half-implemented."""
    with pytest.raises(UnsupportedQtiFeature):
        coerce_value(BaseType.POINT, "10 20")


def test_cast_value_normalises_int_to_declared_float():
    assert type(cast_value(BaseType.FLOAT, 1)) is float
    assert cast_value(BaseType.INTEGER, 2.0) == 2
    assert cast_value(BaseType.FLOAT, None) is None
    assert cast_value(None, "untouched") == "untouched"


def test_match_returns_null_when_either_operand_is_null():
    """The distinction that makes ``qti-response-if`` skip rather than take else."""
    assert qti_match(None, "A") is None
    assert qti_match("A", None) is None
    assert qti_match(None, None) is None


def test_match_compares_equal_scalars():
    assert qti_match("A", "A") is True
    assert qti_match("A", "B") is False
    assert qti_match(1.0, 1.0) is True


def test_match_rejects_mismatched_base_types():
    """Comparing an identifier to a float is an authoring error, not ``False``."""
    with pytest.raises(QtiTypeError):
        qti_match("1", 1.0)


def test_match_refuses_containers():
    """Multiple-cardinality match is multiset equality; refuse until implemented."""
    with pytest.raises(UnsupportedQtiFeature, match="multiset"):
        qti_match(("A", "B"), ("B", "A"))
