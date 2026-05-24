from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_dtype import (
    BaseSequenceDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.col import Col

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class ColGroupDtype(BaseSequenceDtype):
    """
    Provides the functionality of the HTML 'colgroup' tag.

    The colgroup element represents a group of one or more columns in the
    table that is its parent, if it has a parent and that is a table
    element. If the colgroup element contains no col elements, then the
    element may have a span content attribute specified, whose value must
    be a valid non-negative integer greater than zero. The colgroup element
    and its span attribute take part in the table mod- el.
    """

    class Meta:
        name = "ColGroupDType"

    col: list[Col] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
        },
    )
    span: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
