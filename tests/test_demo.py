"""The demo harness over a real socket.

This is the only test that exercises what the task actually asked for --- render and
grade, end to end, over HTTP --- so it is worth the thread.
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


def test_item_page_renders_and_embeds_metadata(base_url):
    status, body = get(f"{base_url}/items/firstexample")
    assert status == 200
    assert "<qti-choice-interaction" in body
    assert 'max-choices="1"' in body
    assert '<script type="application/json" id="qti-item">' in body
    assert "Epinephrine" in body


def test_static_assets_are_served(base_url):
    status, js = get(f"{base_url}/static/qti.js")
    assert status == 200
    assert 'customElements.define("qti-choice-interaction"' in js

    status, css = get(f"{base_url}/static/qti.css")
    assert status == 200
    assert ".qti-choice" in css


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
    _, raw = get(f"{base_url}/items/firstexample")
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
    """Pins the seam between the server-rendered HTML and ``qti.js``.

    Nothing else in the suite would catch a renamed id or attribute: the Python side
    would still pass its own tests while the page quietly stopped grading in a
    browser. Each assertion here corresponds to a selector in
    ``pyqti/demo/static/qti.js``.
    """
    _, page = get(f"{base_url}/items/firstexample")

    # document.getElementById("qti-form") / form.dataset.endpoint
    assert 'id="qti-form"' in page
    assert 'data-endpoint="/api/items/firstexample/responses"' in page
    # document.getElementById("qti-result")
    assert 'id="qti-result"' in page
    # <script src="/static/qti.js">
    assert '<script src="/static/qti.js">' in page

    # customElements.define("qti-choice-interaction") + its attribute reads
    interaction = page[page.index("<qti-choice-interaction") :]
    interaction = interaction[: interaction.index("</qti-choice-interaction>")]
    assert 'response-identifier="RESPONSE"' in interaction
    assert 'max-choices="1"' in interaction
    # querySelectorAll(":scope > qti-simple-choice") with an identifier to submit
    assert interaction.count("<qti-simple-choice identifier=") == 4

    _, js = get(f"{base_url}/static/qti.js")
    for selector in (
        'getElementById("qti-form")',
        'getElementById("qti-result")',
        '":scope > qti-simple-choice"',
        "dataset.endpoint",
        "response-identifier",
        "max-choices",
    ):
        assert selector in js, f"qti.js no longer references {selector}"


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
