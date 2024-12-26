from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype import (
    BaseSequenceXbaseEmptyDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.hotspot_choice_dtype_shape import (
    HotspotChoiceDtypeShape,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.hotspot_choice_dtype_show_hide import (
    HotspotChoiceDtypeShowHide,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class HotspotChoiceDtype(BaseSequenceXbaseEmptyDtype):
    """The definition of a hotspot choices that can be selected by the candidate.

    If the delivery system does not support pointer-based selection then
    the order in which the choices are g- iven must be the order in
    which they are offered to the candidate for selection. For exam-
    ple, the 'tab order' in simple keyboard navigation. If hotspots
    overlap then those listed first hide overlapping hotspots that
    appear later. The default hotspot, if defined, must appear last.
    """

    class Meta:
        name = "HotspotChoiceDType"

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
    show_hide: HotspotChoiceDtypeShowHide = field(
        default=HotspotChoiceDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    shape: Optional[HotspotChoiceDtypeShape] = field(
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
