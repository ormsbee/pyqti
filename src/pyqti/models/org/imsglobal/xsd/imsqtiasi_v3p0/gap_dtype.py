from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype import (
    BaseSequenceXbaseEmptyDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.gap_dtype_show_hide import (
    GapDtypeShowHide,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class GapDtype(BaseSequenceXbaseEmptyDtype):
    """
    This defines the gap structure that must only appear within a
    'gapMatchInteraction'.
    """

    class Meta:
        name = "GapDType"

    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    template_identifier: None | str = field(
        default=None,
        metadata={
            "name": "template-identifier",
            "type": "Attribute",
        },
    )
    show_hide: GapDtypeShowHide = field(
        default=GapDtypeShowHide.SHOW,
        metadata={
            "name": "show-hide",
            "type": "Attribute",
        },
    )
    match_group: list[str] = field(
        default_factory=list,
        metadata={
            "name": "match-group",
            "type": "Attribute",
            "tokens": True,
        },
    )
    required: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
