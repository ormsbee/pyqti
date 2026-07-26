"""Deriving a presentation-safe copy of an assessment item.

**Why this exists.** pyqti no longer renders items; Citolab's web components do,
and they fetch **QTI XML** from a URL. But QTI XML carries the answer:
``qti-correct-response``, ``qti-mapping``, inline ``qti-response-processing`` and
feedback bodies all live in the same document. Serving an item as authored hands the
answer to anyone who opens devtools. For high-stakes delivery the server must keep
the authoritative item to itself and publish only a redacted view.

**Allowlist, not denylist.** Every field of ``QtiAssessmentItem`` is explicitly
classified below, and :func:`redact_for_delivery` raises if it meets a field that is
not. A denylist would only remove the leaks we happened to think of; classifying all
of them means a future model regeneration that adds a field breaks a test instead of
quietly publishing it to candidates. The same principle applies inside the item body
via :data:`STRIP_FROM_BODY`.

**What is deliberately kept.** Two risky-looking fields survive, because removing
them would damage the item rather than protect it --- see :data:`KEEP_WITH_REVIEW`.

This module is one control in a layered scheme, not the whole thing. The others live
outside pyqti: never registering Citolab's response-processing components, accepting
only responses (never outcomes) from the client, binding attempts server-side, and
withholding scores until release.
"""

from __future__ import annotations

import copy
from dataclasses import fields
from typing import Any

from xsdata.formats.dataclass.models.generics import AnyElement

from pyqti.errors import UnsupportedContentError
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0 import QtiAssessmentItem
from pyqti.qtitree import attribute_vars, iter_nodes, prune
from pyqti.serialization import to_qti_xml

#: Item fields that are safe to publish untouched.
KEEP: frozenset[str] = frozenset(
    {
        "identifier",
        "title",
        "time_dependent",
        "label",
        "lang",
        "adaptive",
        "qti_item_body",  # published, but pruned by STRIP_FROM_BODY
        "qti_response_declaration",  # published, but stripped by REDACT_ON_RESPONSE
    }
)

#: Item fields reset to empty before publishing.
#:
#: ``any_attributes`` is the ``##any`` attribute wildcard: it passes arbitrary
#: author-supplied attributes straight through the serializer, so it cannot be
#: audited and is cleared. (It is also where ``xsi:schemaLocation`` ends up.)
CLEAR: frozenset[str] = frozenset(
    {
        "qti_response_processing",
        "qti_outcome_declaration",
        "qti_modal_feedback",
        "qti_template_declaration",
        "qti_template_processing",
        "qti_context_declaration",
        "qti_stylesheet",
        "qti_companion_materials_info",
        "tool_name",
        "tool_version",
        "any_attributes",
    }
)

#: Item fields kept on purpose despite carrying some risk.
#:
#: ``qti_assessment_stimulus_ref`` points at the shared stimulus --- a reading
#: passage, say. Strip it and the candidate cannot answer the question at all. The
#: reference is kept; the stimulus it names must itself be served through this same
#: redaction path.
#:
#: ``qti_catalog_info`` carries accessibility alternatives (alt text, translations,
#: signed content). Removing it strips accommodations from the candidates who depend
#: on them, which in a high-stakes exam is a worse failure than the marginal leak it
#: would prevent. Whether an author has hidden something in catalog content is an
#: authoring-review question, not one redaction should answer by deletion.
KEEP_WITH_REVIEW: frozenset[str] = frozenset(
    {
        "qti_assessment_stimulus_ref",
        "qti_catalog_info",
    }
)

#: Response-declaration fields cleared before publishing.
#:
#: ``qti_default_value`` goes too. pyqti never uses it --- QTI initialises response
#: variables to NULL regardless --- so it is pure leak surface.
REDACT_ON_RESPONSE: tuple[str, ...] = (
    "qti_correct_response",
    "qti_mapping",
    "qti_area_mapping",
    "qti_default_value",
)

#: Elements removed from the item body wherever they appear.
#:
#: Feedback is conditional on outcome values and therefore answer-revealing.
#: Template blocks are conditional on template variables, which determine the answer
#: for randomised items. ``qti-printed-variable`` prints a variable's value directly.
#: ``qti-stylesheet`` is stripped *here as well as* at item level, because
#: ``qti-rubric-block`` can carry its own and rubric blocks survive redaction --- CSS
#: can single out the correct choice, and it is an out-of-band fetch mid-exam.
STRIP_FROM_BODY: frozenset[str] = frozenset(
    {
        "qti-feedback-block",
        "qti-feedback-inline",
        "qti-template-block",
        "qti-template-inline",
        "qti-printed-variable",
        "qti-stylesheet",
    }
)

#: ``qti-rubric-block`` is published only when it is addressed to the candidate *and*
#: is not the marking scheme.
#:
#: Both halves are required. ``use="scoring"`` **is** the mark scheme, so checking
#: ``view`` alone publishes it whenever the author also tagged it for the candidate.
#: And ``view`` is a token *list*: testing ``"candidate" in view`` keeps
#: ``view="candidate scorer"``, which is a denylist wearing an allowlist's clothes.
#: Equality is the point.
CANDIDATE_VIEW = "candidate"
CANDIDATE_RUBRIC_USE = "instructions"

#: Attributes cleared on every node. All are author annotations with no candidate-
#: facing function, and all are free text an answer can hide in --- ``label="KEY"``,
#: ``style`` visually marking the correct choice, ``xref`` pointing at a mark scheme.
CLEAR_ATTRIBUTES: frozenset[str] = frozenset({"label", "style", "xref"})

#: ``class`` tokens that survive. Everything else is dropped.
#:
#: ``class`` cannot simply be cleared --- it is how QTI 3.0 authors select presentation
#: from the specification's *shared vocabulary* (label numbering, choice stacking,
#: input widths). But it also cannot be published as authored, because
#: ``class="correct-answer"`` is self-documenting and it is the join key for the
#: stylesheet vector.
#:
#: This set is deliberately conservative: it holds the shared-vocabulary tokens we are
#: confident about, and an unrecognised token is dropped rather than published. Widen
#: it when a fixture needs a token, never speculatively --- the same discipline
#: ``examples/choice-rich-body.xml`` documents for element support.
ALLOWED_CLASS_TOKENS: frozenset[str] = frozenset(
    {
        # choice label numbering and suffixes
        "qti-labels-none",
        "qti-labels-decimal",
        "qti-labels-lower-alpha",
        "qti-labels-upper-alpha",
        "qti-labels-cjk-ideographic",
        "qti-labels-suffix-none",
        "qti-labels-suffix-period",
        "qti-labels-suffix-parenthesis",
        # layout
        "qti-orientation-horizontal",
        "qti-orientation-vertical",
        "qti-choices-stacking-1",
        "qti-choices-stacking-2",
        "qti-choices-stacking-3",
        "qti-choices-stacking-4",
        "qti-choices-stacking-5",
        # alignment
        "qti-align-left",
        "qti-align-center",
        "qti-align-right",
        "qti-valign-top",
        "qti-valign-middle",
        "qti-valign-bottom",
        # misc presentation
        "qti-fullwidth",
        "qti-underline",
        "qti-well",
    }
)


def _empty_for(current: Any) -> Any:
    if isinstance(current, list):
        return []
    if isinstance(current, dict):
        return {}
    return None


def _tokens(raw: Any) -> set[str]:
    """Normalise a QTI token-list attribute to a set of plain strings."""
    if raw is None:
        return set()
    values = raw if isinstance(raw, list | tuple | set) else [raw]
    return {str(getattr(value, "value", value)) for value in values}


def _should_strip_from_body(name: str, node: Any) -> bool:
    if name in STRIP_FROM_BODY:
        return True

    # Anything the parser could not map to a known QTI type lands as an AnyElement:
    # a foreign-namespace element, or unrecognised markup absorbed by a wildcard.
    # It is by definition uninspectable, so it cannot be published.
    if isinstance(node, AnyElement):
        return True

    if name == "qti-rubric-block":
        views = _tokens(getattr(node, "view", None))
        use = getattr(node, "use", None)
        use_value = str(getattr(use, "value", use)) if use is not None else None
        return views != {CANDIDATE_VIEW} or use_value != CANDIDATE_RUBRIC_USE

    return False


def _scrub_attributes(root: Any) -> None:
    """Clear answer-bearing attributes on ``root`` and every node beneath it.

    Attributes are not children, so :func:`~pyqti.qtitree.prune` never sees them.
    Skipping this walk is how ``label="KEY"``, ``style``, and arbitrary
    author-supplied ``data-*`` and foreign-namespace attributes reach a candidate:
    215 of the classes reachable from an item body carry the ``##any`` attribute
    wildcard, and because that wildcard *absorbs* unknown attributes, the strict
    parser's ``fail_on_unknown_properties`` never complains about them.
    """
    for node in iter_nodes(root):
        for var in attribute_vars(node):
            if var.is_attributes:
                # The ##any wildcard: unbounded and unauditable. Always empty it.
                setattr(node, var.name, {})
            elif var.local_name == "class":
                surviving = sorted(
                    _tokens(getattr(node, var.name, None)) & ALLOWED_CLASS_TOKENS
                )
                setattr(node, var.name, surviving)
            elif var.local_name in CLEAR_ATTRIBUTES:
                setattr(node, var.name, [] if var.tokens else None)


def redact_for_delivery(model: QtiAssessmentItem) -> QtiAssessmentItem:
    """Return a deep copy of ``model`` with everything answer-bearing removed.

    The input is never mutated: the caller keeps the authoritative item to grade
    against. Raises :class:`~pyqti.errors.UnsupportedContentError` if the model has a
    field this module has not classified.
    """
    unclassified = {
        field.name
        for field in fields(model)
        if field.name not in KEEP | CLEAR | KEEP_WITH_REVIEW
    }
    if unclassified:
        raise UnsupportedContentError(
            "redaction has no keep-or-strip decision for "
            f"qti-assessment-item field(s): {', '.join(sorted(unclassified))}. "
            "Classify them in pyqti/redaction.py before serving this item."
        )

    safe = copy.deepcopy(model)

    for name in CLEAR:
        setattr(safe, name, _empty_for(getattr(safe, name)))

    for declaration in safe.qti_response_declaration:
        for name in REDACT_ON_RESPONSE:
            setattr(declaration, name, None)

    # Prune the catalog too, not just the body. Accessibility content is published
    # (see KEEP_WITH_REVIEW) so it must go through the same element filter -- it is
    # authored prose, and prose is where an answer hides.
    for subtree in (safe.qti_item_body, safe.qti_catalog_info):
        if subtree is not None:
            prune(subtree, _should_strip_from_body)

    # Attributes last, so anything the element pass introduced is covered too.
    _scrub_attributes(safe)

    return safe


def presentation_xml(model: QtiAssessmentItem) -> str:
    """Redact ``model`` and serialize it as QTI XML, ready to serve to a front end.

    This is the only function that should ever produce item XML for a candidate.
    """
    return to_qti_xml(redact_for_delivery(model))
