"""An item session: variable state plus the attempt lifecycle.

Variable initialisation is **asymmetric**, and both halves are normative. Quoting the
XSD annotations carried in the generated models:

* ``OutcomeDeclarationDType`` --- "If no default value is given in the declaration
  then the outcome variable is initialized to NULL unless the outcome is of a numeric
  type (integer or float) in which case it is initialized to 0."
* ``ResponseDeclarationDType`` --- response values are "always initialized to NULL
  (no value) regardless of whether or not a default value is given in the
  declaration."

A single generic ``init_variable()`` for both kinds gets this wrong, so the two paths
are kept separate.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pyqti.errors import QtiStructureError
from pyqti.item import ItemDefinition
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0 import QtiAssessmentItem
from pyqti.processing import ast
from pyqti.processing.compile import compile_response_processing
from pyqti.processing.evaluate import run_response_processing
from pyqti.values import BaseType, Cardinality, cast_value, is_null

#: QTI's built-in item-level variables.
COMPLETION_STATUS = "completionStatus"
NUM_ATTEMPTS = "numAttempts"
DURATION = "duration"

NOT_ATTEMPTED = "not_attempted"
COMPLETED = "completed"
INCOMPLETE = "incomplete"


@dataclass
class ResponseValidity:
    """The outcome of checking submitted responses against the interactions.

    Deliberately *reported* rather than enforced. Response validity is a delivery-
    engine concern (``qti-item-session-control/@validate-responses``), not response
    processing, and response processing must stay runnable on invalid responses.
    """

    valid: bool = True
    errors: list[str] = field(default_factory=list)

    def add(self, message: str) -> None:
        self.valid = False
        self.errors.append(message)


class ItemSession:
    """Holds the runtime state of one candidate's interaction with one item."""

    def __init__(self, item: ItemDefinition | QtiAssessmentItem):
        self.item = (
            item
            if isinstance(item, ItemDefinition)
            else ItemDefinition.from_model(item)
        )

        # Compiled once. Compilation resolves the response-processing template and
        # rejects unsupported constructs, so problems surface at construction time.
        self.processing: ast.ResponseProcessing = compile_response_processing(
            self.item.response_processing
        )

        self.responses: dict[str, Any] = {}
        self.outcomes: dict[str, Any] = {}
        self.builtins: dict[str, Any] = {}

        self.reset()

    # ------------------------------------------------------------------ #
    # Initialisation
    # ------------------------------------------------------------------ #

    def reset(self) -> None:
        """Return the session to its pre-attempt state."""
        self.responses = {
            identifier: None for identifier in self.item.response_declarations
        }
        self.reset_outcomes()
        self.builtins = {
            COMPLETION_STATUS: NOT_ATTEMPTED,
            NUM_ATTEMPTS: 0,
            DURATION: 0.0,
        }

    def reset_outcomes(self) -> None:
        """Re-initialise every outcome variable from its declaration.

        Called before each response-processing run. The QTI specification states this
        reset normatively for *test-level* outcome processing ("The values of the
        test's outcome variables are always reset to their defaults prior to carrying
        out the instructions described by the outcomeRules") but says nothing
        equivalent for item-level response processing. QTIWorks resets item outcomes
        by analogy, and pyqti follows it.

        This is invisible on a single attempt and is the difference between right and
        wrong on the second one, so the ambiguity is recorded rather than hidden.
        """
        self.outcomes = {
            identifier: declaration.initial_value
            for identifier, declaration in self.item.outcome_declarations.items()
        }

    # ------------------------------------------------------------------ #
    # SessionState protocol (used by pyqti.processing.evaluate)
    # ------------------------------------------------------------------ #

    def get_variable(self, identifier: str) -> Any:
        if identifier in self.responses:
            return self.responses[identifier]
        if identifier in self.outcomes:
            return self.outcomes[identifier]
        if identifier in self.builtins:
            return self.builtins[identifier]
        raise QtiStructureError(
            f"<qti-variable> references undeclared variable {identifier!r}"
        )

    def set_outcome(self, identifier: str, value: Any) -> None:
        if identifier not in self.outcomes:
            raise QtiStructureError(
                f"<qti-set-outcome-value> targets undeclared outcome {identifier!r}"
            )
        self.outcomes[identifier] = value

    def correct_response(self, identifier: str) -> Any:
        declaration = self.item.response_declarations.get(identifier)
        if declaration is None:
            raise QtiStructureError(
                f"<qti-correct> references undeclared response {identifier!r}"
            )
        return declaration.correct_value

    def outcome_base_type(self, identifier: str) -> BaseType | None:
        declaration = self.item.outcome_declarations.get(identifier)
        return declaration.base_type if declaration else None

    # ------------------------------------------------------------------ #
    # Attempt lifecycle
    # ------------------------------------------------------------------ #

    def validate_responses(self, responses: dict[str, Any]) -> ResponseValidity:
        """Check submitted responses against the item's interactions.

        Reports rather than raises --- see :class:`ResponseValidity`.
        """
        validity = ResponseValidity()

        for identifier in responses:
            if identifier not in self.item.response_declarations:
                validity.add(f"no qti-response-declaration for {identifier!r}")

        for interaction in self.item.interactions:
            value = responses.get(interaction.response_identifier)
            selected = _selection_size(value)

            if selected > interaction.max_choices > 0:
                validity.add(
                    f"{interaction.response_identifier!r}: {selected} choices "
                    f"selected but max-choices is {interaction.max_choices}"
                )
            if selected < interaction.min_choices:
                validity.add(
                    f"{interaction.response_identifier!r}: {selected} choices "
                    f"selected but min-choices is {interaction.min_choices}"
                )

            for choice in _as_selection(value):
                if choice not in interaction.choice_identifiers:
                    validity.add(
                        f"{interaction.response_identifier!r}: {choice!r} is not "
                        "one of the declared choices"
                    )

        return validity

    def set_responses(self, responses: dict[str, Any]) -> None:
        """Bind candidate responses, coercing each to its declared base-type."""
        for identifier, raw in responses.items():
            declaration = self.item.response_declarations.get(identifier)
            if declaration is None:
                raise QtiStructureError(
                    f"no qti-response-declaration for {identifier!r}"
                )
            if declaration.cardinality is Cardinality.SINGLE:
                self.responses[identifier] = cast_value(declaration.base_type, raw)
            else:
                self.responses[identifier] = tuple(
                    cast_value(declaration.base_type, choice)
                    for choice in _as_selection(raw)
                )

    def process_responses(self) -> dict[str, Any]:
        """Run response processing and return the resulting outcomes."""
        self.reset_outcomes()
        run_response_processing(self.processing, self)
        return dict(self.outcomes)

    def submit(self, responses: dict[str, Any]) -> dict[str, Any]:
        """Bind responses, run response processing, and return the outcomes.

        The whole grading path in one call. ``validate_responses`` is intentionally
        *not* called here: invalid responses still grade (an undeclared choice simply
        fails to match), and enforcing validity is the delivery engine's decision.
        """
        self.builtins[NUM_ATTEMPTS] = self.builtins.get(NUM_ATTEMPTS, 0) + 1
        self.set_responses(responses)
        outcomes = self.process_responses()
        self.builtins[COMPLETION_STATUS] = (
            INCOMPLETE
            if any(is_null(value) for value in self.responses.values())
            else COMPLETED
        )
        return outcomes

    @property
    def completion_status(self) -> str:
        return self.builtins[COMPLETION_STATUS]

    @property
    def num_attempts(self) -> int:
        return self.builtins[NUM_ATTEMPTS]


def _as_selection(value: Any) -> tuple[Any, ...]:
    if value is None:
        return ()
    if isinstance(value, list | tuple | set | frozenset):
        return tuple(value)
    return (value,)


def _selection_size(value: Any) -> int:
    return len(_as_selection(value))


def grade(
    item: ItemDefinition | QtiAssessmentItem, responses: dict[str, Any]
) -> dict[str, Any]:
    """Convenience one-shot: build a session, submit ``responses``, return outcomes."""
    return ItemSession(item).submit(responses)
