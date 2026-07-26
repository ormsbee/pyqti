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
from xml.etree import ElementTree

import pytest

from pyqti.errors import UnsupportedContentError
from pyqti.item import ItemDefinition
from pyqti.loading import load_assessment_item
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0 import QtiAssessmentItem
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.response_declaration_dtype import (
    ResponseDeclarationDtype,
)
from pyqti.redaction import (
    CLEAR,
    KEEP,
    KEEP_WITH_REVIEW,
    REDACT_ON_RESPONSE,
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
    # accessibility catalog (published deliberately -- see KEEP_WITH_REVIEW)
    "qti-catalog",
    "qti-card",
    "qti-card-entry",
    "qti-html-content",
    "qti-file-href",
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

FIXTURES = [
    "firstexample.xml",
    "choice-if-only.xml",
    "choice-rich-body.xml",
    "adversarial-leaks.xml",
]

QTI_NS = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
XML_NS = "http://www.w3.org/XML/1998/namespace"

#: Attributes permitted on any element.
GLOBAL_ATTRIBUTES = {"id", "class", "lang", "dir", f"{{{XML_NS}}}lang"}

#: Attributes permitted on specific elements. Anything not listed here or in
#: :data:`GLOBAL_ATTRIBUTES` fails the pair allowlist below.
#:
#: The pair form matters. A flat element allowlist cannot see attributes at all, and
#: attributes are where the answer hides most easily: ``label="KEY"``, ``style``
#: highlighting the right choice, or --- once text entry is supported ---
#: ``pattern-mask="^(Paris|paris)$"``, which frequently *is* the answer.
ELEMENT_ATTRIBUTES = {
    "qti-assessment-item": {"identifier", "title", "time-dependent", "adaptive"},
    "qti-response-declaration": {"identifier", "cardinality", "base-type"},
    "qti-choice-interaction": {
        "response-identifier",
        "max-choices",
        "min-choices",
        "shuffle",
        "orientation",
    },
    "qti-simple-choice": {"identifier"},
    "qti-rubric-block": {"use", "view"},
    "qti-assessment-stimulus-ref": {"identifier", "href"},
    "qti-card": {"support"},
    "a": {"href", "target", "rel"},
    "img": {"src", "alt", "width", "height"},
    "td": {"colspan", "rowspan", "headers", "scope"},
    "th": {"colspan", "rowspan", "headers", "scope", "abbr"},
    "ol": {"type", "start", "reversed"},
}


def strip_ns(tag: str) -> str:
    return tag.split("}")[-1] if tag.startswith("{") else tag


def element_names(xml: str) -> set[str]:
    return set(re.findall(r"<([a-zA-Z][-a-zA-Z0-9]*)", xml))


def element_attribute_pairs(xml: str) -> set[tuple[str, str]]:
    """Every ``(element, attribute)`` pair in the document.

    Parsed rather than regexed: the regex approach used for element names cannot see
    attributes, and gets foreign-namespace names right only by accident.
    """
    root = ElementTree.fromstring(xml)
    return {
        (strip_ns(element.tag), name)
        for element in root.iter()
        for name in element.attrib
    }


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
def test_served_xml_contains_only_allowed_attributes(examples_dir, name):
    """The allowlist must cover attributes, not just elements.

    This is the check that was missing when redaction first shipped: ``prune()``
    removes children and never touches attributes, so ``label``, ``style``,
    ``data-*`` and foreign-namespace attributes all reached the candidate. 215 of the
    classes reachable from an item body carry the ``##any`` attribute wildcard, and
    because that wildcard absorbs unknown attributes the strict parser stays silent
    about them.
    """
    xml = presentation_xml(load_assessment_item(examples_dir / name))

    unexpected = {
        (element, attribute)
        for element, attribute in element_attribute_pairs(xml)
        if attribute not in GLOBAL_ATTRIBUTES
        and attribute not in ELEMENT_ATTRIBUTES.get(element, set())
    }

    assert not unexpected, (
        f"{name} would publish unrecognised attribute(s) {sorted(unexpected)}. "
        "Decide whether each is safe for a candidate to see, then either clear it in "
        "pyqti/redaction.py or add it to ELEMENT_ATTRIBUTES here."
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


def test_adversarial_fixture_leaks_no_sentinel(examples_dir):
    """The regression suite for every leak vector we know of.

    ``examples/adversarial-leaks.xml`` carries a unique ``LEAK_*`` sentinel per vector
    and ``KEEP_*`` for everything that must survive. Sentinels are discovered from the
    source rather than listed here, so adding a vector to the fixture automatically
    extends this test --- there is no second place to remember to update.
    """
    path = examples_dir / "adversarial-leaks.xml"
    source = path.read_text()
    served = presentation_xml(load_assessment_item(path))

    leaks = sorted(set(re.findall(r"LEAK_[A-Z_0-9]+", source)))
    keeps = sorted(set(re.findall(r"KEEP_[A-Z_0-9]+", source)))

    assert len(leaks) >= 20, "the adversarial fixture has lost its teeth"
    assert [s for s in leaks if s in served] == [], "answer-bearing content published"
    assert [s for s in keeps if s not in served] == [], "candidate content destroyed"


def test_response_declaration_publishes_only_three_attributes():
    """``qti-response-declaration`` must be provably closed.

    It is the one published class with no wildcards at all, so after
    ``REDACT_ON_RESPONSE`` clears its four element fields it can only carry
    ``identifier``, ``cardinality`` and ``base-type``. Pinning that means a model
    regeneration which adds a field to it fails here.
    """
    published = {
        field.name
        for field in fields(ResponseDeclarationDtype)
        if field.name not in REDACT_ON_RESPONSE
    }
    assert published == {"identifier", "cardinality", "base_type"}


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
