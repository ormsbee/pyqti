"""Variable initialisation and the attempt lifecycle."""

import pytest

from pyqti.errors import QtiStructureError
from pyqti.loading import load_assessment_item
from pyqti.session import COMPLETED, INCOMPLETE, NOT_ATTEMPTED, ItemSession


def build(declarations: str) -> ItemSession:
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
     identifier="init" title="Init" time-dependent="false">
     <qti-response-declaration base-type="identifier" cardinality="single"
      identifier="RESPONSE">
      <qti-default-value><qti-value>A</qti-value></qti-default-value>
      <qti-correct-response><qti-value>A</qti-value></qti-correct-response>
     </qti-response-declaration>
     {declarations}
    </qti-assessment-item>"""
    return ItemSession(load_assessment_item(xml))


def test_numeric_outcome_without_a_default_starts_at_zero():
    """Normative, from ``OutcomeDeclarationDType``'s XSD annotation."""
    session = build(
        '<qti-outcome-declaration base-type="float" cardinality="single"'
        ' identifier="SCORE"/>'
        '<qti-outcome-declaration base-type="integer" cardinality="single"'
        ' identifier="COUNT"/>'
    )
    assert session.outcomes["SCORE"] == 0.0
    assert type(session.outcomes["SCORE"]) is float
    assert session.outcomes["COUNT"] == 0
    assert type(session.outcomes["COUNT"]) is int


def test_non_numeric_outcome_without_a_default_starts_null():
    session = build(
        '<qti-outcome-declaration base-type="identifier" cardinality="single"'
        ' identifier="GRADE"/>'
    )
    assert session.outcomes["GRADE"] is None


def test_outcome_default_value_is_used_and_coerced():
    session = build(
        '<qti-outcome-declaration base-type="float" cardinality="single"'
        ' identifier="SCORE">'
        "<qti-default-value><qti-value>3</qti-value></qti-default-value>"
        "</qti-outcome-declaration>"
    )
    assert session.outcomes["SCORE"] == 3.0
    assert type(session.outcomes["SCORE"]) is float


def test_response_variables_always_start_null_despite_a_default():
    """Normative, from ``ResponseDeclarationDType``'s XSD annotation.

    The declaration in :func:`build` gives ``RESPONSE`` a ``qti-default-value`` of
    ``A``; it must still start NULL. A single generic initialiser for both response
    and outcome variables gets this wrong.
    """
    session = build(
        '<qti-outcome-declaration base-type="float" cardinality="single"'
        ' identifier="SCORE"/>'
    )
    assert session.responses["RESPONSE"] is None


def test_builtins_start_unattempted():
    session = build(
        '<qti-outcome-declaration base-type="float" cardinality="single"'
        ' identifier="SCORE"/>'
    )
    assert session.completion_status == NOT_ATTEMPTED
    assert session.num_attempts == 0


def test_second_attempt_does_not_inherit_the_first_score(first_example):
    """Outcomes are reset before each response-processing run.

    Without the reset, ``choice-if-only``-style items (no else branch) would carry a
    previous attempt's score forward.
    """
    session = ItemSession(first_example)

    assert session.submit({"RESPONSE": "A"})["SCORE"] == 1.0
    assert session.num_attempts == 1

    assert session.submit({"RESPONSE": "B"})["SCORE"] == 0.0
    assert session.num_attempts == 2

    assert session.submit({"RESPONSE": "A"})["SCORE"] == 1.0


def test_second_attempt_reset_with_a_surviving_default(examples_dir):
    """The reset matters most when response processing does not assign every path."""
    model = load_assessment_item(examples_dir / "choice-if-only.xml")
    session = ItemSession(model)

    assert session.submit({"RESPONSE": "A"})["SCORE"] == 2.0
    # Without reset_outcomes() this would still be 2.0.
    assert session.submit({"RESPONSE": "B"})["SCORE"] == 1.0


def test_completion_status_tracks_answered_responses(first_example):
    session = ItemSession(first_example)

    session.submit({})
    assert session.completion_status == INCOMPLETE

    session.submit({"RESPONSE": "A"})
    assert session.completion_status == COMPLETED


def test_responses_are_coerced_to_their_declared_base_type():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
     identifier="numeric" title="Numeric" time-dependent="false">
     <qti-response-declaration base-type="float" cardinality="single"
      identifier="RESPONSE">
      <qti-correct-response><qti-value>2.5</qti-value></qti-correct-response>
     </qti-response-declaration>
     <qti-outcome-declaration base-type="float" cardinality="single"
      identifier="SCORE"/>
     <qti-response-processing
      template="https://purl.imsglobal.org/spec/qti/v3p0/rptemplates/match_correct"/>
    </qti-assessment-item>"""

    session = ItemSession(load_assessment_item(xml))
    # An int arriving from JSON must be cast to the declared float, or qti_match
    # would raise on mismatched types.
    assert session.submit({"RESPONSE": 2.5})["SCORE"] == 1.0
    assert type(session.responses["RESPONSE"]) is float


def test_validate_responses_reports_without_blocking(first_example):
    session = ItemSession(first_example)

    ok = session.validate_responses({"RESPONSE": "A"})
    assert ok.valid is True
    assert ok.errors == []

    too_few = session.validate_responses({})
    assert too_few.valid is False
    assert "min-choices" in too_few.errors[0]

    unknown_choice = session.validate_responses({"RESPONSE": "Z"})
    assert unknown_choice.valid is False
    assert "not one of the declared choices" in unknown_choice.errors[0]

    unknown_variable = session.validate_responses({"NOPE": "A"})
    assert unknown_variable.valid is False


def test_setting_an_undeclared_response_raises(first_example):
    session = ItemSession(first_example)
    with pytest.raises(QtiStructureError, match="NOPE"):
        session.set_responses({"NOPE": "A"})


def test_undeclared_variable_reference_raises():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
     identifier="bad-ref" title="Bad Ref" time-dependent="false">
     <qti-outcome-declaration base-type="float" cardinality="single"
      identifier="SCORE"/>
     <qti-response-processing>
      <qti-response-condition><qti-response-if>
       <qti-match>
        <qti-variable identifier="GHOST"/>
        <qti-base-value base-type="identifier">A</qti-base-value>
       </qti-match>
       <qti-set-outcome-value identifier="SCORE">
        <qti-base-value base-type="float">1</qti-base-value>
       </qti-set-outcome-value>
      </qti-response-if></qti-response-condition>
     </qti-response-processing>
    </qti-assessment-item>"""

    session = ItemSession(load_assessment_item(xml))
    with pytest.raises(QtiStructureError, match="GHOST"):
        session.process_responses()


def test_prior_attempts_resumes_the_attempt_counter(first_example):
    """A delivery engine holding durable state elsewhere resumes mid-history.

    ``ItemSession`` is per-request; the LMS (or any other engine) owns the real
    attempt count. Without this, every attempt would look like the first.
    """
    session = ItemSession(first_example, prior_attempts=3)
    assert session.num_attempts == 3

    session.submit({"RESPONSE": "A"})
    assert session.num_attempts == 4


def test_prior_attempts_defaults_to_a_fresh_session(first_example):
    session = ItemSession(first_example)
    assert session.num_attempts == 0
    session.submit({"RESPONSE": "A"})
    assert session.num_attempts == 1


def test_reset_returns_to_the_resumed_count_not_zero(first_example):
    """``reset()`` is pre-*attempt*, not pre-*history*."""
    session = ItemSession(first_example, prior_attempts=2)
    session.submit({"RESPONSE": "A"})
    session.reset()
    assert session.num_attempts == 2


def test_negative_prior_attempts_is_rejected(first_example):
    with pytest.raises(ValueError, match="must not be negative"):
        ItemSession(first_example, prior_attempts=-1)
