from dataclasses import dataclass, field
from typing import List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.area_map_entry_dtype import (
    AreaMapEntryDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class AreaMappingDtype:
    """A special class used to create a mapping from a source set of point values
    to a target set of float values.

    When mapping containers, the result is the sum of the mapped values
    from the target set. See mapResponsePoint for details. The
    attributes have the same meaning as the similarly named attributes
    on mapping.
    """

    class Meta:
        name = "AreaMappingDType"

    qti_area_map_entry: List[AreaMapEntryDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-area-map-entry",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    lower_bound: Optional[float] = field(
        default=None,
        metadata={
            "name": "lower-bound",
            "type": "Attribute",
        },
    )
    upper_bound: Optional[float] = field(
        default=None,
        metadata={
            "name": "upper-bound",
            "type": "Attribute",
        },
    )
    default_value: float = field(
        default=0.0,
        metadata={
            "name": "default-value",
            "type": "Attribute",
        },
    )
