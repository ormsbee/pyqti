from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.uslinear_value_dtype import (
    UslinearValueDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class UsruleSystemDtype:
    """The container for the information about the rule that is permitted/required
    for use in the assessment.

    The rule is defined in terms of US units.
    """

    class Meta:
        name = "USRuleSystemDType"

    qti_minimum_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "qti-minimum-length",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
    qti_minor_increment: Optional[UslinearValueDtype] = field(
        default=None,
        metadata={
            "name": "qti-minor-increment",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_major_increment: Optional[UslinearValueDtype] = field(
        default=None,
        metadata={
            "name": "qti-major-increment",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
