from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)
from pyqti.models.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class PrintedVariableDtype(EmptyPrimitiveTypeDtype):
    """
    The outcome variable or template variable must have been defined.

    The values of response variables cannot be printed directly as their
    values are implicitly known to the candidate through the interactions
    they are bound to; if necessary, their values can be assigned to
    outcomes during response processing and displayed to the candidate as
    part of a body elem- ent visible only in the appropriate feedback
    states. If the variable's value is NULL then the element is ignored.
    Variables of base-type string are treated as simple runs of text.-
    Variables of base-type integer or float are converted to runs of text
    (strings) using the formatting rules described below. Float values
    should only be formatted in the e, E, f, g, G, r or R styles. Variables
    of base-type duration are treated as floats, representing the duration
    in seconds. Variables of base-type file are rendered using a control
    that enables the user to open the file. The control should display the
    name associated with the file, if any. Variables of base-type uri are
    rendered using a control that enables the user to open the identified
    resource, for example, by following a hypertext link in the case of a
    URL. For variables of single cardinality, the value of the variable is
    printed. For varia- bles of ordered cardinality, if the attribute index
    is set, the single value corresponding to the indexed member is
    printed, otherwise an ordered list of the values within the cont- ainer
    is printed, delimited by the string value of the delimiter attribute.
    For variables of multiple cardinality, a list of the values within the
    container is printed, delimited by the string value of the delimiter
    attribute. For variables of record cardinality, if t- he attribute
    field is set, the value corresponding to the specified field is
    printed, oth- erwise a list of the field names and corresponding field
    values within the variable is pr- inted, delimited by the string value
    of the delimiter attribute and with the corresponden- ce between them
    indicated by the string value of the mappingIndicator attribute.
    """

    class Meta:
        name = "PrintedVariableDType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    label: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    w3_org_xml_1998_namespace_base: None | str = field(
        default=None,
        metadata={
            "name": "base",
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    identifier: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    format: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: object = field(
        default="10",
        metadata={
            "type": "Attribute",
        },
    )
    index: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    power_form: bool = field(
        default=False,
        metadata={
            "name": "power-form",
            "type": "Attribute",
        },
    )
    field_value: None | str = field(
        default=None,
        metadata={
            "name": "field",
            "type": "Attribute",
        },
    )
    delimiter: str = field(
        default=";",
        metadata={
            "type": "Attribute",
        },
    )
    mapping_indicator: str = field(
        default="=",
        metadata={
            "name": "mapping-indicator",
            "type": "Attribute",
        },
    )
