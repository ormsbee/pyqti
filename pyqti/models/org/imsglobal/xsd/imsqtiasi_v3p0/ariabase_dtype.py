from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype_aria_autocomplete import (
    AriabaseDtypeAriaAutocomplete,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype_aria_checked import (
    AriabaseDtypeAriaChecked,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype_aria_current import (
    AriabaseDtypeAriaCurrent,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype_aria_expanded import (
    AriabaseDtypeAriaExpanded,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype_aria_invalid import (
    AriabaseDtypeAriaInvalid,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype_aria_live import (
    AriabaseDtypeAriaLive,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype_aria_orientation import (
    AriabaseDtypeAriaOrientation,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype_aria_pressed import (
    AriabaseDtypeAriaPressed,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype_aria_selected import (
    AriabaseDtypeAriaSelected,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype_aria_sort import (
    AriabaseDtypeAriaSort,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariabase_dtype_role import (
    AriabaseDtypeRole,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.ariarelevant_list_dtype import (
    AriarelevantListDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class AriabaseDtype:
    """This is a base class for all of the ARIA characteristics for a non-empty
    instance.

    It is from this container that all of the other non-empty classes
    inherit their set of ARIA cap- abilities. This set of
    characteristics is taken from the Accessible Rich Internet Applica-
    tions (WAI-ARIA) specification [ARIA, 14], [WAI-ARIA, 17] and [WAI-
    ARIA, 21]. This specif- ication provides an ontology of roles,
    states, and properties that define accessible user interface
    elements and can be used to improve the accessibility and
    interoperability of w- eb content and applications. These semantics
    are designed to allow an author to properly convey user interface
    behaviors and structural information to assistive technologies in d-
    ocument-level markup.
    """

    class Meta:
        name = "ARIABaseDType"

    role: Optional[AriabaseDtypeRole] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    aria_controls: List[str] = field(
        default_factory=list,
        metadata={
            "name": "aria-controls",
            "type": "Attribute",
            "tokens": True,
        },
    )
    aria_describedby: List[str] = field(
        default_factory=list,
        metadata={
            "name": "aria-describedby",
            "type": "Attribute",
            "tokens": True,
        },
    )
    aria_flowto: List[str] = field(
        default_factory=list,
        metadata={
            "name": "aria-flowto",
            "type": "Attribute",
            "tokens": True,
        },
    )
    aria_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "aria-label",
            "type": "Attribute",
        },
    )
    aria_labelledby: List[str] = field(
        default_factory=list,
        metadata={
            "name": "aria-labelledby",
            "type": "Attribute",
            "tokens": True,
        },
    )
    aria_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "aria-level",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    aria_live: AriabaseDtypeAriaLive = field(
        default=AriabaseDtypeAriaLive.OFF,
        metadata={
            "name": "aria-live",
            "type": "Attribute",
        },
    )
    aria_orientation: AriabaseDtypeAriaOrientation = field(
        default=AriabaseDtypeAriaOrientation.HORIZONTAL,
        metadata={
            "name": "aria-orientation",
            "type": "Attribute",
        },
    )
    aria_owns: List[str] = field(
        default_factory=list,
        metadata={
            "name": "aria-owns",
            "type": "Attribute",
            "tokens": True,
        },
    )
    aria_hidden: bool = field(
        default=False,
        metadata={
            "name": "aria-hidden",
            "type": "Attribute",
        },
    )
    aria_activedescendant: Optional[str] = field(
        default=None,
        metadata={
            "name": "aria-activedescendant",
            "type": "Attribute",
        },
    )
    aria_atomic: bool = field(
        default=False,
        metadata={
            "name": "aria-atomic",
            "type": "Attribute",
        },
    )
    aria_autocomplete: AriabaseDtypeAriaAutocomplete = field(
        default=AriabaseDtypeAriaAutocomplete.NONE,
        metadata={
            "name": "aria-autocomplete",
            "type": "Attribute",
        },
    )
    aria_busy: bool = field(
        default=False,
        metadata={
            "name": "aria-busy",
            "type": "Attribute",
        },
    )
    aria_checked: AriabaseDtypeAriaChecked = field(
        default=AriabaseDtypeAriaChecked.UNDEFINED,
        metadata={
            "name": "aria-checked",
            "type": "Attribute",
        },
    )
    aria_disabled: bool = field(
        default=False,
        metadata={
            "name": "aria-disabled",
            "type": "Attribute",
        },
    )
    aria_expanded: AriabaseDtypeAriaExpanded = field(
        default=AriabaseDtypeAriaExpanded.UNDEFINED,
        metadata={
            "name": "aria-expanded",
            "type": "Attribute",
        },
    )
    aria_haspopup: bool = field(
        default=False,
        metadata={
            "name": "aria-haspopup",
            "type": "Attribute",
        },
    )
    aria_invalid: AriabaseDtypeAriaInvalid = field(
        default=AriabaseDtypeAriaInvalid.FALSE,
        metadata={
            "name": "aria-invalid",
            "type": "Attribute",
        },
    )
    aria_multiline: bool = field(
        default=False,
        metadata={
            "name": "aria-multiline",
            "type": "Attribute",
        },
    )
    aria_multiselectable: bool = field(
        default=False,
        metadata={
            "name": "aria-multiselectable",
            "type": "Attribute",
        },
    )
    aria_posinset: Optional[int] = field(
        default=None,
        metadata={
            "name": "aria-posinset",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    aria_pressed: AriabaseDtypeAriaPressed = field(
        default=AriabaseDtypeAriaPressed.UNDEFINED,
        metadata={
            "name": "aria-pressed",
            "type": "Attribute",
        },
    )
    aria_readonly: bool = field(
        default=False,
        metadata={
            "name": "aria-readonly",
            "type": "Attribute",
        },
    )
    aria_relevant: List[AriarelevantListDtype] = field(
        default_factory=lambda: [
            AriarelevantListDtype.ADDITIONS_TEXT,
        ],
        metadata={
            "name": "aria-relevant",
            "type": "Attribute",
            "tokens": True,
        },
    )
    aria_required: bool = field(
        default=False,
        metadata={
            "name": "aria-required",
            "type": "Attribute",
        },
    )
    aria_selected: AriabaseDtypeAriaSelected = field(
        default=AriabaseDtypeAriaSelected.UNDEFINED,
        metadata={
            "name": "aria-selected",
            "type": "Attribute",
        },
    )
    aria_setsize: Optional[int] = field(
        default=None,
        metadata={
            "name": "aria-setsize",
            "type": "Attribute",
        },
    )
    aria_sort: AriabaseDtypeAriaSort = field(
        default=AriabaseDtypeAriaSort.NONE,
        metadata={
            "name": "aria-sort",
            "type": "Attribute",
        },
    )
    aria_valuemax: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "aria-valuemax",
            "type": "Attribute",
        },
    )
    aria_valuemin: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "aria-valuemin",
            "type": "Attribute",
        },
    )
    aria_valuenow: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "aria-valuenow",
            "type": "Attribute",
        },
    )
    aria_valuetext: Optional[str] = field(
        default=None,
        metadata={
            "name": "aria-valuetext",
            "type": "Attribute",
        },
    )
    aria_modal: bool = field(
        default=False,
        metadata={
            "name": "aria-modal",
            "type": "Attribute",
        },
    )
    aria_current: AriabaseDtypeAriaCurrent = field(
        default=AriabaseDtypeAriaCurrent.FALSE,
        metadata={
            "name": "aria-current",
            "type": "Attribute",
        },
    )
    aria_placeholder: Optional[str] = field(
        default=None,
        metadata={
            "name": "aria-placeholder",
            "type": "Attribute",
        },
    )
    aria_colcount: Optional[int] = field(
        default=None,
        metadata={
            "name": "aria-colcount",
            "type": "Attribute",
        },
    )
    aria_rowcount: Optional[int] = field(
        default=None,
        metadata={
            "name": "aria-rowcount",
            "type": "Attribute",
        },
    )
    aria_colindex: Optional[int] = field(
        default=None,
        metadata={
            "name": "aria-colindex",
            "type": "Attribute",
        },
    )
    aria_rowindex: Optional[int] = field(
        default=None,
        metadata={
            "name": "aria-rowindex",
            "type": "Attribute",
        },
    )
    aria_colspan: Optional[int] = field(
        default=None,
        metadata={
            "name": "aria-colspan",
            "type": "Attribute",
        },
    )
    aria_rowspan: Optional[int] = field(
        default=None,
        metadata={
            "name": "aria-rowspan",
            "type": "Attribute",
        },
    )
    aria_keyshortcuts: Optional[str] = field(
        default=None,
        metadata={
            "name": "aria-keyshortcuts",
            "type": "Attribute",
        },
    )
    aria_roledescription: Optional[str] = field(
        default=None,
        metadata={
            "name": "aria-roledescription",
            "type": "Attribute",
        },
    )
    aria_errormessage: Optional[str] = field(
        default=None,
        metadata={
            "name": "aria-errormessage",
            "type": "Attribute",
        },
    )
    aria_details: Optional[str] = field(
        default=None,
        metadata={
            "name": "aria-details",
            "type": "Attribute",
        },
    )
