"""A hand-written view of an assessment item.

The generated models are faithful to the XSD but awkward to work with: attributes
arrive as one of seven duplicate enum classes, ``class`` is called ``class_value``,
and required-ness is encoded as "the field has no default". This module reads a
parsed ``QtiAssessmentItem`` once and produces plain frozen dataclasses that the
session, the compiler and the JSON layer can use without knowing any of that.

The raw model is kept on :attr:`ItemDefinition.model` --- the renderer needs the real
``qti-item-body`` to feed xsdata's event stream, and the compiler needs the real
``qti-response-processing``.
"""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from dataclasses import dataclass
from typing import Any

from pyqti.errors import QtiStructureError
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0 import QtiAssessmentItem
from pyqti.qtitree import iter_children
from pyqti.values import (
    NUMERIC_BASE_TYPES,
    BaseType,
    Cardinality,
    base_type_from,
    cardinality_from,
    coerce_value,
)


def _values_of(container: Any, base_type: BaseType | None) -> tuple[Any, ...]:
    """Coerce the ``qti-value`` children of a correct-response/default-value block.

    A ``qti-value`` may carry its own ``base-type``, which wins over the
    declaration's when present.
    """
    if container is None:
        return ()
    out = []
    for value_element in container.qti_value:
        own = base_type_from(value_element.base_type)
        out.append(coerce_value(own or base_type, value_element.value))
    return tuple(out)


@dataclass(frozen=True, slots=True)
class ResponseDeclaration:
    identifier: str
    cardinality: Cardinality
    base_type: BaseType | None
    correct_response: tuple[Any, ...]
    has_correct_response: bool

    @property
    def correct_value(self) -> Any:
        """The correct response as a single value, or NULL.

        Per QTI, ``qti-correct`` yields NULL when the declaration has no
        ``qti-correct-response`` --- it does not yield an empty container.
        """
        if not self.has_correct_response:
            return None
        if self.cardinality is Cardinality.SINGLE:
            return self.correct_response[0] if self.correct_response else None
        return self.correct_response

    @classmethod
    def from_model(cls, model: Any) -> ResponseDeclaration:
        base_type = base_type_from(model.base_type)
        correct = model.qti_correct_response
        return cls(
            identifier=model.identifier,
            cardinality=cardinality_from(model.cardinality),
            base_type=base_type,
            correct_response=_values_of(correct, base_type),
            has_correct_response=correct is not None,
        )


@dataclass(frozen=True, slots=True)
class OutcomeDeclaration:
    identifier: str
    cardinality: Cardinality
    base_type: BaseType | None
    default_value: tuple[Any, ...]
    has_default_value: bool

    @property
    def initial_value(self) -> Any:
        """The value this outcome starts each attempt with.

        Normative, quoted from the XSD annotation on ``OutcomeDeclarationDType``:
        "If no default value is given in the declaration then the outcome variable
        is initialized to NULL unless the outcome is of a numeric type (integer or
        float) in which case it is initialized to 0."
        """
        if self.has_default_value:
            if self.cardinality is Cardinality.SINGLE:
                return self.default_value[0] if self.default_value else None
            return self.default_value
        if (
            self.cardinality is Cardinality.SINGLE
            and self.base_type in NUMERIC_BASE_TYPES
        ):
            return 0.0 if self.base_type is BaseType.FLOAT else 0
        return None

    @classmethod
    def from_model(cls, model: Any) -> OutcomeDeclaration:
        base_type = base_type_from(model.base_type)
        default = model.qti_default_value
        return cls(
            identifier=model.identifier,
            cardinality=cardinality_from(model.cardinality),
            base_type=base_type,
            default_value=_values_of(default, base_type),
            has_default_value=default is not None,
        )


@dataclass(frozen=True, slots=True)
class ChoiceInteraction:
    """A ``qti-choice-interaction`` reduced to what rendering and grading need."""

    response_identifier: str
    max_choices: int
    min_choices: int
    shuffle: bool
    orientation: str
    choice_identifiers: tuple[str, ...]

    @property
    def is_single_answer(self) -> bool:
        return self.max_choices == 1

    @classmethod
    def from_model(cls, model: Any) -> ChoiceInteraction:
        return cls(
            response_identifier=model.response_identifier,
            max_choices=model.max_choices,
            min_choices=model.min_choices,
            shuffle=bool(model.shuffle),
            orientation=getattr(model.orientation, "value", str(model.orientation)),
            choice_identifiers=tuple(
                child.identifier
                for name, child in iter_children(model)
                if name == "qti-simple-choice"
            ),
        )


def _walk_body(node: Any) -> Iterator[tuple[str, Any]]:
    """Depth-first walk of an item body, yielding every element.

    Interactions are not required to be direct children of ``qti-item-body`` ---
    they can be nested inside a ``div``, ``section`` and so on.
    """
    for name, child in iter_children(node):
        yield name, child
        yield from _walk_body(child)


@dataclass(frozen=True, slots=True)
class ItemDefinition:
    identifier: str
    title: str
    response_declarations: Mapping[str, ResponseDeclaration]
    outcome_declarations: Mapping[str, OutcomeDeclaration]
    interactions: tuple[ChoiceInteraction, ...]
    model: QtiAssessmentItem

    @property
    def item_body(self) -> Any | None:
        return self.model.qti_item_body

    @property
    def response_processing(self) -> Any | None:
        return self.model.qti_response_processing

    def interaction_for(self, response_identifier: str) -> ChoiceInteraction | None:
        for interaction in self.interactions:
            if interaction.response_identifier == response_identifier:
                return interaction
        return None

    @classmethod
    def from_model(cls, model: QtiAssessmentItem) -> ItemDefinition:
        responses = {
            declaration.identifier: ResponseDeclaration.from_model(declaration)
            for declaration in model.qti_response_declaration
        }
        outcomes = {
            declaration.identifier: OutcomeDeclaration.from_model(declaration)
            for declaration in model.qti_outcome_declaration
        }

        interactions: list[ChoiceInteraction] = []
        if model.qti_item_body is not None:
            for name, node in _walk_body(model.qti_item_body):
                if name == "qti-choice-interaction":
                    interactions.append(ChoiceInteraction.from_model(node))

        # An interaction bound to a response variable that was never declared is a
        # structural error: nothing downstream could grade it.
        for interaction in interactions:
            if interaction.response_identifier not in responses:
                raise QtiStructureError(
                    f"{interaction.response_identifier!r} is bound by a "
                    "qti-choice-interaction but has no qti-response-declaration"
                )

        return cls(
            identifier=model.identifier,
            title=model.title,
            response_declarations=responses,
            outcome_declarations=outcomes,
            interactions=tuple(interactions),
            model=model,
        )


def first_choice_interaction(item: ItemDefinition) -> ChoiceInteraction:
    """Convenience for the single-interaction case, with an explicit error otherwise."""
    if not item.interactions:
        raise QtiStructureError(f"item {item.identifier!r} has no choice interaction")
    return item.interactions[0]


__all__ = [
    "ChoiceInteraction",
    "ItemDefinition",
    "OutcomeDeclaration",
    "ResponseDeclaration",
    "first_choice_interaction",
]
