"""Response processing: template resolution, three-valued logic, and scoring."""

import pytest

from pyqti.errors import (
    QtiStructureError,
    UnsupportedExpressionError,
    UnsupportedRuleError,
    UnsupportedTemplateError,
)
from pyqti.loading import load_assessment_item, load_response_processing
from pyqti.processing import ast
from pyqti.processing.compile import compile_response_processing
from pyqti.processing.evaluate import evaluate
from pyqti.processing.templates import load_template, template_name_for_uri
from pyqti.session import ItemSession, grade

MATCH_CORRECT_URI = "https://purl.imsglobal.org/spec/qti/v3p0/rptemplates/match_correct"


def item(examples_dir, name):
    return load_assessment_item(examples_dir / name)


# --------------------------------------------------------------------------- #
# Scoring
# --------------------------------------------------------------------------- #


def test_correct_response_scores_one(first_example):
    outcomes = grade(first_example, {"RESPONSE": "A"})
    assert outcomes["SCORE"] == 1.0
    assert type(outcomes["SCORE"]) is float


def test_incorrect_response_scores_zero(first_example):
    """The else-branch test, and the whole reason match_correct is vendored intact.

    ``examples/firstexample.xml`` declares ``SCORE`` with a ``qti-default-value`` of
    **1**. If ``qti-response-else`` were not executed, the default would survive and
    a wrong answer would score 1.0 --- i.e. every answer marked correct.
    """
    outcomes = grade(first_example, {"RESPONSE": "B"})
    assert outcomes["SCORE"] == 0.0


def test_unanswered_response_scores_zero(first_example):
    outcomes = grade(first_example, {})
    assert outcomes["SCORE"] == 0.0


def test_null_match_is_null_not_false(first_example):
    """Pins three-valued logic at the unit level.

    With ``match_correct`` alone a wrong answer and an unanswered one both score 0,
    so only this assertion distinguishes "match returned False" from "match returned
    NULL". The difference is invisible today and decisive once ``qti-and``/``qti-or``
    are involved.
    """
    session = ItemSession(first_example)
    condition = session.processing.rules[0].if_branch.condition

    assert evaluate(condition, session) is None, "unanswered match must be NULL"

    session.set_responses({"RESPONSE": "B"})
    assert evaluate(condition, session) is False, "wrong answer must be False"

    session.set_responses({"RESPONSE": "A"})
    assert evaluate(condition, session) is True


def test_inline_rules_match_the_template(examples_dir):
    """Proves the engine interprets inline rules, not just template URIs.

    ``choice-if-only.xml`` has no ``@template`` at all, and no ``qti-response-else``,
    so the declared default of 1 has to survive a wrong or unanswered response.
    """
    model = item(examples_dir, "choice-if-only.xml")

    assert grade(model, {"RESPONSE": "A"})["SCORE"] == 2.0
    assert grade(model, {"RESPONSE": "B"})["SCORE"] == 1.0
    assert grade(model, {})["SCORE"] == 1.0


def test_rich_body_item_grades(examples_dir):
    model = item(examples_dir, "choice-rich-body.xml")

    assert grade(model, {"RESPONSE": "lt"})["SCORE"] == 1.0
    assert grade(model, {"RESPONSE": "gt"})["SCORE"] == 0.0


def test_undeclared_choice_still_grades_as_incorrect(first_example):
    """Response *validity* is a delivery-engine concern; RP must still run."""
    assert grade(first_example, {"RESPONSE": "Z"})["SCORE"] == 0.0


# --------------------------------------------------------------------------- #
# Templates
# --------------------------------------------------------------------------- #


def test_template_uri_resolution():
    assert template_name_for_uri(MATCH_CORRECT_URI) == "match_correct"
    assert (
        template_name_for_uri(
            "http://www.imsglobal.org/question/qti_v2p1/rptemplates/match_correct"
        )
        == "match_correct"
    ), "QTI 2.x URIs appear in real content and must resolve"


def test_unknown_template_uri_raises():
    """A no-op here would leave every outcome at its default and mark all correct."""
    with pytest.raises(UnsupportedTemplateError):
        template_name_for_uri("https://example.com/rptemplates/match_correct")

    with pytest.raises(UnsupportedTemplateError, match="no vendored copy"):
        template_name_for_uri(
            "https://purl.imsglobal.org/spec/qti/v3p0/rptemplates/map_nonsense"
        )


def test_vendored_match_correct_has_both_branches():
    compiled = compile_response_processing(load_template(MATCH_CORRECT_URI))
    (condition,) = compiled.rules

    assert isinstance(condition, ast.ResponseCondition)
    assert isinstance(condition.if_branch.condition, ast.Match)
    assert condition.else_rules, "match_correct must set SCORE on the else branch"


def test_map_response_template_names_its_missing_operator():
    """Vendored but unusable: the error should name ``qti-map-response`` exactly."""
    uri = "https://purl.imsglobal.org/spec/qti/v3p0/rptemplates/map_response"
    with pytest.raises(UnsupportedExpressionError, match="qti-map-response"):
        compile_response_processing(load_template(uri))


# --------------------------------------------------------------------------- #
# Compiler
# --------------------------------------------------------------------------- #


def rp(body: str):
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<qti-response-processing xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0">'
        f"{body}"
        "</qti-response-processing>"
    )
    return compile_response_processing(load_response_processing(xml))


def test_compiles_none_to_empty():
    assert compile_response_processing(None).rules == ()


def test_unsupported_expression_raises():
    with pytest.raises(UnsupportedExpressionError, match="qti-sum"):
        rp(
            """<qti-response-condition><qti-response-if>
             <qti-match>
              <qti-sum><qti-base-value base-type="float">1</qti-base-value>
               <qti-base-value base-type="float">2</qti-base-value></qti-sum>
              <qti-base-value base-type="float">3</qti-base-value>
             </qti-match>
            </qti-response-if></qti-response-condition>"""
        )


def test_unsupported_rule_raises():
    with pytest.raises(UnsupportedRuleError, match="qti-lookup-outcome-value"):
        rp(
            '<qti-lookup-outcome-value identifier="SCORE">'
            '<qti-base-value base-type="float">1</qti-base-value>'
            "</qti-lookup-outcome-value>"
        )


def test_template_plus_inline_rules_is_rejected():
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<qti-response-processing xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"'
        f' template="{MATCH_CORRECT_URI}">'
        '<qti-set-outcome-value identifier="SCORE">'
        '<qti-base-value base-type="float">1</qti-base-value>'
        "</qti-set-outcome-value>"
        "</qti-response-processing>"
    )
    with pytest.raises(QtiStructureError, match="both"):
        compile_response_processing(load_response_processing(xml))


def test_template_location_is_refused_explicitly():
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<qti-response-processing xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"'
        ' template-location="rp.xml"/>'
    )
    with pytest.raises(UnsupportedRuleError, match="template-location"):
        compile_response_processing(load_response_processing(xml))


def test_exit_response_stops_processing():
    compiled = rp(
        '<qti-set-outcome-value identifier="SCORE">'
        '<qti-base-value base-type="float">5</qti-base-value>'
        "</qti-set-outcome-value>"
        "<qti-exit-response/>"
        '<qti-set-outcome-value identifier="SCORE">'
        '<qti-base-value base-type="float">9</qti-base-value>'
        "</qti-set-outcome-value>"
    )
    assert isinstance(compiled.rules[1], ast.ExitResponse)


# --------------------------------------------------------------------------- #
# Three-valued logic
# --------------------------------------------------------------------------- #


class FakeState:
    def __init__(self, variables=None):
        self.variables = variables or {}
        self.outcomes = {}

    def get_variable(self, identifier):
        return self.variables.get(identifier)

    def set_outcome(self, identifier, value):
        self.outcomes[identifier] = value

    def correct_response(self, identifier):
        return self.variables.get(f"correct:{identifier}")

    def outcome_base_type(self, identifier):
        return None


TRUE = ast.BaseValue(base_type=None, value=True)
FALSE = ast.BaseValue(base_type=None, value=False)
NULL = ast.Null()


@pytest.mark.parametrize(
    ("node", "expected"),
    [
        (ast.And(operands=(TRUE, TRUE)), True),
        (ast.And(operands=(TRUE, FALSE)), False),
        (ast.And(operands=(TRUE, NULL)), None),
        # False wins over NULL: the conjunction is definitely false.
        (ast.And(operands=(FALSE, NULL)), False),
        (ast.Or(operands=(FALSE, FALSE)), False),
        (ast.Or(operands=(FALSE, TRUE)), True),
        (ast.Or(operands=(FALSE, NULL)), None),
        # True wins over NULL: the disjunction is definitely true.
        (ast.Or(operands=(TRUE, NULL)), True),
        (ast.Not(operand=TRUE), False),
        (ast.Not(operand=NULL), None),
        (ast.IsNull(operand=NULL), True),
        (ast.IsNull(operand=TRUE), False),
    ],
)
def test_three_valued_logic(node, expected):
    assert evaluate(node, FakeState()) is expected
