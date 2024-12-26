from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.calculator_dtype_qti_calculator_type import (
    CalculatorDtypeQtiCalculatorType,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.item_file_info_dtype import (
    ItemFileInfoDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class CalculatorDtype:
    """
    This is the container for the information about the calculator that is
    required/permitted for use by the learner undertaking the assessment.
    """

    class Meta:
        name = "CalculatorDType"

    qti_calculator_type: Optional[CalculatorDtypeQtiCalculatorType] = field(
        default=None,
        metadata={
            "name": "qti-calculator-type",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
    qti_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "qti-description",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "required": True,
        },
    )
    qti_calculator_info: Optional[ItemFileInfoDtype] = field(
        default=None,
        metadata={
            "name": "qti-calculator-info",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
