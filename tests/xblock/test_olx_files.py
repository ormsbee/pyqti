"""Course export: each block in its own file, with a pointer left in the parent."""

import io
import posixpath

import pytest
from lxml import etree

from pyqti.errors import QtiStructureError

from .conftest import build_block, build_runtime, exported, parse_olx

#: An item whose whitespace a careless export or import would change. It is
#: minified on purpose: libxml2 only pretty-prints elements that have no
#: whitespace of their own, and then puts some between "a" and "b". The one
#: space it does have, between "c" and "d", is what a parser that strips blank
#: text (the platform's does) takes away.
INLINE = (
    '<qti-assessment-item xmlns="http://www.imsglobal.org/xsd/imsqtiasi_v3p0"'
    ' identifier="inline" title="Inline" time-dependent="false">'
    '<qti-response-declaration identifier="RESPONSE" cardinality="single"'
    ' base-type="identifier">'
    "<qti-correct-response><qti-value>A</qti-value></qti-correct-response>"
    "</qti-response-declaration>"
    '<qti-outcome-declaration identifier="SCORE" cardinality="single"'
    ' base-type="float"/>'
    "<qti-item-body>"
    "<p><em>a</em><strong>b</strong></p>"
    "<p><em>c</em> <strong>d</strong></p>"
    '<qti-choice-interaction response-identifier="RESPONSE" max-choices="1">'
    '<qti-simple-choice identifier="A">Alpha</qti-simple-choice>'
    '<qti-simple-choice identifier="B">Beta</qti-simple-choice>'
    "</qti-choice-interaction>"
    "</qti-item-body>"
    "<qti-response-processing"
    ' template="https://purl.imsglobal.org/spec/qti/v3p0/rptemplates/match_correct"/>'
    "</qti-assessment-item>"
)

PATH = "openedx-qti/u1.xml"


class MemoryFS:
    """The slice of PyFilesystem2 that course export and import hand a block.

    edx-platform passes real ``fs`` objects. The ``fs`` package cannot be
    imported here, because it needs setuptools' ``pkg_resources``, so this
    implements just the calls the block makes, including ``fs``'s refusal to
    write into a directory that does not exist.
    """

    def __init__(self):
        self.files = {}
        self.dirs = {""}

    def makedirs(self, path, recreate=False):
        if path in self.dirs and not recreate:
            raise FileExistsError(path)
        self.dirs.add(path)

    def exists(self, path):
        return path in self.files or path in self.dirs

    def open(self, path, mode="r"):
        if "w" not in mode:
            return io.BytesIO(self.files[path])
        if posixpath.dirname(path) not in self.dirs:
            raise FileNotFoundError(path)
        files = self.files

        class Written(io.BytesIO):
            def close(self):
                files[path] = self.getvalue()
                super().close()

        return Written()


def course_runtime():
    """A runtime with course export's and import's filesystems, as one."""
    runtime = build_runtime()
    runtime.export_fs = runtime.resources_fs = MemoryFS()
    return runtime


def test_course_export_leaves_only_a_pointer_in_the_parent():
    block = build_block(INLINE, runtime=course_runtime(), max_attempts=3)
    vertical = etree.Element("vertical")
    child = etree.SubElement(vertical, "openedx-qti", url_name="u1")
    block.add_xml_to_node(child)
    assert etree.tostring(vertical) == (
        b'<vertical><openedx-qti url_name="u1"/></vertical>'
    )


def test_the_definition_file_is_the_wrapper_and_its_item():
    runtime = course_runtime()
    exported(build_block(INLINE, runtime=runtime, max_attempts=3))
    definition = etree.fromstring(runtime.export_fs.files[PATH])
    assert definition.tag == "openedx-qti"
    assert definition.get("max_attempts") == "3"
    assert "url_name" not in definition.attrib, "the name belongs to the pointer"
    (item,) = definition
    assert etree.QName(item).localname == "qti-assessment-item"


def test_course_import_follows_the_pointer_back():
    runtime = course_runtime()
    block = build_block(
        INLINE, runtime=runtime, display_name="Inline", max_attempts=3, weight=2.5
    )
    again = parse_olx(exported(block), runtime=runtime)
    for name in ("qti_xml", "display_name", "max_attempts", "weight"):
        assert getattr(again, name) == getattr(block, name), name


def test_whitespace_between_inline_elements_survives_the_file():
    """Both directions: not indented on the way out, not stripped on the way in."""
    runtime = course_runtime()
    block = build_block(INLINE, runtime=runtime)
    again = parse_olx(exported(block), runtime=runtime)
    assert again.qti_xml == block.qti_xml
    written = runtime.export_fs.files[PATH].decode("utf-8")
    assert "<em>a</em><strong>b</strong>" in written
    assert "<em>c</em> <strong>d</strong>" in written


def test_the_library_serializer_gets_one_inline_node():
    """What edx-platform's override_export_fs does to get a single node."""
    runtime = course_runtime()
    block = build_block(INLINE, runtime=runtime)
    block.export_to_file = lambda: False
    node = exported(block)
    (item,) = node
    assert etree.QName(item).localname == "qti-assessment-item"
    assert not runtime.export_fs.exists(PATH)


def test_an_empty_block_round_trips_through_a_file():
    runtime = course_runtime()
    block = build_block(runtime=runtime, display_name="Draft")
    pointer = exported(block)
    assert dict(pointer.attrib) == {"url_name": "u1"}
    again = parse_olx(pointer, runtime=runtime)
    assert (again.qti_xml, again.display_name) == ("", "Draft")


@pytest.mark.parametrize(
    "runtime",
    [build_runtime, course_runtime],
    ids=["no filesystem", "no such file (split, library runtime)"],
)
def test_a_bare_name_without_its_file_is_an_empty_block(runtime):
    block = parse_olx('<openedx-qti url_name="u9"/>', runtime=runtime())
    assert block.qti_xml == ""


def test_a_pointer_to_something_else_is_refused():
    runtime = course_runtime()
    runtime.resources_fs.files[PATH] = b"<problem/>"
    with pytest.raises(QtiStructureError, match="expected a <openedx-qti>"):
        parse_olx('<openedx-qti url_name="u1"/>', runtime=runtime)
