"""A stdlib HTTP harness that renders and grades items in a real browser.

Routes::

    GET  /                                 index of loaded items
    GET  /items/{identifier}               full HTML page
    GET  /static/{qti.js,qti.css}          front-end assets
    POST /api/items/{identifier}/responses grade a submission (JSON)

**The JSON contract** is the part worth designing carefully, because a React
implementation of the interaction should be able to adopt it unchanged::

    request   {"responses": {"RESPONSE": "A"}}
    200       {"item": "firstexample", "outcomes": {"SCORE": 1.0},
               "completion_status": "completed", "valid": true, "errors": []}
    422       {"error": {"type": "UnsupportedExpressionError", "message": "..."}}

Encoding rules: keys are QTI identifiers with no envelope; a JSON scalar is single
cardinality; ``null`` or an absent key is NULL; an array is multiple/ordered
(reserved, not yet implemented); an object is a record. ``float`` outcomes are JSON
numbers, so ``SCORE`` is ``1.0`` and never ``"1"``.

There is deliberately **no** ``{"cardinality":..., "base_type":..., "value":...}``
wrapper. Adding keys to a JSON object is never a breaking change, so
``completion_status``, feedback and attempt counters stay additive --- whereas
introducing a wrapper later would be exactly the rewrite this shape avoids.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Iterable
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from importlib.resources import files
from pathlib import Path
from typing import Any

from pyqti.errors import PyQtiError
from pyqti.item import ItemDefinition
from pyqti.loading import load_assessment_item
from pyqti.render.html import render_item_body_html
from pyqti.session import ItemSession

DEFAULT_EXAMPLES = Path(__file__).resolve().parents[3] / "examples"

_STATIC_TYPES = {".js": "application/javascript", ".css": "text/css"}


def load_items(paths: Iterable[Path]) -> dict[str, ItemDefinition]:
    """Parse each path into an :class:`ItemDefinition`, keyed by its identifier."""
    items: dict[str, ItemDefinition] = {}
    for path in sorted(paths):
        item = ItemDefinition.from_model(load_assessment_item(path))
        items[item.identifier] = item
    return items


def build_item_payload(item: ItemDefinition) -> dict[str, Any]:
    """The metadata blob embedded in the page and reusable as a JSON endpoint.

    Computing it here means a future ``GET /api/items/{id}`` is a move of this
    function rather than a new design.
    """
    return {
        "item": item.identifier,
        "title": item.title,
        "response_declarations": {
            identifier: {
                "cardinality": declaration.cardinality.value,
                "base_type": (
                    declaration.base_type.value if declaration.base_type else None
                ),
            }
            for identifier, declaration in item.response_declarations.items()
        },
        "interactions": [
            {
                "type": "choice",
                "response_identifier": interaction.response_identifier,
                "max_choices": interaction.max_choices,
                "min_choices": interaction.min_choices,
                "shuffle": interaction.shuffle,
                "orientation": interaction.orientation,
                "choices": [
                    {"identifier": choice} for choice in interaction.choice_identifiers
                ],
            }
            for interaction in item.interactions
        ],
        "score_endpoint": f"/api/items/{item.identifier}/responses",
    }


def render_page(item: ItemDefinition) -> str:
    body = render_item_body_html(item.item_body)
    payload = json.dumps(build_item_payload(item), indent=2)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{item.title} &mdash; pyqti demo</title>
<link rel="stylesheet" href="/static/qti.css">
</head>
<body>
<main>
<p class="crumb"><a href="/">&larr; all items</a></p>
<h1>{item.title}</h1>
<form id="qti-form" data-endpoint="/api/items/{item.identifier}/responses">
{body}
<button type="submit">Submit</button>
</form>
<output id="qti-result" hidden></output>
</main>
<script type="application/json" id="qti-item">
{payload}
</script>
<script src="/static/qti.js"></script>
</body>
</html>
"""


def render_index(items: dict[str, ItemDefinition]) -> str:
    rows = "\n".join(
        f'<li><a href="/items/{identifier}">{item.title}</a> '
        f"<code>{identifier}</code></li>"
        for identifier, item in items.items()
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>pyqti demo</title>
<link rel="stylesheet" href="/static/qti.css">
</head>
<body>
<main>
<h1>pyqti demo</h1>
<p>Single-answer multiple choice items, rendered and graded by pyqti.</p>
<ul class="items">
{rows}
</ul>
</main>
</body>
</html>
"""


class QtiDemoHandler(BaseHTTPRequestHandler):
    """One handler, ``if``/``elif`` routing, no abstraction."""

    server_version = "pyqti-demo"
    items: dict[str, ItemDefinition] = {}

    # -- helpers -------------------------------------------------------- #

    def _send(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, status: int, html: str) -> None:
        self._send(status, html.encode("utf-8"), "text/html; charset=utf-8")

    def _send_json(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self._send(status, body, "application/json")

    def _not_found(self) -> None:
        self._send_json(404, {"error": {"type": "NotFound", "message": self.path}})

    def log_message(self, format: str, *args: Any) -> None:  # noqa: A002
        # Quieter than the default, and keeps test output readable.
        return

    # -- routing -------------------------------------------------------- #

    def do_GET(self) -> None:  # noqa: N802
        path = self.path.split("?", 1)[0]

        if path == "/":
            self._send_html(200, render_index(self.items))
        elif path.startswith("/static/"):
            self._serve_static(path.removeprefix("/static/"))
        elif path.startswith("/items/"):
            identifier = path.removeprefix("/items/").strip("/")
            item = self.items.get(identifier)
            if item is None:
                self._not_found()
            else:
                self._send_html(200, render_page(item))
        else:
            self._not_found()

    def do_POST(self) -> None:  # noqa: N802
        path = self.path.split("?", 1)[0]
        if not (path.startswith("/api/items/") and path.endswith("/responses")):
            self._not_found()
            return

        identifier = path.removeprefix("/api/items/").removesuffix("/responses")
        item = self.items.get(identifier)
        if item is None:
            self._not_found()
            return

        try:
            length = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(length) if length else b"{}"
            request = json.loads(raw or b"{}")
            responses = request.get("responses") or {}
            if not isinstance(responses, dict):
                raise ValueError("'responses' must be an object")
        except (ValueError, json.JSONDecodeError) as exc:
            self._send_json(400, {"error": {"type": "BadRequest", "message": str(exc)}})
            return

        try:
            session = ItemSession(item)
            validity = session.validate_responses(responses)
            outcomes = session.submit(responses)
        except PyQtiError as exc:
            self._send_json(
                422, {"error": {"type": type(exc).__name__, "message": str(exc)}}
            )
            return

        self._send_json(
            200,
            {
                "item": item.identifier,
                "outcomes": outcomes,
                "completion_status": session.completion_status,
                "valid": validity.valid,
                "errors": validity.errors,
            },
        )

    def _serve_static(self, name: str) -> None:
        if "/" in name or not name.endswith((".js", ".css")):
            self._not_found()
            return
        try:
            text = files("pyqti.demo.static").joinpath(name).read_text(encoding="utf-8")
        except (FileNotFoundError, ModuleNotFoundError):
            self._not_found()
            return
        suffix = name[name.rfind(".") :]
        self._send(
            200,
            text.encode("utf-8"),
            f"{_STATIC_TYPES[suffix]}; charset=utf-8",
        )


def make_server(
    items: dict[str, ItemDefinition], host: str = "127.0.0.1", port: int = 8000
) -> ThreadingHTTPServer:
    handler = type("BoundQtiDemoHandler", (QtiDemoHandler,), {"items": items})
    return ThreadingHTTPServer((host, port), handler)


def serve(
    examples: Path = DEFAULT_EXAMPLES, host: str = "127.0.0.1", port: int = 8000
) -> None:
    items = load_items(examples.glob("*.xml"))
    if not items:
        raise SystemExit(f"no QTI items found in {examples}")

    server = make_server(items, host, port)
    print(f"pyqti demo serving {len(items)} item(s) at http://{host}:{port}/")
    for identifier in items:
        print(f"  http://{host}:{port}/items/{identifier}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopping")
    finally:
        server.server_close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="qti-demo", description="Render and grade QTI items in a browser."
    )
    parser.add_argument("--examples", type=Path, default=DEFAULT_EXAMPLES)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args(argv)

    serve(examples=args.examples, host=args.host, port=args.port)
    return 0
