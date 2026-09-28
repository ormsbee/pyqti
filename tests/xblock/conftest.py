"""Fixtures for the optional XBlock integration.

The whole package is skipped when the ``xblock`` extra is absent, so that
``pip install pyqti`` (no extra) still has a green suite.
"""

import pytest

pytest.importorskip("xblock", reason="requires the optional 'xblock' extra")
pytest.importorskip("web_fragments", reason="requires the optional 'xblock' extra")

from lxml import etree  # noqa: E402
from xblock.fields import ScopeIds  # noqa: E402
from xblock.runtime import DictKeyValueStore, KvsFieldData  # noqa: E402
from xblock.test.tools import TestRuntime  # noqa: E402

from pyqti.xblock.block import QtiAssessmentItemBlock  # noqa: E402


class RecordingRuntime(TestRuntime):
    """TestRuntime, but ``publish`` records instead of raising.

    ``ScorableXBlockMixin._publish_grade`` goes through ``runtime.publish``, so
    a runtime that refuses it cannot test grading at all.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.published = []

    def publish(self, block, event_type, event_data):
        self.published.append((event_type, event_data))

    def handler_url(self, block, handler_name, suffix="", query="", thirdparty=False):
        return f"/handler/{handler_name}"


def build_runtime():
    return RecordingRuntime(
        services={"field-data": KvsFieldData(DictKeyValueStore())}
    )


def build_block(qti_xml=None, runtime=None, **fields):
    """A block wired to a real runtime, optionally pre-loaded with an item."""
    runtime = runtime or build_runtime()
    block = QtiAssessmentItemBlock(
        runtime,
        scope_ids=ScopeIds("learner", "openedx-qti", "def-1", "usage-1"),
    )
    if qti_xml is not None:
        block._store_qti(qti_xml)
    for name, value in fields.items():
        setattr(block, name, value)
    return block


def parse_olx(node, runtime=None, block_class=QtiAssessmentItemBlock):
    """Import an ``<openedx-qti>`` node (or its text) through ``parse_xml``."""
    if isinstance(node, str):
        node = etree.fromstring(node.encode("utf-8"))
    runtime = runtime or build_runtime()
    keys = runtime.id_generator.create_definition("openedx-qti")
    scope_ids = ScopeIds("learner", "openedx-qti", keys, "usage-1")
    return block_class.parse_xml(node, runtime, scope_ids)


def exported(block, url_name="u1"):
    """Export as edx-platform does: it names the node before handing it over."""
    node = etree.Element("openedx-qti", url_name=url_name)
    block.add_xml_to_node(node)
    return node


@pytest.fixture
def runtime():
    return build_runtime()


@pytest.fixture
def block_factory():
    return build_block


@pytest.fixture
def first_example_xml(examples_dir):
    return (examples_dir / "firstexample.xml").read_text(encoding="utf-8")


def call_json(block, handler_name, payload):
    """Drive a @json_handler the way the runtime does.

    json_handler rewrites the method to take a webob Request, so calling it
    directly as a Python method does not work.
    """
    import json

    from webob import Request

    request = Request.blank("/")
    request.method = "POST"
    request.body = json.dumps(payload).encode("utf-8")
    response = block.handle(handler_name, request)
    body = json.loads(response.body) if response.body else {}
    return response.status_code, body


def call_handler(block, handler_name):
    """Drive a raw @handler and return (status, body-as-text)."""
    from webob import Request

    response = block.handle(handler_name, Request.blank("/"))
    return response.status_code, response.body.decode("utf-8")
