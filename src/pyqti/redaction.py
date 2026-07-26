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

from pyqti.errors import UnsupportedContentError
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0 import QtiAssessmentItem
from pyqti.qtitree import prune
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
STRIP_FROM_BODY: frozenset[str] = frozenset(
    {
        "qti-feedback-block",
        "qti-feedback-inline",
        "qti-template-block",
        "qti-template-inline",
        "qti-printed-variable",
    }
)

#: ``qti-rubric-block`` is only published when it is addressed to the candidate.
#: Any other ``view`` (``scorer``, ``author``, ``proctor``, ``tutor``) is by
#: definition not for them.
CANDIDATE_VIEW = "candidate"


def _empty_for(current: Any) -> Any:
    if isinstance(current, list):
        return []
    if isinstance(current, dict):
        return {}
    return None


def _should_strip_from_body(name: str, node: Any) -> bool:
    if name in STRIP_FROM_BODY:
        return True
    if name == "qti-rubric-block":
        # ``view`` is a token list in the schema, but tolerate a bare value so a
        # model regeneration cannot turn this control off by changing its shape.
        raw = getattr(node, "view", None) or []
        views = raw if isinstance(raw, list | tuple | set) else [raw]
        return CANDIDATE_VIEW not in {getattr(v, "value", v) for v in views}
    return False


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

    if safe.qti_item_body is not None:
        prune(safe.qti_item_body, _should_strip_from_body)

    return safe


def presentation_xml(model: QtiAssessmentItem) -> str:
    """Redact ``model`` and serialize it as QTI XML, ready to serve to a front end.

    This is the only function that should ever produce item XML for a candidate.
    """
    return to_qti_xml(redact_for_delivery(model))
