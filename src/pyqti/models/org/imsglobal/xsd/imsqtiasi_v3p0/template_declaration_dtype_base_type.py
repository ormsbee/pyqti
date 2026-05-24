from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class TemplateDeclarationDtypeBaseType(Enum):
    """
    A base-type is simply a description of a set of atomic values (atomic
    to this specificati- on).

    Note that several of the base-types used to define the runtime data
    model have ident- ical definitions to those of the basic data types
    used to define the values for attributes in the specification itself.
    The use of an enumeration to define the set of base-types us- ed in the
    runtime model, as opposed to the use of classes with similar names, is
    designed to help distinguish between these two distinct levels of
    modelling.
    """

    BOOLEAN = "boolean"
    DIRECTED_PAIR = "directedPair"
    DURATION = "duration"
    FILE = "file"
    FLOAT = "float"
    IDENTIFIER = "identifier"
    INTEGER = "integer"
    PAIR = "pair"
    POINT = "point"
    STRING = "string"
    URI = "uri"
