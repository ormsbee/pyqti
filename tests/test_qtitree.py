"""Pins the assumptions that the whole response-processing compiler rests on.

These are the highest-value tests in the suite. They do not test pyqti's behaviour
so much as they test that the *generated models still have the shape pyqti assumes*.
If someone regenerates ``pyqti.models`` with different xsdata flags --- notably
without ``--compound-fields`` --- these fail in milliseconds instead of the breakage
showing up as mis-graded responses.
"""

import pytest

from pyqti.errors import QtiStructureError
from pyqti.loading import load_assessment_item, load_response_processing
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.any_ndtype import (
    EqualDtype,
    LogicPairDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.response_condition_dtype import (
    ResponseIfDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.set_value_dtype import SetValueDtype
from pyqti.qtitree import (
    choice_name_collisions,
    choice_names,
    first_child,
    iter_children,
    iter_content,
)

MATCH_CORRECT = """<?xml version="1.0" encoding="UTF-8"?>
<qti-response-processing xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0">
  <qti-response-condition>
    <qti-response-if>
      <qti-match>
        <qti-variable identifier="RESPONSE"/>
        <qti-correct identifier="RESPONSE"/>
      </qti-match>
      <qti-set-outcome-value identifier="SCORE">
        <qti-base-value base-type="float">1</qti-base-value>
      </qti-set-outcome-value>
    </qti-response-if>
    <qti-response-else>
      <qti-set-outcome-value identifier="SCORE">
        <qti-base-value base-type="float">0</qti-base-value>
      </qti-set-outcome-value>
    </qti-response-else>
  </qti-response-condition>
</qti-response-processing>
"""


def tree(obj, depth=0):
    """Flatten to ``(depth, element_name, class_name)`` triples."""
    out = []
    for name, child in iter_children(obj):
        out.append((depth, name, type(child).__name__))
        out.extend(tree(child, depth + 1))
    return out


def test_response_processing_tree_names_are_recovered():
    """The nested-class thesis: ``QtiMatch`` must resolve to ``qti-match``.

    ``qti-match`` is generated as a distinct nested class per containing type, so
    this is what proves name recovery works rather than class-identity dispatch.
    """
    rp = load_response_processing(MATCH_CORRECT)

    assert tree(rp) == [
        (0, "qti-response-condition", "ResponseConditionDtype"),
        (1, "qti-response-if", "ResponseIfDtype"),
        (2, "qti-match", "QtiMatch"),
        (3, "qti-variable", "VariableDtype"),
        (3, "qti-correct", "CorrectDtype"),
        (2, "qti-set-outcome-value", "SetValueDtype"),
        (3, "qti-base-value", "BaseValueDtype"),
        (1, "qti-response-else", "ResponseElseDtype"),
        (2, "qti-set-outcome-value", "SetValueDtype"),
        (3, "qti-base-value", "BaseValueDtype"),
    ]


@pytest.mark.parametrize(
    ("cls", "field"),
    [
        (ResponseIfDtype, "choice"),
        (ResponseIfDtype, "choice_1"),
        (SetValueDtype, "choice"),
        (LogicPairDtype, "choice"),
        (EqualDtype, "choice"),
    ],
)
def test_choice_type_to_name_map_is_injective(cls, field):
    """No child type may map to two element names.

    xsdata generates the per-parent nested subclasses precisely to keep this true.
    If it ever stops being true, name recovery is ambiguous and the compiler cannot
    be trusted --- so this is asserted, not assumed.
    """
    assert choice_name_collisions(cls, field) == {}
    assert choice_names(cls, field), "expected a non-empty choice map"


def test_response_if_has_separate_condition_and_rule_fields():
    """``choice`` is the single condition; ``choice_1`` is the list of rules.

    Pins the ``--compound-fields`` contract. Confusing these two is the likeliest
    compiler bug, and regenerating without the flag would rename them entirely.
    """
    fields = {f.name for f in ResponseIfDtype.__dataclass_fields__.values()}
    assert {"choice", "choice_1"} <= fields

    rp = load_response_processing(MATCH_CORRECT)
    condition = first_child(rp, "qti-response-condition")
    response_if = first_child(condition, "qti-response-if")

    # The condition is a single object, the rules are a list.
    assert not isinstance(response_if.choice, list)
    assert isinstance(response_if.choice_1, list)


def test_item_body_children(first_example):
    assert [name for name, _ in iter_children(first_example.qti_item_body)] == [
        "p",
        "p",
        "qti-choice-interaction",
    ]


def test_mixed_content_preserves_text_and_element_order(first_example):
    """``iter_content`` must interleave text runs with elements in document order."""
    first_p = first_child(first_example.qti_item_body, "p")
    content = [
        (name, child if name is None else None) for name, child in iter_content(first_p)
    ]

    assert content[0] == (None, "Of the following hormones, which is produced by the ")
    assert content[1][0] == "em"


def test_choice_interaction_shape(first_example):
    interaction = first_child(first_example.qti_item_body, "qti-choice-interaction")

    assert interaction.response_identifier == "RESPONSE"
    assert interaction.max_choices == 1
    assert interaction.min_choices == 1
    assert interaction.shuffle is False

    choices = [(name, child.identifier) for name, child in iter_children(interaction)]
    assert choices == [
        ("qti-simple-choice", "A"),
        ("qti-simple-choice", "B"),
        ("qti-simple-choice", "C"),
        ("qti-simple-choice", "D"),
    ]


def test_bad_attribute_value_is_rejected(examples_dir):
    """``fail_on_converter_warnings=True`` must turn a bad attribute into an error.

    With xsdata's default config this parses "successfully" and leaves
    ``max_choices`` as the string ``'lots'`` --- exactly the silent-corruption class
    of bug that mis-grades candidates.
    """
    from xsdata.exceptions import ParserError

    xml = (examples_dir / "firstexample.xml").read_text()
    broken = xml.replace('max-choices="1"', 'max-choices="lots"')

    with pytest.raises(ParserError, match="max_choices"):
        load_assessment_item(broken)


def test_unknown_compound_field_raises():
    with pytest.raises(QtiStructureError):
        choice_names(ResponseIfDtype, "not_a_field")


def test_path_like_string_gets_an_actionable_error():
    with pytest.raises(ValueError, match="looks like a filename"):
        load_assessment_item("examples/firstexample.xml")
