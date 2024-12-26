from dataclasses import dataclass, field
from typing import List, Optional, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.lookup_outcome_value_dtype import (
    LookupOutcomeValueDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.response_condition_dtype import (
    ResponseConditionDtype,
    ResponseProcessingFragmentDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.set_value_dtype import (
    SetValueDtype,
)
from pyqti.models.org.w3.pkg_2001.xinclude.include_type import Include

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class ResponseProcessingDtype:
    """Response processing is the process by which the Delivery Engine assigns
    outcomes based on the candidate's responses.

    The outcomes may be used to provide feedback to the candidate.
    Feedback is either provided immediately following the end of the
    candidate's attempt or it is provided at some later time, perhaps as
    part of a summary report on the item session. The end of an attempt,
    and therefore response processing, must only take place in direct
    response to a user action or in response to some expected event,
    such as the end of a tes- t. An item session that enters the
    suspended state may have values for the response varia- bles that
    have yet to be submitted for response processing.
    """

    class Meta:
        name = "ResponseProcessingDType"

    choice: List[
        Union[
            Include,
            ResponseConditionDtype,
            ResponseProcessingFragmentDtype,
            SetValueDtype,
            EmptyPrimitiveTypeDtype,
            LookupOutcomeValueDtype,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-response-condition",
                    "type": ResponseConditionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-response-processing-fragment",
                    "type": ResponseProcessingFragmentDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-outcome-value",
                    "type": SetValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-exit-response",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-lookup-outcome-value",
                    "type": LookupOutcomeValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
    template: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    template_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "template-location",
            "type": "Attribute",
        },
    )
