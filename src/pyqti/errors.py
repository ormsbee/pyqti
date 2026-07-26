"""Exception hierarchy for pyqti.

Everything pyqti raises deliberately derives from :class:`PyQtiError`, so callers
can distinguish "this content is beyond what pyqti implements" from a genuine bug.

The unsupported-* errors are load-bearing rather than defensive. An assessment
engine that silently ignores content it does not understand will happily render a
question without its diagram, or leave an outcome at its default and mark every
answer correct. Both mis-grade the candidate, so pyqti refuses instead.
"""


class PyQtiError(Exception):
    """Base class for every error pyqti raises on purpose."""


class UnsupportedQtiFeature(PyQtiError):
    """Base for 'valid QTI, but pyqti does not implement it yet'."""


class UnsupportedContentError(UnsupportedQtiFeature):
    """An element in an item body that the renderer does not know how to emit."""


class UnsupportedExpressionError(UnsupportedQtiFeature):
    """A response-processing expression the compiler does not implement."""


class UnsupportedRuleError(UnsupportedQtiFeature):
    """A response-processing rule the compiler does not implement."""


class UnsupportedTemplateError(UnsupportedQtiFeature):
    """A response-processing template URI pyqti has no vendored copy of."""


class QtiTypeError(PyQtiError):
    """A QTI runtime type violation, e.g. comparing an identifier to a float."""


class QtiStructureError(PyQtiError):
    """The document parsed, but is structurally invalid for what it claims to be."""
