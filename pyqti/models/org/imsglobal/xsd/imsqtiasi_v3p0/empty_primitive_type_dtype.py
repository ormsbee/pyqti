from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class EmptyPrimitiveTypeDtype:
    class Meta:
        name = "EmptyPrimitiveTypeDType"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
