from dataclasses import dataclass, field
from typing import Optional, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.increment_sidtype import (
    IncrementSidtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.increment_usdtype import (
    IncrementUsdtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ProtractorDtype:
    """
    This is the container for the information about the permitted characteristics
    of the prot- ractor companion material.
    """

    class Meta:
        name = "ProtractorDType"

    qti_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "qti-description",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
    qti_increment_si_or_qti_increment_us: Optional[
        Union[IncrementSidtype, IncrementUsdtype]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-increment-si",
                    "type": IncrementSidtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-increment-us",
                    "type": IncrementUsdtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
