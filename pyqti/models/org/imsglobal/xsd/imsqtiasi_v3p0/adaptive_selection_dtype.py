from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adaptive_href_dtype import (
    AdaptiveHrefDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class AdaptiveSelectionDtype:
    """This is the container for the set of data that is to be supplied to a
    Computer Adaptive T- esting (CAT) engine.

    This information is required when a CAT engine is to be used to
    dete- rmine which items are to be supplied next. The details for
    this data is defined in the IMS Computer Adaptive Testing 1.0
    specification [CAT, 19] which defines the API to the CAT en- gine.
    When using an extenal CAT engine there are implementation issues
    that MUST be addre- ssed to ensure consistent behavior with other
    QTI features such as Selection, Ordering, B- ranching, etc.
    """

    class Meta:
        name = "AdaptiveSelectionDType"

    qti_adaptive_engine_ref: Optional[AdaptiveHrefDtype] = field(
        default=None,
        metadata={
            "name": "qti-adaptive-engine-ref",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
    qti_adaptive_settings_ref: Optional[AdaptiveHrefDtype] = field(
        default=None,
        metadata={
            "name": "qti-adaptive-settings-ref",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_usagedata_ref: Optional[AdaptiveHrefDtype] = field(
        default=None,
        metadata={
            "name": "qti-usagedata-ref",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_metadata_ref: Optional[AdaptiveHrefDtype] = field(
        default=None,
        metadata={
            "name": "qti-metadata-ref",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
