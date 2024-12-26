from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class TrackDtypeKind(Enum):
    """
    This is the permitted set of values for the 'kind' attribute on the HTML5
    'track' tag.
    """

    SUBTITLES = "subtitles"
    CAPTIONS = "captions"
    DESCRIPTIONS = "descriptions"
    CHAPTERS = "chapters"
    METADATA = "metadata"
