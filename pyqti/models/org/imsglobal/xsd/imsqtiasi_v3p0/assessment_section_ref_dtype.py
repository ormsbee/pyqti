from dataclasses import dataclass, field
from typing import Dict, List, Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class AssessmentSectionRefDtype(EmptyPrimitiveTypeDtype):
    """Sections can be included into qti-test-parts or other qti-assessment-
    sections by aggregat- ion or by reference.

    The qti-assessment-section-ref element enables the inclusion by
    refe- rence. The only documents that can be refered to by qti-
    assessment-section-ref are XML do- cuments that contain a single
    qti-assessment-section as a single root. There are no other
    restrictions on the referenced qti-assessment-section document. The
    qti-assessment-sectio- n-ref element functions as a facade for the
    qti-assessment-section to which it refers. Th- at means that, at
    runtime, the document that contains the reference, with the refered-
    to section merged in, should behave exactly the same as a document
    that has all the same sec- tions aggregated in one document.
    Adaptive test branch rules can only refer to included or directly
    referenced sections, they can not refer to sections that are in
    their turn inclu- ded or referenced within the referenced section.
    That is to say, branching rules should t- reat referred sections as
    leaf nodes, that have no children that are amenable to branching
    separately from their immediate parent.
    """

    class Meta:
        name = "AssessmentSectionRefDType"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
