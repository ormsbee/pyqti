from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.outcome_declaration_dtype import (
    OutcomeDeclarationDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class QtiOutcomeDeclaration(OutcomeDeclarationDtype):
    class Meta:
        name = "qti-outcome-declaration"
        namespace = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"
