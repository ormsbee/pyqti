from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class ContextDeclarationDtypeCardinality(Enum):
    """
    Contains the permitted set of cardinality values.

    The cardinality is used in the context of the associated variable.
    """

    MULTIPLE = "multiple"
    ORDERED = "ordered"
    RECORD = "record"
    SINGLE = "single"
