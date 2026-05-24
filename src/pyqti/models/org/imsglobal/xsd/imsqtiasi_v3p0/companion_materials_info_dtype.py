from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.calculator_dtype import (
    CalculatorDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.item_file_info_dtype import (
    ItemFileInfoDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.protractor_dtype import (
    ProtractorDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.rule_dtype import RuleDtype

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class CompanionMaterialsInfoDtype:
    """
    This is the container for the information about the companion materials
    that are available to a learner undertaking the assessment.
    """

    class Meta:
        name = "CompanionMaterialsInfoDType"

    qti_calculator: list[CalculatorDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-calculator",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_rule: list[RuleDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-rule",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_protractor: list[ProtractorDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-protractor",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_digital_material: list[ItemFileInfoDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-digital-material",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    qti_physical_material: list[str] = field(
        default_factory=list,
        metadata={
            "name": "qti-physical-material",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
