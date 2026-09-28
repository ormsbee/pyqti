"""The entry point, and the seam that keeps the extra optional."""

from importlib.metadata import entry_points

from xblock.core import XBlock

from pyqti.xblock.block import QtiAssessmentItemBlock

TAG = "openedx-qti"


def test_entry_point_is_registered_under_the_olx_tag():
    """The entry point NAME is the OLX tag, which is why it is spelled this way."""
    registered = {ep.name: ep for ep in entry_points(group="xblock.v1")}
    assert TAG in registered, f"xblock.v1 entry points: {sorted(registered)}"
    assert registered[TAG].value == "pyqti.xblock.block:QtiAssessmentItemBlock"


def test_the_runtime_can_load_the_block_by_tag():
    """What Studio and the OLX importer actually do."""
    assert XBlock.load_class(TAG) is QtiAssessmentItemBlock


def test_static_assets_are_importable_resources():
    """They must ship in the wheel, which is why static/ is a package."""
    from importlib.resources import files

    for name in ("qti-xblock.js", "qti-xblock.css"):
        text = files("pyqti.xblock.static").joinpath(name).read_text(encoding="utf-8")
        assert text.strip()


def _glue_code() -> str:
    """The glue with comments stripped.

    Checked against code rather than prose: the file's own header *describes*
    what it must not do, and a substring search would happily match that.
    """
    import re
    from importlib.resources import files

    js = files("pyqti.xblock.static").joinpath("qti-xblock.js").read_text()
    js = re.sub(r"/\*.*?\*/", "", js, flags=re.DOTALL)
    return re.sub(r"//[^\n]*", "", js)


def test_the_glue_never_invokes_client_side_scoring():
    """Citolab can score in the browser. It must never be asked to."""
    code = _glue_code()
    assert "processResponse" not in code
    assert "qti-processing" not in code


def test_the_glue_is_scoped_to_the_block_not_the_document():
    """Two of these on one page must not cross-wire."""
    code = _glue_code()
    assert "document.querySelector" not in code
    assert "document.getElementById" not in code
    assert "document.addEventListener" not in code
