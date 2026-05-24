from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype import (
    BaseSequenceXbaseEmptyDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class Brdtype(BaseSequenceXbaseEmptyDtype):
    """
    This provides the functionality of the HTML 'br' tag.

    The 'br' tag represents a line brea- k.This tag has no children.
    """

    class Meta:
        name = "BRDType"
