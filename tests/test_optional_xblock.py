"""The core library must not depend on the optional XBlock extra.

These run whether or not ``pyqti[xblock]`` is installed --- that is the point.
"""

import subprocess
import sys

import pyqti


def test_public_api_does_not_advertise_the_xblock():
    """``__all__`` is derived from ``_EXPORTS``; a name most installs cannot
    resolve has no business in it."""
    assert not [name for name in pyqti.__all__ if "block" in name.lower()]
    assert all(
        not module.startswith("pyqti.xblock")
        for module in pyqti._EXPORTS.values()
    )


def test_importing_pyqti_does_not_import_xblock():
    """A bare import must not pull in the framework, even when it is installed."""
    code = (
        "import sys; import pyqti; "
        "from pyqti import ItemSession, presentation_xml; "
        "assert 'xblock' not in sys.modules, sorted(m for m in sys.modules "
        "if m.startswith('xblock')); "
        "print('clean')"
    )
    result = subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, result.stderr
    assert "clean" in result.stdout


def test_importing_the_xblock_package_does_not_import_the_framework():
    """``pyqti.xblock`` itself stays cheap; only ``.block`` needs XBlock."""
    code = (
        "import sys; import pyqti.xblock; "
        "assert 'xblock.core' not in sys.modules; print('clean')"
    )
    result = subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, result.stderr
    assert "clean" in result.stdout
