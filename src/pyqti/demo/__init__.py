"""A minimal end-to-end demo harness for pyqti.

Deliberately stdlib-only (``http.server``) and deliberately small: its job is to
prove that rendering and grading work together against a real browser, not to be a
delivery engine.
"""

from pyqti.demo.server import build_item_payload, main, serve

__all__ = ["build_item_payload", "main", "serve"]
