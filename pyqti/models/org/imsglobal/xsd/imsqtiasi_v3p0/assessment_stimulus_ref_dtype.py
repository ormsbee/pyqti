from dataclasses import dataclass, field
from typing import Dict, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class AssessmentStimulusRefDtype(EmptyPrimitiveTypeDtype):
    """This is the structure that enables reference to a 'qti-assessment-stimulus'
    instance.

    The stimulus must be contained within its own instance and so the
    Item uses the 'qti-assessme- nt-stimulus-ref' structure to provide
    the link between the Item and the Stimulus.
    """

    class Meta:
        name = "AssessmentStimulusRefDType"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
