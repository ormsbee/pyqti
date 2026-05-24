from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class AssessmentStimulusRefDtype(EmptyPrimitiveTypeDtype):
    """
    This is the structure that enables reference to a
    'qti-assessment-stimulus' instance.

    The stimulus must be contained within its own instance and so the Item
    uses the 'qti-assessme- nt-stimulus-ref' structure to provide the link
    between the Item and the Stimulus.
    """

    class Meta:
        name = "AssessmentStimulusRefDType"

    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    href: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
