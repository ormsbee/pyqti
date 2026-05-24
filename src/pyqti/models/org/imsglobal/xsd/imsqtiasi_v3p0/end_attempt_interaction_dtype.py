from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype import (
    BaseSequenceXbaseEmptyDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class EndAttemptInteractionDtype(BaseSequenceXbaseEmptyDtype):
    """
    The end attempt interaction is a special type of interaction which
    allows item authors to provide the candidate with control over the way
    in which the candidate terminates an atte- mpt.

    The candidate can use the interaction to terminate the attempt
    (triggering response processing) immediately, typically to request a
    hint. It must be bound to a response vari- able with base-type boolean
    and single cardinality. If the candidate invokes response pro- cessing
    using an endAttemptInteraction then the associated response variable is
    set to 't- rue'. If response processing is invoked in any other way,
    either through a different endA- ttemptInteraction or through the
    default method for the delivery engine, then the associa- ted response
    variable is set to 'false'. The default value of the response variable
    is al- ways ignored.
    """

    class Meta:
        name = "EndAttemptInteractionDType"

    response_identifier: str = field(
        metadata={
            "name": "response-identifier",
            "type": "Attribute",
        }
    )
    title: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    count_attempt: None | bool = field(
        default=None,
        metadata={
            "name": "count-attempt",
            "type": "Attribute",
        },
    )
