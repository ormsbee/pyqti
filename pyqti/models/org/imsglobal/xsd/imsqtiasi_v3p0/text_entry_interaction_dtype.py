from dataclasses import dataclass, field
from typing import Optional

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype import (
    BaseSequenceXbaseEmptyDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class TextEntryInteractionDtype(BaseSequenceXbaseEmptyDtype):
    """A TextEntry Interaction is an inlineInteraction that obtains a simple piece
    of text from the candidate.

    Like inlineChoiceInteraction, the delivery engine must allow the
    candidate to review their choice within the context of the
    surrounding text. The textEntryInteracti- on must be bound to a
    response variable with single or record cardinality only. If the re-
    sponse variable has single cardinality the base-type must be one of
    string, integer or fl- oat; if it has record cardinality the
    permitted fields are 'stringValue', 'floatValue', e- tc.
    """

    class Meta:
        name = "TextEntryInteractionDType"

    response_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "response-identifier",
            "type": "Attribute",
            "required": True,
        },
    )
    base: int = field(
        default=10,
        metadata={
            "type": "Attribute",
        },
    )
    string_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "string-identifier",
            "type": "Attribute",
        },
    )
    expected_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "expected-length",
            "type": "Attribute",
        },
    )
    pattern_mask: Optional[str] = field(
        default=None,
        metadata={
            "name": "pattern-mask",
            "type": "Attribute",
        },
    )
    placeholder_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "placeholder-text",
            "type": "Attribute",
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    data_patternmask_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "data-patternmask-message",
            "type": "Attribute",
        },
    )
