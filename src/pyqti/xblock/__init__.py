"""Open edX XBlock integration --- optional, behind the ``xblock`` extra.

Nothing here is imported by ``pyqti`` itself. ``import pyqti`` and
``from pyqti import ItemSession`` work identically whether or not the extra is
installed; the dependency runs XBlock -> pyqti and never the reverse. That is
why none of these names appear in ``pyqti.__init__._EXPORTS``.

This module is deliberately *not* imported here. ``import pyqti.xblock`` must
stay cheap and must not require XBlock to be installed --- only
``pyqti.xblock.block`` pulls in the framework.

Install with::

    pip install pyqti[xblock]
"""
