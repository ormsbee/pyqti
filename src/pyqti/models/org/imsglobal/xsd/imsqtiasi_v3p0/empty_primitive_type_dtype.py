from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class EmptyPrimitiveTypeDtype:
    class Meta:
        name = "EmptyPrimitiveTypeDType"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
