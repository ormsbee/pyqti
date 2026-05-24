from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class ItemSessionControlDtype(EmptyPrimitiveTypeDtype):
    """
    When items are referenced as part of a test, the test may impose
    constraints on how many attempts, and which states are allowed.

    These constraints can be specified for individual items, for whole
    sections or for an entire qti-test-part. By default, a setting at
    qti-te- st-part level affects all items in that part unless the setting
    is overridden at the qti-- assessment-section level or ultimately at
    the individual qti-assessment-item-ref. The def- aults for an
    qti-Item-session-control are used only in the absence of any applicable
    cons- traint.
    """

    class Meta:
        name = "ItemSessionControlDType"

    max_attempts: None | int = field(
        default=None,
        metadata={
            "name": "max-attempts",
            "type": "Attribute",
        },
    )
    show_feedback: bool = field(
        default=False,
        metadata={
            "name": "show-feedback",
            "type": "Attribute",
        },
    )
    allow_review: bool = field(
        default=True,
        metadata={
            "name": "allow-review",
            "type": "Attribute",
        },
    )
    show_solution: bool = field(
        default=False,
        metadata={
            "name": "show-solution",
            "type": "Attribute",
        },
    )
    allow_comment: bool = field(
        default=False,
        metadata={
            "name": "allow-comment",
            "type": "Attribute",
        },
    )
    allow_skipping: bool = field(
        default=True,
        metadata={
            "name": "allow-skipping",
            "type": "Attribute",
        },
    )
    validate_responses: bool = field(
        default=False,
        metadata={
            "name": "validate-responses",
            "type": "Attribute",
        },
    )
