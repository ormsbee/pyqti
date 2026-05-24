from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class TimeLimitsDtype(EmptyPrimitiveTypeDtype):
    """
    In the context of a specific qti-assessment-test an item, or group of
    items, may be subje- ct to a time constraint.

    This specification supports both minimum and maximum time constr-
    aints. The controlled time for a single item is simply the duration of
    the item session as defined by the builtin response variable duration.
    For qti-assessment-sections, qti-test-- parts and whole
    qti-assessment-tests the time limits relate to the durations of all the
    i- tem sessions plus any other time spent navigating that part of the
    test. In other words, the time includes time spent in states where no
    item is being interacted with, such as de- dicated navigation screens.
    The allow-late-submission attribute regulates whether a candi- date's
    response that is beyond the max-time should still be accepted. Minimum
    times are a- pplicable to qti-assessment-sections and
    qti-assessment-items only when linear navigation mode is in effect.
    """

    class Meta:
        name = "TimeLimitsDType"

    min_time: None | float = field(
        default=None,
        metadata={
            "name": "min-time",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    max_time: None | float = field(
        default=None,
        metadata={
            "name": "max-time",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    allow_late_submission: bool = field(
        default=False,
        metadata={
            "name": "allow-late-submission",
            "type": "Attribute",
        },
    )
