from dataclasses import dataclass, field
from typing import Dict, List

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_full_dtype import (
    BaseSequenceFullDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class CustomInteractionDtype(BaseSequenceFullDtype):
    """The qti-custom-interaction provides an opportunity for extensibility of this
    specification to include support for interactions not currently documented,
    using methods that are prop- rietary for the supplier.

    The use of this interaction is deprecated in favor of qti-porta-
    ble-custom-interaction [PCI, 20].
    """

    class Meta:
        name = "CustomInteractionDType"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
