from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.interpolation_table_entry_dtype import (
    InterpolationTableEntryDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class InterpolationTableDtype:
    """
    An interpolationTable transforms a source float (or integer) by finding
    the first interpo- lationTableEntry with a sourceValue that is less
    than or equal to (subject to includeBoun- dary) the source value.

    For example, an interpolation table can be used to map a raw nume- ric
    score onto an identifier representing a grade. It may also be used to
    implement numer- ic transformations such as those from a simple raw
    score to a value on a calibrated scale.
    """

    class Meta:
        name = "InterpolationTableDType"

    qti_interpolation_table_entry: list[InterpolationTableEntryDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-interpolation-table-entry",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    default_value: None | str = field(
        default=None,
        metadata={
            "name": "default-value",
            "type": "Attribute",
        },
    )
