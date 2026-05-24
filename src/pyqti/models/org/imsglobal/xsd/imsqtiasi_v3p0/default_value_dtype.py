from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.value_dtype import (
    ValueDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class DefaultValueDtype:
    """
    Defines the default value of the associated response, outcome and
    template variable.
    """

    class Meta:
        name = "DefaultValueDType"

    qti_value: list[ValueDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-value",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    interpretation: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
