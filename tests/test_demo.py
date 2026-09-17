"""The demo harness over a real socket.

The only test that exercises delivery end to end over HTTP, so it is worth the thread.
Note what it *cannot* cover: rendering now happens in the browser, so these tests
prove pyqti serves the right XML and grades correctly, not that the item displays.
"""

import json
import threading
import urllib.error
import urllib.request
from collections.abc import Iterator

import pytest

from pyqti.demo.server import build_item_payload, load_items, make_server
from pyqti.item import ItemDefinition
from pyqti.loading import load_assessment_item


@pytest.fixture(scope="module")
def base_url(request) -> Iterator[str]:
    examples = request.path.parent.parent / "examples"
    server = make_server(load_items(examples.glob("*.xml")), "127.0.0.1", 0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_address[1]}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def get(url: str) -> tuple[int, str]:
    with urllib.request.urlopen(url) as response:  # noqa: S310
        return response.status, response.read().decode("utf-8")


def post_json(url: str, payload: dict) -> tuple[int, dict]:
    request = urllib.request.Request(  # noqa: S310
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request) as response:  # noqa: S310
            return response.status, json.loads(response.read())
    except urllib.error.HTTPError as error:
        return error.code, json.loads(error.read())


def test_index_lists_items(base_url):
    status, body = get(f"{base_url}/")
    assert status == 200
    assert "firstexample" in body
    assert "choice-if-only" in body


def test_item_page_hosts_the_web_components(base_url):
    """The page ships no item markup --- only the components and a URL to fetch."""
    status, body = get(f"{base_url}/items/firstexample")
    assert status == 200

    assert "cdn.jsdelivr.net/npm/@citolab/qti-components@" in body
    assert "/qti-item/+esm" in body
    # qti-item only defines the qti-item/item-container wrappers. The structural
    # elements (qti-assessment-item, qti-item-body, ...) come from qti-elements;
    # without it the browser fetches the XML and renders nothing.
    assert "/qti-elements/+esm" in body
    assert "/qti-interactions/+esm" in body
    assert '<item-container item-url="/items/firstexample/item.xml">' in body, (
        "the renderer needs a URL to fetch the item from"
    )
    assert '<script type="application/json" id="qti-item-meta">' in body

    # pyqti no longer renders, so the question text must NOT be in the page.
    assert "Epinephrine" not in body


def test_item_page_omits_client_side_scoring_and_answer_reveal(base_url):
    """Defence in depth: the page must not load anything that scores or reveals.

    Redaction is the primary control --- the served XML has no response processing
    and no correct response to act on --- but these components have no business being
    on an exam page regardless.
    """
    _, body = get(f"{base_url}/items/firstexample")

    assert "/qti-processing/+esm" not in body
    assert "qti-processing" not in body
    for reveal in (
        "item-show-correct-response",
        "item-show-candidate-correction",
        "item-correct-response-mode",
    ):
        assert reveal not in body


def test_static_assets_are_served(base_url):
    status, js = get(f"{base_url}/static/qti.js")
    assert status == 200
    # Glue only: no custom element definitions, no scoring.
    assert "customElements.define" not in js
    assert "processResponse" not in js
    assert "qti-item-context-updated" in js
    assert "dataset.endpoint" in js

    status, css = get(f"{base_url}/static/qti.css")
    assert status == 200
    assert "#qti-result" in css


def test_grading_a_correct_response(base_url):
    status, payload = post_json(
        f"{base_url}/api/items/firstexample/responses", {"responses": {"RESPONSE": "A"}}
    )
    assert status == 200
    assert payload["item"] == "firstexample"
    assert payload["outcomes"] == {"SCORE": 1.0}
    assert payload["completion_status"] == "completed"
    assert payload["valid"] is True
    assert payload["errors"] == []


def test_grading_an_incorrect_response(base_url):
    """The over-the-wire form of the SCORE-default-of-1 trap."""
    status, payload = post_json(
        f"{base_url}/api/items/firstexample/responses", {"responses": {"RESPONSE": "B"}}
    )
    assert status == 200
    assert payload["outcomes"] == {"SCORE": 0.0}


def test_score_is_a_json_number_not_a_string(base_url):
    status, payload = post_json(
        f"{base_url}/api/items/firstexample/responses", {"responses": {"RESPONSE": "A"}}
    )
    assert status == 200
    assert isinstance(payload["outcomes"]["SCORE"], float)


def test_unanswered_response_is_graded_but_flagged_invalid(base_url):
    """Validity is reported, never enforced --- response processing still runs."""
    status, payload = post_json(
        f"{base_url}/api/items/firstexample/responses", {"responses": {}}
    )
    assert status == 200
    assert payload["outcomes"] == {"SCORE": 0.0}
    assert payload["completion_status"] == "incomplete"
    assert payload["valid"] is False
    assert any("min-choices" in error for error in payload["errors"])


def test_undeclared_choice_is_graded_but_flagged(base_url):
    status, payload = post_json(
        f"{base_url}/api/items/firstexample/responses", {"responses": {"RESPONSE": "Z"}}
    )
    assert status == 200
    assert payload["outcomes"] == {"SCORE": 0.0}
    assert payload["valid"] is False


def test_unknown_item_is_404(base_url):
    status, _ = post_json(f"{base_url}/api/items/nope/responses", {"responses": {}})
    assert status == 404

    with pytest.raises(urllib.error.HTTPError) as excinfo:
        get(f"{base_url}/items/nope")
    assert excinfo.value.code == 404


def test_malformed_json_is_400(base_url):
    request = urllib.request.Request(  # noqa: S310
        f"{base_url}/api/items/firstexample/responses",
        data=b"{not json",
        headers={"Content-Type": "application/json"},
    )
    with pytest.raises(urllib.error.HTTPError) as excinfo:
        urllib.request.urlopen(request)  # noqa: S310
    assert excinfo.value.code == 400


def test_page_provides_every_hook_the_javascript_queries(base_url):
    """Pins the seam between the page and ``qti.js``.

    Nothing else in the suite would catch a renamed id: the Python side would keep
    passing its own tests while the page quietly stopped grading in a browser. Each
    assertion corresponds to a lookup in ``pyqti/demo/static/qti.js``.

    This is weaker cover than it used to be, because the item markup is now produced
    in the browser rather than here. A real browser check is the only thing that can
    confirm the item actually renders.
    """
    _, page = get(f"{base_url}/items/firstexample")

    assert 'id="qti-form"' in page
    assert 'data-endpoint="/api/items/firstexample/responses"' in page
    assert 'id="qti-result"' in page
    assert 'src="/static/qti.js"' in page

    _, js = get(f"{base_url}/static/qti.js")
    for reference in (
        'getElementById("qti-form")',
        'getElementById("qti-result")',
        '"qti-assessment-item"',  # querySelector for the rendered item
        "dataset.endpoint",
        "qti-item-context-updated",
    ):
        assert reference in js, f"qti.js no longer references {reference}"


def test_item_xml_route_serves_redacted_xml(base_url):
    """The route Citolab fetches must never contain the answer.

    ``tests/test_redaction.py`` proves redaction works; this proves the server
    actually uses it on the path the browser hits.
    """
    status, xml = get(f"{base_url}/items/firstexample/item.xml")
    assert status == 200

    assert "qti-correct-response" not in xml
    assert "qti-response-processing" not in xml
    assert "qti-outcome-declaration" not in xml

    # ...while still being a usable question.
    assert "Epinephrine" in xml
    assert xml.count("<qti-simple-choice") == 4
    assert 'response-identifier="RESPONSE"' in xml


def test_unknown_item_subpath_is_404(base_url):
    """Only ``item.xml`` is served under an item; nothing else is reachable."""
    for path in (
        "/items/firstexample/secrets.xml",
        "/items/firstexample/item.xml/extra",
        "/items/nope/item.xml",
    ):
        with pytest.raises(urllib.error.HTTPError) as excinfo:
            get(f"{base_url}{path}")
        assert excinfo.value.code == 404, path


def test_item_payload_shape(examples_dir):
    item = ItemDefinition.from_model(
        load_assessment_item(examples_dir / "firstexample.xml")
    )
    payload = build_item_payload(item)

    assert payload["item"] == "firstexample"
    assert payload["response_declarations"]["RESPONSE"] == {
        "cardinality": "single",
        "base_type": "identifier",
    }
    (interaction,) = payload["interactions"]
    assert interaction["type"] == "choice"
    assert interaction["response_identifier"] == "RESPONSE"
    assert interaction["max_choices"] == 1
    assert interaction["choices"] == [
        {"identifier": "A"},
        {"identifier": "B"},
        {"identifier": "C"},
        {"identifier": "D"},
    ]
    assert payload["score_endpoint"] == "/api/items/firstexample/responses"

    # The payload must be JSON-serialisable as-is.
    json.dumps(payload)
