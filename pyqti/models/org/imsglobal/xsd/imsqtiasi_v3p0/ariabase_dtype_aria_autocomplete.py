from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class AriabaseDtypeAriaAutocomplete(Enum):
    """
    The permitted set of values for the aria-autocomplete ARIA annotations.
    """

    INLINE = "inline"
    LIST = "list"
    BOTH = "both"
    NONE = "none"
