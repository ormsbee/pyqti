from enum import Enum

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


class CardDtypeValue(Enum):
    ADDITIONAL_DIRECTIONS = "additional-directions"
    AUDIO_DESCRIPTION = "audio-description"
    BRAILLE = "braille"
    GLOSSARY_ON_SCREEN = "glossary-on-screen"
    HIGH_CONTRAST = "high-contrast"
    KEYBOARD_DIRECTIONS = "keyboard-directions"
    KEYWORD_TRANSLATION = "keyword-translation"
    LINGUISTIC_GUIDANCE = "linguistic-guidance"
    LONG_DESCRIPTION = "long-description"
    SIGN_LANGUAGE = "sign-language"
    SIMPLIFIED_LANGUAGE_PORTIONS = "simplified-language-portions"
    SIMPLIFIED_GRAPHICS = "simplified-graphics"
    SPOKEN = "spoken"
    TACTILE = "tactile"
    TRANSCRIPT = "transcript"
