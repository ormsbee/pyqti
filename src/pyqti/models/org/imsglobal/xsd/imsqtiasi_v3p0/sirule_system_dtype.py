from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.silinear_value_dtype import (
    SilinearValueDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class SiruleSystemDtype:
    """
    The container for the information about the rule that is
    permitted/required for use in the assessment.

    The rule is defined in terms of SI units.
    """

    class Meta:
        name = "SIRuleSystemDType"

    qti_minimum_length: int = field(
        metadata={
            "name": "qti-minimum-length",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        }
    )
    qti_minor_increment: None | SilinearValueDtype = field(
        default=None,
        metadata={
            "name": "qti-minor-increment",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_major_increment: SilinearValueDtype = field(
        metadata={
            "name": "qti-major-increment",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        }
    )
