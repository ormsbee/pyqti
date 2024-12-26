from dataclasses import dataclass, field
from typing import List, Union

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.adtype import (
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    Address,
    Article,
    Aside,
    Blockquote,
    Div,
    Dl,
    Figure,
    Footer,
    Header,
    Nav,
    Ol,
    P,
    Pre,
    Section,
    Table,
    Ul,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.audio import Audio
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.hr import Hr
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.video import Video
from pyqti.models.org.w3.pkg_1998.math.math_ml.math import Math

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class StimulusBodyDtype:
    """This is the container for the content that is to be defined as the common
    stimulus in an Item cf.

    ItemBody. The stimulus body contains the text, graphics, media
    objects and inter- actions that describe the common content and
    information about how it is structured. The body is presented by
    combining it with stylesheet information, either explicitly or
    impli- citly using the default style rules of the delivery or
    authoring system.
    """

    class Meta:
        name = "StimulusBodyDType"

    choice: List[
        Union[
            Math,
            Pre,
            H1,
            H2,
            H3,
            H4,
            H5,
            H6,
            P,
            Address,
            Dl,
            Ol,
            Ul,
            Hr,
            Blockquote,
            Table,
            Div,
            Article,
            Aside,
            Audio,
            Figure,
            Footer,
            Header,
            Nav,
            Section,
            Video,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ol",
                    "type": Ol,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "table",
                    "type": Table,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "div",
                    "type": Div,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "article",
                    "type": Article,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "aside",
                    "type": Aside,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "audio",
                    "type": Audio,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "figure",
                    "type": Figure,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "footer",
                    "type": Footer,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "header",
                    "type": Header,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "nav",
                    "type": Nav,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "section",
                    "type": Section,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "video",
                    "type": Video,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
