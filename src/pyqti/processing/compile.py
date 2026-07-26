"""Compile generated response-processing models into :mod:`pyqti.processing.ast`.

This module absorbs every awkwardness of the generated code so nothing downstream
has to know about it:

* Operators are dispatched by **element name** (via :mod:`pyqti.qtitree`), never by
  Python class --- ``qti-match`` is a different class in every containing context.
* ``ResponseIfDtype`` has **two** compound fields: ``choice`` holds the single
  boolean condition and ``choice_1`` holds the list of nested rules. Everything here
  reads named fields explicitly via :func:`~pyqti.qtitree.iter_field` so the two can
  never be confused.
* ``LogicPairDtype.choice`` is a positional 2-element list, so a ``qti-match``'s
  operands are simply its two children in order.
* ``BaseValueDtype.value`` is always ``str`` and must be coerced by its declared
  ``base-type``.

Unsupported constructs are rejected *here*, at compile time, with a message naming
the exact element --- rather than surfacing part-way through grading a response.
"""

from __future__ import annotations

from typing import Any

from pyqti.errors import (
    QtiStructureError,
    UnsupportedExpressionError,
    UnsupportedRuleError,
)
from pyqti.processing import ast
from pyqti.processing.templates import load_template
from pyqti.qtitree import iter_children, iter_field
from pyqti.values import base_type_from, coerce_value

# --------------------------------------------------------------------------- #
# Expressions
# --------------------------------------------------------------------------- #


def _operands(node: Any) -> list[ast.Expression]:
    """Compile every child of an operator node, in document order."""
    return [compile_expression(name, child) for name, child in iter_children(node)]


def _exactly(name: str, node: Any, count: int) -> list[ast.Expression]:
    operands = _operands(node)
    if len(operands) != count:
        raise QtiStructureError(
            f"<{name}> takes exactly {count} operand(s), got {len(operands)}"
        )
    return operands


def compile_expression(name: str, node: Any) -> ast.Expression:
    """Compile one QTI expression element, dispatching on its element name."""
    if name == "qti-variable":
        return ast.Variable(identifier=node.identifier)

    if name == "qti-correct":
        return ast.Correct(identifier=node.identifier)

    if name == "qti-base-value":
        base_type = base_type_from(node.base_type)
        return ast.BaseValue(
            base_type=base_type,
            value=coerce_value(base_type, node.value),
        )

    if name == "qti-null":
        return ast.Null()

    if name == "qti-is-null":
        return ast.IsNull(operand=_exactly(name, node, 1)[0])

    if name == "qti-not":
        return ast.Not(operand=_exactly(name, node, 1)[0])

    if name == "qti-match":
        left, right = _exactly(name, node, 2)
        return ast.Match(left=left, right=right)

    if name == "qti-and":
        return ast.And(operands=tuple(_operands(node)))

    if name == "qti-or":
        return ast.Or(operands=tuple(_operands(node)))

    raise UnsupportedExpressionError(f"unsupported expression <{name}>")


# --------------------------------------------------------------------------- #
# Rules
# --------------------------------------------------------------------------- #


def _compile_rules_in(container: Any, field_name: str) -> tuple[ast.Rule, ...]:
    return tuple(
        compile_rule(name, node) for name, node in iter_field(container, field_name)
    )


def _compile_condition(response_if: Any) -> ast.Expression:
    """Compile the single boolean condition in ``ResponseIfDtype.choice``."""
    conditions = list(iter_field(response_if, "choice"))
    if len(conditions) != 1:
        raise QtiStructureError(
            f"<qti-response-if> needs exactly one condition expression, "
            f"got {len(conditions)}"
        )
    name, node = conditions[0]
    return compile_expression(name, node)


def _compile_branch(response_if: Any) -> ast.ResponseBranch:
    return ast.ResponseBranch(
        condition=_compile_condition(response_if),
        rules=_compile_rules_in(response_if, "choice_1"),
    )


def _compile_response_condition(node: Any) -> ast.ResponseCondition:
    if node.qti_response_if is None:
        raise QtiStructureError("<qti-response-condition> has no <qti-response-if>")

    return ast.ResponseCondition(
        if_branch=_compile_branch(node.qti_response_if),
        else_if_branches=tuple(
            _compile_branch(branch) for branch in node.qti_response_else_if
        ),
        else_rules=(
            _compile_rules_in(node.qti_response_else, "choice")
            if node.qti_response_else is not None
            else ()
        ),
    )


def _compile_set_value(node: Any) -> ast.SetOutcomeValue:
    values = list(iter_field(node, "choice"))
    if len(values) != 1:
        raise QtiStructureError(
            f"<qti-set-outcome-value identifier={node.identifier!r}> needs exactly "
            f"one expression, got {len(values)}"
        )
    name, child = values[0]
    return ast.SetOutcomeValue(
        identifier=node.identifier,
        expression=compile_expression(name, child),
    )


def compile_rule(name: str, node: Any) -> ast.Rule:
    """Compile one QTI response rule, dispatching on its element name."""
    if name == "qti-set-outcome-value":
        return _compile_set_value(node)

    if name == "qti-exit-response":
        return ast.ExitResponse()

    if name == "qti-response-condition":
        return _compile_response_condition(node)

    raise UnsupportedRuleError(f"unsupported response rule <{name}>")


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #


def compile_response_processing(model: Any) -> ast.ResponseProcessing:
    """Compile a ``qti-response-processing`` model, resolving a template if needed.

    An item carrying both ``@template`` and inline rules is malformed; pyqti says so
    rather than silently preferring one.
    """
    if model is None:
        return ast.ResponseProcessing(rules=())

    template = getattr(model, "template", None)
    template_location = getattr(model, "template_location", None)
    inline = list(model.choice or [])

    if template_location and not template:
        raise UnsupportedRuleError(
            "qti-response-processing/@template-location is not implemented yet; "
            "only @template is resolved"
        )

    if template:
        if inline:
            raise QtiStructureError(
                "qti-response-processing has both @template and inline rules"
            )
        return compile_response_processing(load_template(template))

    return ast.ResponseProcessing(rules=_compile_rules_in(model, "choice"))
