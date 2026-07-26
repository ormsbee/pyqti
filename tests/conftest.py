from pathlib import Path

import pytest

from pyqti.loading import load_assessment_item

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"


@pytest.fixture
def examples_dir() -> Path:
    return EXAMPLES


@pytest.fixture
def first_example():
    """The canonical 1EdTech Beginner's Guide item: single-answer MC, match_correct."""
    return load_assessment_item(EXAMPLES / "firstexample.xml")
