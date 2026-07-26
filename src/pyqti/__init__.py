"""pyqti --- an early implementation of the QTI 3.0 standard for Python.

Currently supports delivering and grading single-answer multiple-choice items:
a ``qti-choice-interaction`` with ``cardinality="single"`` bound to an ``identifier``
response, graded by real response processing (including resolution of the built-in
``match_correct`` template).

pyqti does not render. Presentation is delegated to QTI web components in the browser
(such as `Citolab qti-components <https://github.com/Citolab/qti-components>`_), which
consume QTI XML directly. pyqti's job on that side is to publish a **presentation-safe**
copy of the item --- see :func:`pyqti.redaction.presentation_xml` --- while keeping the
authoritative item, with its correct responses and response processing, server-side.

Typical use::

    from pathlib import Path
    from pyqti import ItemSession, load_assessment_item, presentation_xml

    item = load_assessment_item(Path("item.xml"))

    xml = presentation_xml(item)                    # safe to send to a browser
    outcomes = ItemSession(item).submit({"RESPONSE": "A"})   # -> {"SCORE": 1.0}

Anything QTI defines that pyqti does not implement raises a subclass of
:class:`~pyqti.errors.UnsupportedQtiFeature` rather than being silently ignored ---
an assessment engine that quietly drops content it does not understand mis-grades
candidates.

**Attribute access is lazy** (PEP 562). Importing ``pyqti.models`` costs tens of
megabytes of resident memory, and the README treats that budget as a real design
constraint --- it is why this project uses plain dataclasses rather than Pydantic and
skips the lxml bindings. Re-exporting the API eagerly here would make a bare
``import pyqti`` pay that cost, and would also defeat the ``overhead`` script, whose
whole job is to measure model-import overhead. Names below are resolved on first use.
"""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any

# Imported for type checkers and IDEs only; at runtime __getattr__ resolves these.
# ruff cannot tell they are re-exports because __all__ is derived from _EXPORTS.
if TYPE_CHECKING:  # pragma: no cover
    from pyqti.errors import (  # noqa: F401
        PyQtiError,
        QtiStructureError,
        QtiTypeError,
        UnsupportedContentError,
        UnsupportedExpressionError,
        UnsupportedQtiFeature,
        UnsupportedRuleError,
        UnsupportedTemplateError,
    )
    from pyqti.item import (  # noqa: F401
        ChoiceInteraction,
        ItemDefinition,
        OutcomeDeclaration,
        ResponseDeclaration,
    )
    from pyqti.loading import (  # noqa: F401
        load_assessment_item,
        load_response_processing,
    )
    from pyqti.redaction import (  # noqa: F401
        presentation_xml,
        redact_for_delivery,
    )
    from pyqti.serialization import to_qti_xml  # noqa: F401
    from pyqti.session import ItemSession, ResponseValidity, grade  # noqa: F401
    from pyqti.values import BaseType, Cardinality  # noqa: F401

_EXPORTS: dict[str, str] = {
    "BaseType": "pyqti.values",
    "Cardinality": "pyqti.values",
    "ChoiceInteraction": "pyqti.item",
    "ItemDefinition": "pyqti.item",
    "ItemSession": "pyqti.session",
    "OutcomeDeclaration": "pyqti.item",
    "PyQtiError": "pyqti.errors",
    "QtiStructureError": "pyqti.errors",
    "QtiTypeError": "pyqti.errors",
    "ResponseDeclaration": "pyqti.item",
    "ResponseValidity": "pyqti.session",
    "UnsupportedContentError": "pyqti.errors",
    "UnsupportedExpressionError": "pyqti.errors",
    "UnsupportedQtiFeature": "pyqti.errors",
    "UnsupportedRuleError": "pyqti.errors",
    "UnsupportedTemplateError": "pyqti.errors",
    "grade": "pyqti.session",
    "load_assessment_item": "pyqti.loading",
    "load_response_processing": "pyqti.loading",
    "presentation_xml": "pyqti.redaction",
    "redact_for_delivery": "pyqti.redaction",
    "to_qti_xml": "pyqti.serialization",
}

__all__ = sorted(_EXPORTS)


def __getattr__(name: str) -> Any:
    module_name = _EXPORTS.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    value = getattr(importlib.import_module(module_name), name)
    globals()[name] = value  # cache so later lookups skip __getattr__
    return value


def __dir__() -> list[str]:
    return __all__
