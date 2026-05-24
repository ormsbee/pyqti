from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.area_map_entry_dtype_shape import (
    AreaMapEntryDtypeShape,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class AreaMapEntryDtype(EmptyPrimitiveTypeDtype):
    """
    The map is defined by a set of qti-area-map-entry objects, each of
    which maps an area of the coordinate space onto a single float.

    When mapping points each area is tested in turn, with those listed
    first taking priority in the case where areas overlap and a point falls
    in the intersection.
    """

    class Meta:
        name = "AreaMapEntryDType"

    shape: AreaMapEntryDtypeShape = field(
        metadata={
            "type": "Attribute",
        }
    )
    coords: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"(([0-9]+%?[,]){2}([0-9]+%?))|(([0-9]+%?[,]){3}([0-9]+%?))|(([0-9]+%?[,]){2}(([0-9]+%?[,]){2})+([0-9]+%?[,])([0-9]+%?))",
        }
    )
    mapped_value: float = field(
        metadata={
            "name": "mapped-value",
            "type": "Attribute",
        }
    )
