"""OLX authoring: the block's tag *is* the QTI element."""

import re

import pytest
from lxml import etree

from pyqti._xsdata import QTI_NAMESPACE
from pyqti.errors import QtiStructureError, UnsupportedQtiFeature
from pyqti.loading import load_assessment_item
from pyqti.xblock.block import QtiAssessmentItemBlock

from .conftest import build_block, build_runtime, call_json

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


def parse_olx(xml):
    node = etree.fromstring(xml.encode("utf-8"))
    runtime = build_runtime()
    keys = runtime.id_generator.create_definition("qti-assessment-item")
    from xblock.fields import ScopeIds

    scope_ids = ScopeIds("learner", "qti-assessment-item", keys, "usage-1")
    return QtiAssessmentItemBlock.parse_xml(node, runtime, scope_ids)


def test_namespaced_olx_is_read_as_qti(examples_dir):
    """A file that is valid QTI as it stands imports unchanged."""
    block = parse_olx((examples_dir / "firstexample.xml").read_text())
    item = load_assessment_item(block.qti_xml)
    assert item.identifier == "firstexample"
    assert block.qti_namespace_declared is True


def test_bare_olx_gets_the_qti_namespace_injected():
    """Namespace-free OLX is also accepted; pyqti's parser needs the namespace."""
    block = parse_olx(BARE)
    assert block.qti_namespace_declared is False
    assert QTI_NAMESPACE in block.qti_xml
    item = load_assessment_item(block.qti_xml)
    assert item.identifier == "bare"


def test_html_vocabulary_is_namespaced_too():
    """QTI 3.0 puts <p>/<em> in the QTI namespace, so bare OLX must qualify them."""
    block = parse_olx(BARE)
    root = etree.fromstring(block.qti_xml.encode())
    paragraphs = root.findall(f".//{{{QTI_NAMESPACE}}}p")
    assert paragraphs, "nested HTML vocabulary was not put in the QTI namespace"


def test_title_becomes_the_display_name():
    assert parse_olx(BARE).display_name == "Bare"


def test_export_round_trips_namespaced(examples_dir):
    block = parse_olx((examples_dir / "firstexample.xml").read_text())
    node = etree.Element("placeholder")
    block.add_xml_to_node(node)
    exported = etree.tostring(node, encoding="unicode")
    assert load_assessment_item(exported).identifier == "firstexample"


def test_export_round_trips_bare():
    """Export returns the shape the author wrote, so re-import is lossless."""
    block = parse_olx(BARE)
    node = etree.Element("placeholder")
    block.add_xml_to_node(node)
    assert node.tag == "qti-assessment-item"
    assert "xmlns" not in etree.tostring(node, encoding="unicode")

    reimported = parse_olx(etree.tostring(node, encoding="unicode"))
    assert load_assessment_item(reimported.qti_xml).identifier == "bare"


def test_wrong_root_element_is_rejected():
    with pytest.raises(QtiStructureError, match="expected a <qti-assessment-item>"):
        parse_olx("<vertical><p>nope</p></vertical>")


def test_qti_children_are_content_not_blocks():
    """<p> inside an item must never be parsed as a child XBlock."""
    assert QtiAssessmentItemBlock.has_children is False
    block = parse_olx(BARE)
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
        parse_olx(unsupported)


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
    """The fixtures are already native QTI, so they are also valid OLX."""
    for path in sorted(examples_dir.glob("*.xml")):
        block = parse_olx(path.read_text())
        assert block.qti_xml, f"{path.name} produced no stored QTI"


def test_adversarial_fixture_still_imports(examples_dir):
    """It is deliberately nasty, but it is valid QTI and must import."""
    block = parse_olx((examples_dir / "adversarial-leaks.xml").read_text())
    assert re.search(r"LEAK_[A-Z_0-9]+", block.qti_xml), (
        "the authoritative copy is supposed to retain the sentinels"
    )
