from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.calculator_dtype_qti_calculator_type import (
    CalculatorDtypeQtiCalculatorType,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.item_file_info_dtype import (
    ItemFileInfoDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class CalculatorDtype:
    """
    This is the container for the information about the calculator that is
    required/permitted for use by the learner undertaking the assessment.
    """

    class Meta:
        name = "CalculatorDType"

    qti_calculator_type: CalculatorDtypeQtiCalculatorType = field(
        metadata={
            "name": "qti-calculator-type",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        }
    )
    qti_description: str = field(
        metadata={
            "name": "qti-description",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        }
    )
    qti_calculator_info: None | ItemFileInfoDtype = field(
        default=None,
        metadata={
            "name": "qti-calculator-info",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
