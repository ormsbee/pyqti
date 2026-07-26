"""Parsing and the item façade."""

import pytest

from pyqti.errors import QtiStructureError
from pyqti.item import ItemDefinition
from pyqti.loading import load_assessment_item
from pyqti.values import BaseType, Cardinality


def test_parses_item_metadata(first_example):
    assert first_example.identifier == "firstexample"
    assert first_example.title == "First Example"
    assert first_example.time_dependent is False


def test_facade_exposes_declarations(first_example):
    item = ItemDefinition.from_model(first_example)

    response = item.response_declarations["RESPONSE"]
    assert response.cardinality is Cardinality.SINGLE
    assert response.base_type is BaseType.IDENTIFIER
    assert response.correct_response == ("A",)
    assert response.correct_value == "A"

    outcome = item.outcome_declarations["SCORE"]
    assert outcome.cardinality is Cardinality.SINGLE
    assert outcome.base_type is BaseType.FLOAT
    # The Beginner's Guide item really does default SCORE to 1.
    assert outcome.default_value == (1.0,)
    assert type(outcome.default_value[0]) is float


def test_facade_exposes_interaction(first_example):
    item = ItemDefinition.from_model(first_example)
    (interaction,) = item.interactions

    assert interaction.response_identifier == "RESPONSE"
    assert interaction.max_choices == 1
    assert interaction.min_choices == 1
    assert interaction.shuffle is False
    assert interaction.orientation == "vertical"
    assert interaction.choice_identifiers == ("A", "B", "C", "D")
    assert interaction.is_single_answer

    assert item.interaction_for("RESPONSE") is interaction
    assert item.interaction_for("NOPE") is None


def test_correct_value_is_null_without_a_correct_response():
    """``qti-correct`` yields NULL, not an empty container, when none is declared."""
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
     identifier="no-correct" title="No Correct" time-dependent="false">
     <qti-response-declaration base-type="identifier" cardinality="single"
      identifier="RESPONSE"/>
    </qti-assessment-item>"""

    item = ItemDefinition.from_model(load_assessment_item(xml))
    declaration = item.response_declarations["RESPONSE"]

    assert declaration.has_correct_response is False
    assert declaration.correct_value is None


def test_interaction_without_a_declaration_is_rejected():
    """Nothing downstream could grade it, so refuse at façade construction."""
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
     identifier="unbound" title="Unbound" time-dependent="false">
     <qti-item-body>
      <qti-choice-interaction max-choices="1" response-identifier="MISSING">
       <qti-simple-choice identifier="A">A</qti-simple-choice>
      </qti-choice-interaction>
     </qti-item-body>
    </qti-assessment-item>"""

    with pytest.raises(QtiStructureError, match="MISSING"):
        ItemDefinition.from_model(load_assessment_item(xml))


def test_finds_interactions_nested_below_the_body():
    """Interactions need not be direct children of ``qti-item-body``."""
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
     identifier="nested" title="Nested" time-dependent="false">
     <qti-response-declaration base-type="identifier" cardinality="single"
      identifier="RESPONSE"/>
     <qti-item-body>
      <div><div>
       <qti-choice-interaction max-choices="1" response-identifier="RESPONSE">
        <qti-simple-choice identifier="A">A</qti-simple-choice>
       </qti-choice-interaction>
      </div></div>
     </qti-item-body>
    </qti-assessment-item>"""

    item = ItemDefinition.from_model(load_assessment_item(xml))
    assert len(item.interactions) == 1
    assert item.interactions[0].response_identifier == "RESPONSE"


def test_item_without_a_body_is_tolerated():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
     identifier="bodyless" title="Bodyless" time-dependent="false"/>"""

    item = ItemDefinition.from_model(load_assessment_item(xml))
    assert item.item_body is None
    assert item.interactions == ()
