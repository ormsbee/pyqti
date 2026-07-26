"""HTML rendering, including the golden output for both body fixtures.

The golden strings are exact on purpose. They are what catch the ~24 ARIA attributes
every element inherits from ``AriabaseDType``, the loss of ``max-choices="1"`` if
``ignore_default_attributes`` were ever turned back on, escaping mistakes, and
mixed-content reordering --- the last being precisely what the deleted ``render.py``
got wrong.
"""

import pytest

from pyqti.errors import UnsupportedContentError
from pyqti.loading import load_assessment_item
from pyqti.render.html import render_item_body_html

FIRST_EXAMPLE_HTML = (
    '<div class="qti-item-body">'
    "<p>Of the following hormones, which is produced by the "
    "<em>adrenal glands?</em></p>"
    "<p>This is another paragraph just to make sure I'm not going "
    "<strong>crazy</strong>.</p>"
    '<qti-choice-interaction response-identifier="RESPONSE" shuffle="false" '
    'max-choices="1" min-choices="1" orientation="vertical">'
    '<qti-simple-choice identifier="A">Epinephrine</qti-simple-choice>'
    '<qti-simple-choice identifier="B">Glucagon</qti-simple-choice>'
    '<qti-simple-choice identifier="C">Insulin</qti-simple-choice>'
    '<qti-simple-choice identifier="D">Oxytocin</qti-simple-choice>'
    "</qti-choice-interaction>"
    "</div>"
)

RICH_BODY_HTML = (
    '<div class="qti-item-body">'
    "<p>Consider the following <em>strictly <strong>nested</strong></em> markup.</p>"
    "<ul>"
    "<li>Angle brackets: 1 &lt; 2</li>"
    "<li>An ampersand: Tom &amp; Jerry</li>"
    "<li>An apostrophe: I'm fine</li>"
    "</ul>"
    '<p>See the <a href="https://www.imsglobal.org/spec/qti/v3p0/guide">'
    "QTI 3.0 guide</a> for details.<br></p>"
    '<qti-choice-interaction response-identifier="RESPONSE" shuffle="false" '
    'max-choices="1" min-choices="1" orientation="vertical">'
    "<qti-prompt>Which comparison is <strong>true</strong>?</qti-prompt>"
    '<qti-simple-choice identifier="lt">1 &lt; 2</qti-simple-choice>'
    '<qti-simple-choice identifier="gt">2 &lt; 1</qti-simple-choice>'
    '<qti-simple-choice identifier="eq">1 <em>equals</em> 2</qti-simple-choice>'
    "</qti-choice-interaction>"
    "</div>"
)


def render_file(examples_dir, name):
    model = load_assessment_item(examples_dir / name)
    return render_item_body_html(model.qti_item_body)


def test_first_example_golden(examples_dir):
    assert render_file(examples_dir, "firstexample.xml") == FIRST_EXAMPLE_HTML


def test_rich_body_golden(examples_dir):
    assert render_file(examples_dir, "choice-rich-body.xml") == RICH_BODY_HTML


def test_no_namespace_prefixes_or_xsi(examples_dir):
    html = render_file(examples_dir, "firstexample.xml")
    assert "ns0:" not in html
    assert "xsi:" not in html
    assert "xmlns" not in html


def test_no_aria_or_default_attribute_flood(examples_dir):
    """``AriabaseDType`` contributes ~45 attributes; none may reach the output."""
    html = render_file(examples_dir, "firstexample.xml")
    assert "aria-" not in html
    assert 'dir="auto"' not in html
    assert 'show-hide="show"' not in html
    assert 'fixed="false"' not in html


def test_max_choices_survives(examples_dir):
    """The regression guard for ``ignore_default_attributes``.

    ``max-choices="1"`` equals the XSD default, so xsdata drops it when
    ``ignore_default_attributes`` is on --- and the front end then cannot tell a
    single-answer interaction from a multi-select.
    """
    html = render_file(examples_dir, "firstexample.xml")
    assert 'max-choices="1"' in html


def test_mixed_content_keeps_trailing_text(examples_dir):
    """The ``.`` after ``</strong>`` is exactly what the old renderer mangled."""
    html = render_file(examples_dir, "firstexample.xml")
    assert "<strong>crazy</strong>." in html


def test_void_elements_have_no_closing_tag(examples_dir):
    html = render_file(examples_dir, "choice-rich-body.xml")
    assert "<br>" in html
    assert "</br>" not in html


def test_text_escaping_leaves_apostrophes_readable(examples_dir):
    html = render_file(examples_dir, "choice-rich-body.xml")
    assert "I'm fine" in html
    assert "&#x27;" not in html
    assert "1 &lt; 2" in html
    assert "Tom &amp; Jerry" in html


def test_attribute_values_are_quote_escaped():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
     identifier="attr" title="Attr" time-dependent="false">
     <qti-response-declaration base-type="identifier" cardinality="single"
      identifier="RESPONSE"/>
     <qti-item-body>
      <qti-choice-interaction max-choices="1" response-identifier="RESPONSE">
       <qti-simple-choice identifier="A&amp;B">choice</qti-simple-choice>
      </qti-choice-interaction>
     </qti-item-body>
    </qti-assessment-item>"""

    html = render_item_body_html(load_assessment_item(xml).qti_item_body)
    assert 'identifier="A&amp;B"' in html


def test_empty_body_renders_empty():
    assert render_item_body_html(None) == ""


def test_wrapper_class_can_be_disabled(examples_dir):
    html = render_item_body_html(
        load_assessment_item(examples_dir / "firstexample.xml").qti_item_body,
        wrapper_class=None,
    )
    assert html.startswith("<p>")
    assert "qti-item-body" not in html


def test_unsupported_element_raises():
    """Silently dropping content would hand the candidate a different question."""
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
     identifier="unsupported" title="Unsupported" time-dependent="false">
     <qti-item-body>
      <section><p>inside a section</p></section>
     </qti-item-body>
    </qti-assessment-item>"""

    with pytest.raises(UnsupportedContentError, match="section"):
        render_item_body_html(load_assessment_item(xml).qti_item_body)


@pytest.mark.parametrize(
    ("attrs", "expected"),
    [
        ('max-choices="1" shuffle="true"', "shuffle"),
        ('max-choices="2"', "max-choices"),
    ],
)
def test_unsupported_interaction_config_raises(attrs, expected):
    """Rendering a shuffled or multi-select interaction as-is would misrepresent it."""
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
     identifier="cfg" title="Cfg" time-dependent="false">
     <qti-response-declaration base-type="identifier" cardinality="single"
      identifier="RESPONSE"/>
     <qti-item-body>
      <qti-choice-interaction {attrs} response-identifier="RESPONSE">
       <qti-simple-choice identifier="A">A</qti-simple-choice>
       <qti-simple-choice identifier="B">B</qti-simple-choice>
      </qti-choice-interaction>
     </qti-item-body>
    </qti-assessment-item>"""

    with pytest.raises(UnsupportedContentError, match=expected):
        render_item_body_html(load_assessment_item(xml).qti_item_body)
