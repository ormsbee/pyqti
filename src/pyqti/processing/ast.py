"""A small hand-written AST for QTI response processing.

**Why this layer exists.** The generated models cannot be dispatched on by class
(see ``pyqti.qtitree``), so something has to translate them into a stable form.
Doing that as an explicit compile step, rather than threading name recovery through
every evaluator function, buys three things: the evaluator is pure and has no
xsdata dependency; unsupported content is rejected at compile time with a useful
message instead of failing deep inside evaluation; and tests can build an AST
directly instead of constructing ``ResponseIfDtype.QtiMatch`` by hand.

**When to reconsider.** Direct interpretation of the generated tree also works and
is not much larger --- a spike confirmed it. Revisit this layer if any of these
become true, and not otherwise:

1. A QTI 2.x front end is added and should share this back end.
2. Static analysis of response processing is wanted ("which outcomes can this item
   set?", "is this equivalent to match_correct?").
3. Reparsing templates per grade becomes a measurable bottleneck.

The node set is deliberately tiny. Everything QTI defines that is not here raises
:class:`~pyqti.errors.UnsupportedExpressionError` or
:class:`~pyqti.errors.UnsupportedRuleError` during compilation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from pyqti.values import BaseType

# --------------------------------------------------------------------------- #
# Expressions
# --------------------------------------------------------------------------- #


class Expression:
    """Base class for anything that evaluates to a QTI value."""

    __slots__ = ()


@dataclass(frozen=True, slots=True)
class Variable(Expression):
    """``qti-variable``: the current value of a response/outcome/built-in variable."""

    identifier: str


@dataclass(frozen=True, slots=True)
class Correct(Expression):
    """``qti-correct``: the declared correct response for a response variable.

    Yields NULL when the declaration has no ``qti-correct-response``.
    """

    identifier: str


@dataclass(frozen=True, slots=True)
class BaseValue(Expression):
    """``qti-base-value``: a literal, already coerced to its declared base-type."""

    base_type: BaseType | None
    value: Any


@dataclass(frozen=True, slots=True)
class Null(Expression):
    """``qti-null``: the NULL value."""


@dataclass(frozen=True, slots=True)
class IsNull(Expression):
    """``qti-is-null``: true when the operand is NULL.

    Included even though this slice does not need it: it is the entire if-branch of
    the ``map_response`` template, so having it here makes MAP_RESPONSE mostly
    mechanical later.
    """

    operand: Expression


@dataclass(frozen=True, slots=True)
class Match(Expression):
    """``qti-match``: equality, with NULL propagation."""

    left: Expression
    right: Expression


@dataclass(frozen=True, slots=True)
class Not(Expression):
    """``qti-not``: three-valued negation (NULL stays NULL)."""

    operand: Expression


@dataclass(frozen=True, slots=True)
class And(Expression):
    """``qti-and``: three-valued conjunction."""

    operands: tuple[Expression, ...]


@dataclass(frozen=True, slots=True)
class Or(Expression):
    """``qti-or``: three-valued disjunction."""

    operands: tuple[Expression, ...]


# --------------------------------------------------------------------------- #
# Rules
# --------------------------------------------------------------------------- #


class Rule:
    """Base class for anything that mutates session state."""

    __slots__ = ()


@dataclass(frozen=True, slots=True)
class SetOutcomeValue(Rule):
    """``qti-set-outcome-value``: assign an expression's value to an outcome."""

    identifier: str
    expression: Expression


@dataclass(frozen=True, slots=True)
class ExitResponse(Rule):
    """``qti-exit-response``: stop response processing immediately."""


@dataclass(frozen=True, slots=True)
class ResponseBranch:
    """One ``qti-response-if`` / ``qti-response-else-if`` clause."""

    condition: Expression
    rules: tuple[Rule, ...]


@dataclass(frozen=True, slots=True)
class ResponseCondition(Rule):
    """``qti-response-condition``: if / else-if* / else."""

    if_branch: ResponseBranch
    else_if_branches: tuple[ResponseBranch, ...] = ()
    else_rules: tuple[Rule, ...] = ()


@dataclass(frozen=True, slots=True)
class ResponseProcessing:
    """A compiled ``qti-response-processing`` block."""

    rules: tuple[Rule, ...]
