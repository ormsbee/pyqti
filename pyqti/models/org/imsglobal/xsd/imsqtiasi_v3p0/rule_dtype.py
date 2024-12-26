from dataclasses import dataclass, field
from typing import Optional, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.sirule_system_dtype import (
    SiruleSystemDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.usrule_system_dtype import (
    UsruleSystemDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class RuleDtype:
    """The container for the information about the rule that is permitted/required
    for use in the assessment.

    The rule is defined in terms of SI or US units.
    """

    class Meta:
        name = "RuleDType"

    qti_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "qti-description",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
    qti_rule_system_si_or_qti_rule_system_us: Optional[
        Union[SiruleSystemDtype, UsruleSystemDtype]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-rule-system-si",
                    "type": SiruleSystemDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-rule-system-us",
                    "type": UsruleSystemDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
