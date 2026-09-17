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
    """The default ``indent=None`` must not touch candidate-visible prose.

    lxml's writer does not reflow mid-sentence the way the pure-Python one does,
    so ``the <em>x</em>`` survives indentation intact. It still injects
    whitespace before the closing tag, and that whitespace is inside a
    mixed-content element the candidate reads, so ``indent=None`` remains the
    default --- for a milder reason than it used to be.
    """
    model = load_assessment_item(examples_dir / "firstexample.xml")

    compact = to_qti_xml(model)
    assert "the <em>adrenal glands?</em>" in compact
    assert "<strong>crazy</strong>." in compact
    assert "adrenal glands?</em>\n" not in compact

    indented = to_qti_xml(model, indent="  ")
    assert "the <em>adrenal glands?</em>" in indented, (
        "lxml's writer is expected to keep mixed content inline -- if this stops "
        "being true, check which writer xsdata selected"
    )
    assert "adrenal glands?</em>\n" in indented, (
        "indenting is still expected to add whitespace inside mixed content, "
        "which is why indent=None is the default"
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


def test_xsdata_uses_the_lxml_backed_pair():
    """Serialization must not vary with what else is installed.

    xsdata chooses its parser handler and serializer writer at import time from
    whether lxml is importable, and the two pairs disagree about mixed content.
    pyqti therefore depends on lxml outright rather than incidentally, so the
    choice is fixed. This asserts the choice actually landed: if lxml were ever
    dropped back to being optional, ``presentation_xml`` output would quietly
    change shape, and that output is the security boundary
    ``tests/test_redaction.py`` asserts over as text.
    """
    import xsdata.formats.dataclass.parsers.handlers as handlers
    import xsdata.formats.dataclass.serializers.writers as writers

    assert writers.DEFAULT_XML_WRITER is writers.LxmlEventWriter
    assert handlers.default_handler() is handlers.LxmlEventHandler
