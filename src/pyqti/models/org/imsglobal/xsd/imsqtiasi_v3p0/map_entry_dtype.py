from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class MapEntryDtype(EmptyPrimitiveTypeDtype):
    """
    This is a part of the mapping functionality.

    The map is defined by a set of qti-map-entry, each of which maps a
    single value from the source set onto a single float.
    """

    class Meta:
        name = "MapEntryDType"

    map_key: str = field(
        metadata={
            "name": "map-key",
            "type": "Attribute",
        }
    )
    mapped_value: float = field(
        metadata={
            "name": "mapped-value",
            "type": "Attribute",
        }
    )
    case_sensitive: bool = field(
        default=False,
        metadata={
            "name": "case-sensitive",
            "type": "Attribute",
        },
    )
