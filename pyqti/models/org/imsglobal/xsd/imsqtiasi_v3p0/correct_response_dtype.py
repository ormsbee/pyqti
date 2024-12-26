from dataclasses import dataclass, field
from typing import List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.value_dtype import (
    ValueDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class CorrectResponseDtype:
    """
    This class is used to define, as part of the response declaration, the
    values(s) for the correct response.
    """

    class Meta:
        name = "CorrectResponseDType"

    qti_value: List[ValueDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-value",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    interpretation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
