from dataclasses import dataclass, field
from typing import List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.associable_hotspot_dtype_shape import (
    AssociableHotspotDtypeShape,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.associable_hotspot_dtype_show_hide import (
    AssociableHotspotDtypeShowHide,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype import (
    BaseSequenceXbaseEmptyDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class AssociableHotspotDtype(BaseSequenceXbaseEmptyDtype):
    """
    This is used to define the hotspots that are associated with the features in
    the 'graphic- AssociateInteraction' and 'graphicGapMatchInteraction'
    interactions.
    """

    class Meta:
        name = "AssociableHotspotDType"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    template_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
        },
    )
    show_hide: AssociableHotspotDtypeShowHide = field(
        default=AssociableHotspotDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    match_group: List[str] = field(
        default_factory=list,
        metadata={
            "name": "match-group",
            "type": "Attribute",
            "tokens": True,
        },
    )
    shape: Optional[AssociableHotspotDtypeShape] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    coords: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"(([0-9]+%?[,]){2}([0-9]+%?))|(([0-9]+%?[,]){3}([0-9]+%?))|(([0-9]+%?[,]){2}(([0-9]+%?[,]){2})+([0-9]+%?[,])([0-9]+%?))",
        },
    )
    hotspot_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "hotspot-label",
            "type": "Attribute",
        },
    )
    match_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "match-max",
            "type": "Attribute",
            "required": True,
        },
    )
    match_min: int = field(
        default=0,
        metadata={
            "name": "match-min",
            "type": "Attribute",
        },
    )
