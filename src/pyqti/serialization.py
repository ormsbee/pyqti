"""Writing QTI models back out as XML.

The counterpart to :mod:`pyqti.loading`. This exists because pyqti now serves QTI
XML to the front end rather than rendering HTML itself: Citolab's
``<item-container item-url="...">`` fetches and renders the XML, so pyqti's job on
the presentation side is to emit a *presentation-safe* document (see
:mod:`pyqti.redaction`) rather than markup.
"""

from __future__ import annotations

from typing import Any

from xsdata.formats.dataclass.serializers import XmlSerializer

from pyqti._xsdata import CONTEXT, QTI_NAMESPACE, make_serializer_config


def to_qti_xml(model: Any, *, indent: str | None = None) -> str:
    """Serialize a QTI model to XML in the QTI 3.0 default namespace.

    ``indent`` is ``None`` by default because indenting injects whitespace into
    mixed content and so alters candidate-visible prose --- see
    :func:`pyqti._xsdata.make_serializer_config` for exactly how much. Pass
    ``indent="  "`` only for output a human is going to read.
    """
    serializer = XmlSerializer(
        config=make_serializer_config(indent=indent), context=CONTEXT
    )
    return serializer.render(model, ns_map={None: QTI_NAMESPACE})
