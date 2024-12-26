from dataclasses import dataclass, field
from typing import List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.map_entry_dtype import (
    MapEntryDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class MappingDtype:
    """A special class used to create a mapping from a source set of any base-type
    (except file and duration) to a single 'float'.

    Note that mappings from values of base-type 'float' sh- ould be
    avoided due to the difficulty of matching floating point values, see
    the match op- erator for more details. When mapping containers the
    result is the sum of the mapped valu- es from the target set. See
    the MapResponse class for details.
    """

    class Meta:
        name = "MappingDType"

    qti_map_entry: List[MapEntryDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-map-entry",
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
