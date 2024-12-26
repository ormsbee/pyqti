from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass
class Struct:
    class Meta:
        name = "struct"
        namespace = "http://www.w3.org/2001/10/synthesis"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
