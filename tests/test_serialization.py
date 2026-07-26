"""Writing models back out as QTI XML."""

import pytest

from pyqti.loading import load_assessment_item
from pyqti.serialization import to_qti_xml

QTI_NS = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


def test_round_trips(examples_dir):
    original = load_assessment_item(examples_dir / "firstexample.xml")
    reparsed = load_assessment_item(to_qti_xml(original))

    assert reparsed.identifier == original.identifier
    assert reparsed.title == original.title
    assert len(reparsed.qti_response_declaration) == len(
        original.qti_response_declaration
    )


def test_uses_the_qti_default_namespace(examples_dir):
    xml = to_qti_xml(load_assessment_item(examples_dir / "firstexample.xml"))
    assert f'xmlns="{QTI_NS}"' in xml
    assert "ns0:" not in xml


def test_unindented_output_preserves_mixed_content(examples_dir):
    """The default ``indent=None`` must not reflow candidate-visible prose.

    With ``indent="  "`` xsdata pretty-prints *through* mixed content, turning
    ``the <em>x</em>`` into ``the\\n  <em>x</em>`` and thereby changing the text the
    candidate reads. That is why the default is no indentation.
    """
    model = load_assessment_item(examples_dir / "firstexample.xml")

    compact = to_qti_xml(model)
    assert "the <em>adrenal glands?</em>" in compact
    assert "<strong>crazy</strong>." in compact

    indented = to_qti_xml(model, indent="  ")
    assert "the <em>adrenal glands?</em>" not in indented, (
        "indenting is expected to reflow mixed content -- if this ever stops being "
        "true, the indent=None default can be revisited"
    )


def test_xsd_default_attributes_are_omitted(examples_dir):
    """``max-choices="1"`` is dropped because 1 is the XSD default.

    This is safe *for XML* and is relied upon: Citolab's ``qti-choice-interaction``
    initialises ``maxChoices = 1`` / ``minChoices = 0`` to match the schema, and picks
    radio vs checkbox from it. The assertion documents an assumption about a third
    party, so it should fail loudly if their behaviour or ours changes.
    """
    xml = to_qti_xml(load_assessment_item(examples_dir / "firstexample.xml"))

    assert 'max-choices="1"' not in xml
    assert 'min-choices="1"' in xml, "a non-default value must still be emitted"


@pytest.mark.parametrize(
    "name", ["firstexample.xml", "choice-if-only.xml", "choice-rich-body.xml"]
)
def test_every_fixture_round_trips(examples_dir, name):
    model = load_assessment_item(examples_dir / name)
    assert load_assessment_item(to_qti_xml(model)).identifier == model.identifier
