from dataclasses import dataclass, field
from typing import ForwardRef, List, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.set_value_dtype import (
    SetValueDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_condition_dtype import (
    TemplateConditionDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.template_constraint_dtype import (
    TemplateConstraintDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class TemplateProcessingDtype:
    """Template processing consists of one or more templateRules that are followed
    by the cloning engine or delivery system in order to assign values to the
    template variables.

    Template p- rocessing is identical in form to responseProcessing
    except that the purpose is to assign values to template variables,
    not outcome variables.
    """

    class Meta:
        name = "TemplateProcessingDType"

    choice: List[
        Union[
            "TemplateProcessingDtype.QtiSetTemplateValue",
            EmptyPrimitiveTypeDtype,
            TemplateConditionDtype,
            "TemplateProcessingDtype.QtiSetDefaultValue",
            "TemplateProcessingDtype.QtiSetCorrectResponse",
            TemplateConstraintDtype,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-set-template-value",
                    "type": ForwardRef(
                        "TemplateProcessingDtype.QtiSetTemplateValue"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-exit-template",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-condition",
                    "type": TemplateConditionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-default-value",
                    "type": ForwardRef(
                        "TemplateProcessingDtype.QtiSetDefaultValue"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-correct-response",
                    "type": ForwardRef(
                        "TemplateProcessingDtype.QtiSetCorrectResponse"
                    ),
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-template-constraint",
                    "type": TemplateConstraintDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )

    @dataclass
    class QtiSetTemplateValue(SetValueDtype):
        pass

    @dataclass
    class QtiSetDefaultValue(SetValueDtype):
        pass

    @dataclass
    class QtiSetCorrectResponse(SetValueDtype):
        pass
