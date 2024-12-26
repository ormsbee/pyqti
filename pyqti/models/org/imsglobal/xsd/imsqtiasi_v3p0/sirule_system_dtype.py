from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.silinear_value_dtype import (
    SilinearValueDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class SiruleSystemDtype:
    """The container for the information about the rule that is permitted/required
    for use in the assessment.

    The rule is defined in terms of SI units.
    """

    class Meta:
        name = "SIRuleSystemDType"

    qti_minimum_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "qti-minimum-length",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
    qti_minor_increment: Optional[SilinearValueDtype] = field(
        default=None,
        metadata={
            "name": "qti-minor-increment",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_major_increment: Optional[SilinearValueDtype] = field(
        default=None,
        metadata={
            "name": "qti-major-increment",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
