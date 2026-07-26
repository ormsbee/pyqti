"""The tests that stand between a candidate and the answer key.

Structured as an **allowlist**: the served XML may only contain elements from an
explicitly permitted set. A denylist (``"qti-correct-response" not in xml``) only
catches leaks somebody already thought of, which is the wrong shape for the threat --
the realistic failure is a QTI feature or fixture nobody anticipated introducing a new
answer-bearing element. An allowlist fails on anything unfamiliar, including that.

Backed by semantic checks (re-parse and confirm the answer is genuinely gone), a
cannot-score check, and an immutability check on the authoritative model.
"""

import re
from dataclasses import fields

import pytest

from pyqti.errors import UnsupportedContentError
from pyqti.item import ItemDefinition
from pyqti.loading import load_assessment_item
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0 import QtiAssessmentItem
from pyqti.redaction import (
    CLEAR,
    KEEP,
    KEEP_WITH_REVIEW,
    presentation_xml,
    redact_for_delivery,
)
from pyqti.session import ItemSession

#: Elements a candidate is allowed to receive. Anything else in the served XML fails
#: the allowlist test below. Widening this set is a deliberate act: ask "could an
#: author hide the answer in here?" before adding to it.
ALLOWED_ELEMENTS = {
    # structure
    "qti-assessment-item",
    "qti-response-declaration",
    "qti-item-body",
    "qti-assessment-stimulus-ref",
    "qti-catalog-info",
    # candidate-facing QTI
    "qti-choice-interaction",
    "qti-simple-choice",
    "qti-prompt",
    "qti-rubric-block",
    "qti-content-body",
    # html content
    "a",
    "abbr",
    "b",
    "blockquote",
    "br",
    "caption",
    "cite",
    "code",
    "col",
    "colgroup",
    "dd",
    "del",
    "dfn",
    "div",
    "dl",
    "dt",
    "em",
    "figcaption",
    "figure",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "i",
    "img",
    "ins",
    "kbd",
    "li",
    "ol",
    "p",
    "pre",
    "q",
    "samp",
    "small",
    "span",
    "strong",
    "sub",
    "sup",
    "table",
    "tbody",
    "td",
    "tfoot",
    "th",
    "thead",
    "tr",
    "ul",
    "var",
}

#: Substrings that must never survive redaction, whatever the allowlist says.
FORBIDDEN = (
    "qti-correct-response",
    "qti-mapping",
    "qti-area-mapping",
    "qti-response-processing",
    "qti-outcome-declaration",
    "qti-modal-feedback",
    "qti-feedback-block",
    "qti-feedback-inline",
    "qti-template-declaration",
    "qti-template-processing",
    "qti-printed-variable",
    "qti-stylesheet",
    "schemaLocation",
)

FIXTURES = ["firstexample.xml", "choice-if-only.xml", "choice-rich-body.xml"]

QTI_NS = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


def element_names(xml: str) -> set[str]:
    return set(re.findall(r"<([a-zA-Z][-a-zA-Z0-9]*)", xml))


# --------------------------------------------------------------------------- #
# The allowlist
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("name", FIXTURES)
def test_served_xml_contains_only_allowed_elements(examples_dir, name):
    xml = presentation_xml(load_assessment_item(examples_dir / name))
    unexpected = element_names(xml) - ALLOWED_ELEMENTS

    assert not unexpected, (
        f"{name} would publish unrecognised element(s) {sorted(unexpected)}. "
        "Decide whether each is safe for a candidate to see, then either strip it in "
        "pyqti/redaction.py or add it to ALLOWED_ELEMENTS here."
    )


@pytest.mark.parametrize("name", FIXTURES)
def test_served_xml_has_no_forbidden_markers(examples_dir, name):
    xml = presentation_xml(load_assessment_item(examples_dir / name))
    assert [token for token in FORBIDDEN if token in xml] == []


# --------------------------------------------------------------------------- #
# Semantics, not just strings
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("name", FIXTURES)
def test_answer_is_semantically_gone(examples_dir, name):
    """Re-parse what we would serve and confirm there is no answer in it."""
    xml = presentation_xml(load_assessment_item(examples_dir / name))
    served = ItemDefinition.from_model(load_assessment_item(xml))

    for identifier, declaration in served.response_declarations.items():
        assert declaration.correct_value is None, identifier
        assert declaration.has_correct_response is False, identifier

    assert dict(served.outcome_declarations) == {}


@pytest.mark.parametrize("name", FIXTURES)
def test_redacted_item_cannot_score(examples_dir, name):
    """Even if the redacted item were graded by mistake, it must reveal nothing."""
    xml = presentation_xml(load_assessment_item(examples_dir / name))
    session = ItemSession(load_assessment_item(xml))

    assert session.processing.rules == (), "redacted items carry no scoring rules"
    assert session.submit({"RESPONSE": "A"}) == {}


@pytest.mark.parametrize("name", FIXTURES)
def test_presentation_surface_survives(examples_dir, name):
    """Redaction must not damage the question the candidate has to answer."""
    original = ItemDefinition.from_model(load_assessment_item(examples_dir / name))
    served = ItemDefinition.from_model(
        load_assessment_item(
            presentation_xml(load_assessment_item(examples_dir / name))
        )
    )

    assert served.identifier == original.identifier
    assert served.title == original.title
    assert [
        (i.response_identifier, i.choice_identifiers) for i in served.interactions
    ] == [(i.response_identifier, i.choice_identifiers) for i in original.interactions]


@pytest.mark.parametrize("name", FIXTURES)
def test_authoritative_model_is_untouched(examples_dir, name):
    """The caller keeps grading against the original, so it must not be mutated."""
    model = load_assessment_item(examples_dir / name)
    before = {
        d.identifier: d.correct_value
        for d in ItemDefinition.from_model(model).response_declarations.values()
    }

    redact_for_delivery(model)

    after = {
        d.identifier: d.correct_value
        for d in ItemDefinition.from_model(model).response_declarations.values()
    }
    assert after == before
    assert any(value is not None for value in after.values()), (
        "fixture should have a correct response, or this test proves nothing"
    )


def test_prose_around_a_stripped_inline_element_survives():
    """Removing an element must not swallow the text that followed it.

    xsdata absorbs a mixed-content tail *into* an element whose model has a wildcard
    field, so deleting ``qti-printed-variable`` would silently take the rest of the
    sentence with it. Silent content loss is a fairness failure in an exam, not a
    cosmetic one.
    """
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="{QTI_NS}" identifier="tail" title="Tail"
     time-dependent="false">
     <qti-outcome-declaration base-type="identifier" cardinality="single"
      identifier="FEEDBACK"/>
     <qti-item-body>
      <div><p>before <qti-printed-variable identifier="FEEDBACK"/> after</p></div>
     </qti-item-body>
    </qti-assessment-item>"""

    served = presentation_xml(load_assessment_item(xml))

    assert "qti-printed-variable" not in served
    assert "<p>before  after</p>" in served


def test_feedback_and_scorer_rubric_are_stripped_but_candidate_rubric_kept():
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="{QTI_NS}" identifier="fb" title="Fb"
     time-dependent="false">
     <qti-outcome-declaration base-type="identifier" cardinality="single"
      identifier="FEEDBACK"/>
     <qti-item-body>
      <qti-rubric-block use="scoring" view="scorer">
       <qti-content-body><p>SCORER-EYES-ONLY</p></qti-content-body>
      </qti-rubric-block>
      <qti-rubric-block use="instructions" view="candidate">
       <qti-content-body><p>Choose one.</p></qti-content-body>
      </qti-rubric-block>
      <qti-feedback-block outcome-identifier="FEEDBACK" identifier="ok"
       show-hide="show">
       <qti-content-body><p>LEAKY-FEEDBACK</p></qti-content-body>
      </qti-feedback-block>
     </qti-item-body>
    </qti-assessment-item>"""

    served = presentation_xml(load_assessment_item(xml))

    assert "SCORER-EYES-ONLY" not in served
    assert "LEAKY-FEEDBACK" not in served
    assert "Choose one." in served


# --------------------------------------------------------------------------- #
# Fail closed
# --------------------------------------------------------------------------- #


def test_every_item_field_is_classified():
    """No field of ``QtiAssessmentItem`` may be left unclassified.

    This is the guard that makes the allowlist meaningful over time: regenerating the
    models with a newer xsdata or schema could add a field, and an unclassified field
    would otherwise be published by default.
    """
    classified = KEEP | CLEAR | KEEP_WITH_REVIEW
    actual = {field.name for field in fields(QtiAssessmentItem)}

    assert actual - classified == set(), "unclassified field(s) would be published"
    assert classified - actual == set(), "classification names a field that is gone"


def test_unclassified_field_raises(monkeypatch):
    """Simulate a model regeneration that adds a field pyqti has not seen."""
    monkeypatch.setattr("pyqti.redaction.KEEP", KEEP - {"title"})

    with pytest.raises(UnsupportedContentError, match="title"):
        redact_for_delivery(
            load_assessment_item(
                f'<qti-assessment-item xmlns="{QTI_NS}" identifier="x" title="X" '
                'time-dependent="false"/>'
            )
        )
