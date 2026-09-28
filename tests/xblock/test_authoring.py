"""OLX authoring: ``<openedx-qti>`` carries the OLX, its child is the QTI."""

import re

import pytest
from lxml import etree
from xblock.fields import Boolean, Scope, ScopeIds

from pyqti._xsdata import QTI_NAMESPACE
from pyqti.errors import QtiStructureError, UnsupportedQtiFeature
from pyqti.loading import load_assessment_item
from pyqti.xblock.block import QtiAssessmentItemBlock

from .conftest import build_block, build_runtime, call_json, exported, parse_olx

BARE = """<qti-assessment-item identifier="bare" title="Bare" time-dependent="false">
  <qti-response-declaration identifier="RESPONSE" cardinality="single"
   base-type="identifier">
    <qti-correct-response><qti-value>A</qti-value></qti-correct-response>
  </qti-response-declaration>
  <qti-outcome-declaration identifier="SCORE" cardinality="single"
   base-type="float"/>
  <qti-item-body>
    <p>Pick <em>A</em>.</p>
    <qti-choice-interaction response-identifier="RESPONSE" max-choices="1">
      <qti-simple-choice identifier="A">Alpha</qti-simple-choice>
      <qti-simple-choice identifier="B">Beta</qti-simple-choice>
    </qti-choice-interaction>
  </qti-item-body>
  <qti-response-processing
   template="https://purl.imsglobal.org/spec/qti/v3p0/rptemplates/match_correct"/>
</qti-assessment-item>"""

#: The OLX-side names these tests put on the wrapper; none may reach the QTI.
OLX_NAMES = {"url_name", "display_name", "max_attempts", "weight"}


def olx(qti_xml, /, **attributes):
    """Wrap a QTI item in ``<openedx-qti>``, as a course's OLX would."""
    wrapper = etree.Element("openedx-qti", attributes)
    wrapper.append(etree.fromstring(qti_xml.encode("utf-8")))
    return wrapper


def test_namespaced_olx_is_read_as_qti(examples_dir):
    """A file that is valid QTI as it stands imports unchanged."""
    block = parse_olx(olx((examples_dir / "firstexample.xml").read_text()))
    item = load_assessment_item(block.qti_xml)
    assert item.identifier == "firstexample"
    assert block.qti_namespace_declared is True


def test_bare_olx_gets_the_qti_namespace_injected():
    """Namespace-free OLX is also accepted; pyqti's parser needs the namespace."""
    block = parse_olx(olx(BARE))
    assert block.qti_namespace_declared is False
    assert QTI_NAMESPACE in block.qti_xml
    item = load_assessment_item(block.qti_xml)
    assert item.identifier == "bare"


def test_html_vocabulary_is_namespaced_too():
    """QTI 3.0 puts <p>/<em> in the QTI namespace, so bare OLX must qualify them."""
    block = parse_olx(olx(BARE))
    root = etree.fromstring(block.qti_xml.encode())
    paragraphs = root.findall(f".//{{{QTI_NAMESPACE}}}p")
    assert paragraphs, "nested HTML vocabulary was not put in the QTI namespace"


def test_title_becomes_the_display_name():
    assert parse_olx(olx(BARE)).display_name == "Bare"


def test_olx_attributes_are_settings_and_stay_out_of_the_qti(examples_dir):
    """The point of the wrapper: the two vocabularies never share an element."""
    node = olx(
        (examples_dir / "firstexample.xml").read_text(),
        url_name="u1",
        display_name="Adrenal",
        max_attempts="3",
        weight="2.5",
        show_score_immediately="false",
    )
    block = parse_olx(node)
    assert block.display_name == "Adrenal", "an explicit name must beat the title"
    assert (block.max_attempts, block.weight) == (3, 2.5)
    assert block.show_score_immediately is False
    root = etree.fromstring(block.qti_xml.encode())
    assert not set(root.attrib) & OLX_NAMES


def test_attributes_that_are_not_settings_are_ignored(caplog):
    """Never a back door around _store_qti's validation, or into learner state."""
    block = parse_olx(olx(BARE, qti_xml="<not-qti/>", num_attempts="5", colour="red"))
    assert load_assessment_item(block.qti_xml).identifier == "bare"
    assert block.num_attempts == 0
    for name in ("qti_xml", "num_attempts", "colour"):
        assert repr(name) in caplog.text


def test_a_block_with_no_item_yet_imports_empty():
    """What Studio creates, so what exporting a fresh block produces."""
    block = parse_olx('<openedx-qti display_name="Draft"/>')
    assert (block.qti_xml, block.display_name) == ("", "Draft")


def test_wrong_child_element_is_rejected():
    with pytest.raises(QtiStructureError, match="found <p>"):
        parse_olx("<openedx-qti><p>nope</p></openedx-qti>")


@pytest.mark.parametrize(
    "content",
    [BARE + BARE, "loose text" + BARE, BARE + "loose text"],
    ids=["two items", "text before", "text after"],
)
def test_the_wrapper_holds_one_item_and_nothing_else(content):
    """Refused, not dropped: whatever it was, the author meant it to be there."""
    with pytest.raises(QtiStructureError, match="exactly one <qti-assessment-item>"):
        parse_olx(f"<openedx-qti>{content}</openedx-qti>")


def test_export_puts_settings_on_the_wrapper_and_the_item_inside(examples_dir):
    block = build_block(
        (examples_dir / "firstexample.xml").read_text(),
        display_name="Adrenal",
        max_attempts=3,
        weight=2.5,
    )
    node = exported(block)
    assert node.tag == "openedx-qti"
    assert {name: node.get(name) for name in OLX_NAMES} == {
        "url_name": "u1",
        "display_name": "Adrenal",
        "max_attempts": "3",
        "weight": "2.5",
    }
    (item,) = node
    assert etree.QName(item).localname == "qti-assessment-item"
    assert not set(item.attrib) & OLX_NAMES


def test_only_settings_that_were_set_are_exported(examples_dir):
    """Defaults stay out of the OLX, as they do for the platform's own blocks."""
    node = exported(build_block((examples_dir / "firstexample.xml").read_text()))
    assert set(node.attrib) == {"url_name", "display_name"}


def test_export_then_import_is_lossless(examples_dir):
    block = build_block(
        (examples_dir / "firstexample.xml").read_text(),
        display_name="Adrenal",
        max_attempts=3,
        weight=2.5,
        show_score_immediately=False,
    )
    again = parse_olx(exported(block))
    for name in (
        "qti_xml",
        "qti_namespace_declared",
        "display_name",
        "max_attempts",
        "weight",
        "show_score_immediately",
    ):
        assert getattr(again, name) == getattr(block, name), name


def test_platform_settings_round_trip_too(examples_dir):
    """edx-platform mixes settings into every block; dropping them loosens access."""

    class Mixed(QtiAssessmentItemBlock):
        visible_to_staff_only = Boolean(default=False, scope=Scope.settings)

    block = Mixed(
        build_runtime(), scope_ids=ScopeIds("learner", "openedx-qti", "d", "u")
    )
    block._store_qti((examples_dir / "firstexample.xml").read_text())
    block.visible_to_staff_only = True

    node = exported(block)
    assert node.get("visible_to_staff_only") == "true"
    assert parse_olx(node, block_class=Mixed).visible_to_staff_only is True


def test_export_round_trips_namespaced(examples_dir):
    block = parse_olx(olx((examples_dir / "firstexample.xml").read_text()))
    (item,) = exported(block)
    assert load_assessment_item(etree.tostring(item)).identifier == "firstexample"


def test_export_round_trips_bare():
    """Export returns the shape the author wrote, so re-import is lossless."""
    block = parse_olx(olx(BARE))
    node = exported(block)
    (item,) = node
    assert item.tag == "qti-assessment-item"
    assert "xmlns" not in etree.tostring(node, encoding="unicode")

    reimported = parse_olx(node)
    assert load_assessment_item(reimported.qti_xml).identifier == "bare"


def test_qti_children_are_content_not_blocks():
    """<p> inside an item must never be parsed as a child XBlock."""
    assert QtiAssessmentItemBlock.has_children is False
    block = parse_olx(olx(BARE))
    assert not hasattr(block, "children")
    # The prose survived as item content rather than being eaten as a block.
    assert "Alpha" in block.qti_xml


def test_unsupported_qti_is_refused_at_authoring_time():
    """Failing at import beats failing at exam time."""
    unsupported = BARE.replace(
        'template="https://purl.imsglobal.org/spec/qti/v3p0/rptemplates/'
        'match_correct"',
        'template="https://example.invalid/not-a-real-template"',
    )
    with pytest.raises(UnsupportedQtiFeature):
        parse_olx(olx(unsupported))


def test_studio_save_rejects_invalid_qti():
    block = build_block(BARE)
    original = block.qti_xml
    status, body = call_json(
        block, "submit_studio_edits", {"values": {"qti_xml": "<not-qti/>"}}
    )
    assert status == 400
    assert "qti-assessment-item" in body["error"]
    assert block.qti_xml == original, "invalid QTI must not reach Scope.content"


def test_studio_save_surfaces_the_unsupported_feature_message():
    """The author sees pyqti's own wording, which names what is unsupported."""
    block = build_block(BARE)
    unsupported = BARE.replace(
        'template="https://purl.imsglobal.org/spec/qti/v3p0/rptemplates/'
        'match_correct"',
        'template="https://example.invalid/not-a-real-template"',
    )
    status, body = call_json(
        block, "submit_studio_edits", {"values": {"qti_xml": unsupported}}
    )
    assert status == 400
    assert "example.invalid" in body["error"]


def test_studio_save_accepts_valid_qti(examples_dir):
    block = build_block(BARE)
    new_xml = (examples_dir / "firstexample.xml").read_text()
    status, body = call_json(
        block, "submit_studio_edits", {"values": {"qti_xml": new_xml}}
    )
    assert (status, body) == (200, {"result": "success"})
    assert load_assessment_item(block.qti_xml).identifier == "firstexample"


def test_studio_accepts_bare_qti_too():
    """Studio and OLX must not disagree about what valid input looks like."""
    block = build_block(BARE)
    assert block.qti_namespace_declared is False
    assert QTI_NAMESPACE in block.qti_xml


def test_every_example_imports_as_olx(examples_dir):
    """The fixtures are native QTI, so wrapping any of them gives valid OLX."""
    for path in sorted(examples_dir.glob("*.xml")):
        block = parse_olx(olx(path.read_text()))
        assert block.qti_xml, f"{path.name} produced no stored QTI"


def test_adversarial_fixture_still_imports(examples_dir):
    """It is deliberately nasty, but it is valid QTI and must import."""
    block = parse_olx(olx((examples_dir / "adversarial-leaks.xml").read_text()))
    assert re.search(r"LEAK_[A-Z_0-9]+", block.qti_xml), (
        "the authoritative copy is supposed to retain the sentinels"
    )
