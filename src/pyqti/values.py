"""QTI's runtime value model: base types, cardinality, NULL, and comparison.

Two things force this module to exist rather than using the generated enums directly.

First, xsdata generated the ``base-type`` enumeration **seven** times and
``cardinality`` **four** times --- once per owning complexType
(``ResponseDeclarationDtypeBaseType``, ``OutcomeDeclarationDtypeBaseType``,
``ValueDtypeBaseType``, ``BaseValueDtypeBaseType``, ...). They are distinct Python
classes, so ``response.base_type == outcome.base_type`` is ``False`` even when both
mean ``identifier``. Everything must be normalised through :func:`base_type_from`.

Second, ``ValueDtype.value`` and ``BaseValueDtype.value`` are **always** ``str`` ---
xsdata never coerces them by base-type. ``<qti-base-value base-type="float">1
</qti-base-value>`` arrives as ``"1"``, so without :func:`coerce_value` a ``SCORE``
of ``"1"`` would serialise to JSON as a string and any arithmetic on it would break.

A NULL value is represented as ``None`` for single cardinality, and as an empty
container for the others --- QTI treats an empty container as NULL, not as an empty
set.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pyqti.errors import QtiTypeError, UnsupportedQtiFeature


class BaseType(StrEnum):
    """The QTI base-type enumeration, normalised into one Python enum."""

    BOOLEAN = "boolean"
    DIRECTED_PAIR = "directedPair"
    DURATION = "duration"
    FILE = "file"
    FLOAT = "float"
    IDENTIFIER = "identifier"
    INTEGER = "integer"
    PAIR = "pair"
    POINT = "point"
    STRING = "string"
    URI = "uri"


class Cardinality(StrEnum):
    """The QTI cardinality enumeration, normalised into one Python enum."""

    MULTIPLE = "multiple"
    ORDERED = "ordered"
    RECORD = "record"
    SINGLE = "single"


#: Base types whose QTI default initial value is 0 rather than NULL.
NUMERIC_BASE_TYPES = frozenset({BaseType.FLOAT, BaseType.INTEGER})

#: Base types this slice can coerce. The rest are structured (pairs, points,
#: files) and are refused rather than half-implemented.
_SCALAR_COERCERS: dict[BaseType, Any] = {
    BaseType.IDENTIFIER: str,
    BaseType.STRING: str,
    BaseType.URI: str,
    BaseType.FLOAT: float,
    BaseType.INTEGER: int,
    BaseType.DURATION: float,
}


def base_type_from(value: Any) -> BaseType | None:
    """Normalise a generated ``*BaseType`` enum (or a str) to :class:`BaseType`."""
    if value is None:
        return None
    if isinstance(value, BaseType):
        return value
    raw = getattr(value, "value", value)
    return BaseType(raw)


def cardinality_from(value: Any) -> Cardinality:
    """Normalise a generated ``*Cardinality`` enum (or str) to :class:`Cardinality`."""
    if isinstance(value, Cardinality):
        return value
    raw = getattr(value, "value", value)
    return Cardinality(raw)


def is_null(value: Any) -> bool:
    """QTI NULL test: ``None``, or an empty container.

    Note that ``False``, ``0`` and ``""`` are *not* NULL, which is why this exists
    instead of a plain truthiness check.
    """
    if value is None:
        return True
    if isinstance(value, list | tuple | set | frozenset | dict):
        return len(value) == 0
    return False


def coerce_value(base_type: BaseType | None, text: str | None) -> Any:
    """Convert QTI value text to a typed Python scalar.

    ``None`` (NULL) passes through. An untyped value is left as text, which matches
    QTI's treatment of a value with no declared base-type.
    """
    if text is None:
        return None
    if base_type is None:
        return text

    if base_type is BaseType.BOOLEAN:
        stripped = text.strip().lower()
        if stripped in ("true", "1"):
            return True
        if stripped in ("false", "0"):
            return False
        raise QtiTypeError(f"{text!r} is not a valid QTI boolean")

    coercer = _SCALAR_COERCERS.get(base_type)
    if coercer is None:
        raise UnsupportedQtiFeature(
            f"base-type {base_type.value!r} is not implemented yet"
        )

    try:
        return coercer(text.strip())
    except ValueError as exc:
        raise QtiTypeError(f"{text!r} is not a valid QTI {base_type.value}") from exc


def cast_value(base_type: BaseType | None, value: Any) -> Any:
    """Coerce an already-typed Python value to a declared base-type.

    Used when assigning to an outcome variable: an expression may produce an ``int``
    where the declaration says ``float``, and a ``SCORE`` of ``1`` rather than ``1.0``
    would serialise differently and behave differently under later arithmetic.

    Distinct from :func:`coerce_value`, which parses value *text* from the document.
    """
    if value is None or base_type is None:
        return value
    if isinstance(value, list | tuple | set | frozenset | dict):
        return value

    if base_type is BaseType.BOOLEAN:
        return bool(value)
    if base_type in (BaseType.FLOAT, BaseType.DURATION):
        return float(value)
    if base_type is BaseType.INTEGER:
        return int(value)
    if base_type in (BaseType.IDENTIFIER, BaseType.STRING, BaseType.URI):
        return value if isinstance(value, str) else str(value)
    return value


def qti_match(left: Any, right: Any) -> bool | None:
    """QTI ``match``: equality with NULL propagation and base-type checking.

    Returns ``None`` (NULL) if either operand is NULL --- *not* ``False``. This
    distinction is load-bearing: a NULL condition makes ``qti-response-if`` skip its
    branch, and three-valued logic in ``qti-and``/``qti-or`` depends on it.

    This is deliberately the only place equality is decided. Multiple cardinality
    ``match`` is *multiset* equality in QTI, so if ``a == b`` on lists were written
    inline at call sites, order-sensitive comparison would ship silently the moment
    multi-answer support arrives. Containers raise here instead.
    """
    if is_null(left) or is_null(right):
        return None

    if isinstance(left, list | tuple | set | frozenset) or isinstance(
        right, list | tuple | set | frozenset
    ):
        raise UnsupportedQtiFeature(
            "match on multiple/ordered cardinality is not implemented yet "
            "(it is multiset equality, not list equality)"
        )

    # QTI requires both operands to share a base-type. Comparing an identifier to a
    # float is an authoring error, so surface it rather than quietly returning False.
    if type(left) is not type(right):
        raise QtiTypeError(
            f"cannot match {type(left).__name__} against {type(right).__name__}"
        )

    return left == right
