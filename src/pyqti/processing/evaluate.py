"""Evaluate compiled response processing against an item session.

This module is pure: it knows about :mod:`pyqti.processing.ast` and
:mod:`pyqti.values`, and nothing about xsdata or the generated models.

The one rule worth reading twice is how conditions are tested. QTI's logic is
**three-valued** --- an expression can be true, false, or NULL --- and the XSD
annotation on ``ResponseIfDType`` is explicit that a branch is skipped "(including
if the expression is NULL)". So every condition is compared with ``is True``, never
for truthiness. An unanswered response makes ``qti-match`` yield NULL rather than
``False``, and with plain truthiness that difference is invisible today but wrong the
moment ``qti-and``/``qti-or`` are involved.
"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from pyqti.processing import ast
from pyqti.values import BaseType, cast_value, is_null, qti_match


@runtime_checkable
class SessionState(Protocol):
    """What the evaluator needs from a session.

    Declared structurally so :mod:`pyqti.session` can import this module rather than
    the other way round.
    """

    def get_variable(self, identifier: str) -> Any: ...

    def set_outcome(self, identifier: str, value: Any) -> None: ...

    def correct_response(self, identifier: str) -> Any: ...

    def outcome_base_type(self, identifier: str) -> BaseType | None: ...


class _ExitResponse(Exception):
    """Internal control flow for ``qti-exit-response``."""


def evaluate(expression: ast.Expression, state: SessionState) -> Any:
    """Evaluate a compiled expression, returning a Python value (``None`` is NULL)."""
    match expression:
        case ast.Variable(identifier=identifier):
            return state.get_variable(identifier)

        case ast.Correct(identifier=identifier):
            return state.correct_response(identifier)

        case ast.BaseValue(value=value):
            return value

        case ast.Null():
            return None

        case ast.IsNull(operand=operand):
            # is-null is total: it is never itself NULL.
            return is_null(evaluate(operand, state))

        case ast.Match(left=left, right=right):
            return qti_match(evaluate(left, state), evaluate(right, state))

        case ast.Not(operand=operand):
            value = evaluate(operand, state)
            return None if value is None else not value

        case ast.And(operands=operands):
            return _and(evaluate(operand, state) for operand in operands)

        case ast.Or(operands=operands):
            return _or(evaluate(operand, state) for operand in operands)

    raise AssertionError(f"unhandled expression node {type(expression).__name__}")


def _and(values: Any) -> bool | None:
    """Three-valued conjunction: any False wins, then any NULL, else True."""
    saw_null = False
    for value in values:
        if value is None:
            saw_null = True
        elif not value:
            return False
    return None if saw_null else True


def _or(values: Any) -> bool | None:
    """Three-valued disjunction: any True wins, then any NULL, else False."""
    saw_null = False
    for value in values:
        if value is None:
            saw_null = True
        elif value:
            return True
    return None if saw_null else False


def _execute_rule(rule: ast.Rule, state: SessionState) -> None:
    match rule:
        case ast.SetOutcomeValue(identifier=identifier, expression=expression):
            value = evaluate(expression, state)
            state.set_outcome(
                identifier, cast_value(state.outcome_base_type(identifier), value)
            )

        case ast.ExitResponse():
            raise _ExitResponse

        case ast.ResponseCondition(
            if_branch=if_branch,
            else_if_branches=else_if_branches,
            else_rules=else_rules,
        ):
            for branch in (if_branch, *else_if_branches):
                # `is True` is deliberate: a NULL condition skips the branch.
                if evaluate(branch.condition, state) is True:
                    execute(branch.rules, state)
                    return
            execute(else_rules, state)

        case _:
            raise AssertionError(f"unhandled rule node {type(rule).__name__}")


def execute(rules: tuple[ast.Rule, ...], state: SessionState) -> None:
    """Run a sequence of rules in order.

    Propagates ``qti-exit-response`` so that :func:`run_response_processing` can stop
    the whole block, not just the innermost branch.
    """
    for rule in rules:
        _execute_rule(rule, state)


def run_response_processing(
    processing: ast.ResponseProcessing, state: SessionState
) -> None:
    """Run a whole compiled response-processing block against ``state``."""
    try:
        execute(processing.rules, state)
    except _ExitResponse:
        pass
