from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class ExtendedTextInteractionDtypeFormat(Enum):
    """
    The set of permitted values to control the format of the text entered by the
    candidate.
    """

    PLAIN = "plain"
    PREFORMATTED = "preformatted"
    XHTML = "xhtml"
