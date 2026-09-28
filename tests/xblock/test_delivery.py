"""Serving, grading and scoring.

The block is a second delivery path for QTI, so it is a second place the answer
could escape. These tests exist mostly to make sure it never becomes one.
"""

import re

import pytest

from pyqti.session import COMPLETED, ItemSession

from .conftest import build_block, call_handler, call_json


@pytest.fixture
def item(examples_dir):
    return (examples_dir / "firstexample.xml").read_text(encoding="utf-8")


@pytest.fixture
def block(item):
    return build_block(item)


# ---------------------------------------------------------------- serving --


def test_served_xml_leaks_no_adversarial_sentinel(examples_dir):
    """The block must not become a second, unredacted delivery path.

    ``examples/adversarial-leaks.xml`` carries a unique ``LEAK_*`` sentinel per
    known vector. A handler that called ``to_qti_xml`` instead of
    ``presentation_xml`` would be a one-line regression that every test in
    tests/test_redaction.py would still pass.
    """
    source = (examples_dir / "adversarial-leaks.xml").read_text(encoding="utf-8")
    sentinels = sorted(set(re.findall(r"LEAK_[A-Z_0-9]+", source)))
    assert sentinels, "fixture is supposed to carry sentinels"

    status, served = call_handler(build_block(source), "item_xml")

    assert status == 200
    survived = [sentinel for sentinel in sentinels if sentinel in served]
    assert survived == [], f"redaction bypassed for: {survived}"


def test_served_xml_withholds_the_answer(block):
    status, served = call_handler(block, "item_xml")
    assert status == 200
    assert "qti-correct-response" not in served
    assert "qti-response-processing" not in served


def test_served_xml_is_xml(block):
    from webob import Request

    response = block.handle("item_xml", Request.blank("/"))
    assert response.content_type == "application/xml"


def test_student_view_does_not_contain_the_item(block):
    """Rendering is the browser's job; the fragment carries no item content."""
    content = block.student_view().content
    assert "Epinephrine" not in content
    assert "item-container" in content


def test_student_view_without_an_item_is_harmless():
    assert "no QTI item" in build_block().student_view().content


# --------------------------------------------------------------- grading --


def test_correct_response_scores(block):
    status, body = call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    assert status == 200
    assert body["score"] == 1.0
    assert body["max_score"] == 1.0
    assert body["completion_status"] == COMPLETED


def test_incorrect_response_scores_zero(block):
    _, body = call_json(block, "submit_response", {"responses": {"RESPONSE": "B"}})
    assert body["score"] == 0.0


def test_grade_is_published(block):
    call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    published = [event for event in block.runtime.published if event[0] == "grade"]
    assert published, "no grade event reached the runtime"
    assert published[-1][1]["value"] == 1.0
    assert published[-1][1]["max_value"] == 1.0


def test_state_persists_across_submissions(block):
    call_json(block, "submit_response", {"responses": {"RESPONSE": "B"}})
    call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    assert block.num_attempts == 2
    assert block.raw_responses == {"RESPONSE": "A"}
    assert block.raw_earned == 1.0


def test_attempt_count_comes_from_the_block_not_the_session(block):
    """ItemSession is per-request; only the block's field is durable."""
    call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    assert block.num_attempts == 3

    # A fresh session would have said 1 every time; the block resumes it.
    session = block._session()
    assert session.num_attempts == 3


def test_max_attempts_is_enforced_before_grading(block, monkeypatch):
    block.max_attempts = 1
    call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})

    def explode(*args, **kwargs):
        raise AssertionError("grading ran despite the attempt limit")

    monkeypatch.setattr(ItemSession, "submit", explode)
    status, body = call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    assert status == 403
    assert block.num_attempts == 1


def test_attempts_remaining_is_reported(block):
    block.max_attempts = 3
    _, body = call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    assert body["attempts_remaining"] == 2


def test_unlimited_attempts_report_none(block):
    _, body = call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    assert body["attempts_remaining"] is None


def test_invalid_responses_are_reported_but_still_graded(block):
    """validate_responses reports; it must not become a gate."""
    _, body = call_json(
        block, "submit_response", {"responses": {"RESPONSE": "NOT_A_CHOICE"}}
    )
    assert body["valid"] is False
    assert body["errors"]
    assert body["score"] == 0.0
    assert block.num_attempts == 1


def test_malformed_payload_is_rejected(block):
    status, _ = call_json(block, "submit_response", {"responses": "not a dict"})
    assert status == 400


def test_undeclared_response_identifier_is_rejected(block):
    status, body = call_json(block, "submit_response", {"responses": {"NOPE": "A"}})
    assert status == 400
    # No enumeration of what the valid identifiers would have been.
    assert "RESPONSE" not in body["error"]


# ------------------------------------------------------- score withholding --


def test_score_can_be_withheld(block):
    block.show_score_immediately = False
    _, body = call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    assert "score" not in body
    assert "max_score" not in body
    # Still graded and still published --- only the echo is withheld.
    assert block.raw_earned == 1.0
    assert [e for e in block.runtime.published if e[0] == "grade"]


# ----------------------------------------------------------------- scoring --


def test_scorable_contract(block):
    assert block.has_score is True
    assert block.has_submitted_answer() is False
    call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    assert block.has_submitted_answer() is True
    assert block.get_score().raw_earned == 1.0
    assert block.max_score() == 1.0


def test_calculate_score_is_pure(block):
    call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    before = block.num_attempts
    assert block.calculate_score().raw_earned == 1.0
    assert block.num_attempts == before, "calculate_score must not mutate state"


def test_raw_possible_override_is_honoured(block):
    block.raw_possible_override = 5.0
    _, body = call_json(block, "submit_response", {"responses": {"RESPONSE": "A"}})
    assert body["max_score"] == 5.0


# ------------------------------------------------------------------- seed --


def test_shuffle_seed_is_stable_and_recorded(block):
    first = block._seed()
    assert first
    assert block._seed() == first, "the seed must not change between renders"
    assert block.shuffle_seed == first


def test_shuffle_seed_differs_per_usage(item):
    from xblock.fields import ScopeIds

    from pyqti.xblock.block import QtiAssessmentItemBlock

    from .conftest import build_runtime

    seeds = set()
    for usage in ("usage-1", "usage-2"):
        runtime = build_runtime()
        other = QtiAssessmentItemBlock(
            runtime,
            scope_ids=ScopeIds("learner", "openedx-qti", "def-1", usage),
        )
        other._store_qti(item)
        seeds.add(other._seed())
    assert len(seeds) == 2
