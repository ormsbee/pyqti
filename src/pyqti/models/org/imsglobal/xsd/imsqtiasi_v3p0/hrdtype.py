from __future__ import annotations

from dataclasses import dataclass

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.base_sequence_xbase_empty_dtype import (
    BaseSequenceXbaseEmptyDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class Hrdtype(BaseSequenceXbaseEmptyDtype):
    """
    This provides the functionality of the HTML 'hr' tag.

    The 'hr' tag represents a paragraph- -level thematic break, e.g. a
    scene change in a story, or a transition to another topic w- ithin a
    section of a reference book. This tag has no children.
    """

    class Meta:
        name = "HRDType"
