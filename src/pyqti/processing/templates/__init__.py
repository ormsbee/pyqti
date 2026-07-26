"""Resolution of QTI built-in response processing template URIs.

``qti-response-processing/@template`` is an opaque URI string --- xsdata provides no
template support whatsoever, and many real items (including
``examples/firstexample.xml``) carry *only* that attribute with no inline rules at
all. Resolving it is therefore not an optimisation, it is the difference between
grading the item and silently doing nothing.

Templates are vendored as XML and parsed with the same strict parser as any other
QTI document, so they compile through the same code path as inline rules. That keeps
the interpreter honest: there is no "template mode" that could diverge from the
real semantics.

**An unresolvable template must raise.** A no-op would leave every outcome at its
declared default, which for the Beginner's Guide item means ``SCORE`` stays at 1 and
every answer is marked correct.
"""

from __future__ import annotations

from importlib.resources import files

from pyqti.errors import UnsupportedTemplateError
from pyqti.loading import load_response_processing
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0 import QtiResponseProcessing

#: URI prefixes 1EdTech has published templates under. The QTI 2.x forms are
#: included because real-world content still uses them.
KNOWN_PREFIXES: tuple[str, ...] = (
    "https://purl.imsglobal.org/spec/qti/v3p0/rptemplates/",
    "http://purl.imsglobal.org/spec/qti/v3p0/rptemplates/",
    "https://www.imsglobal.org/question/qti_v2p2/rptemplates/",
    "http://www.imsglobal.org/question/qti_v2p2/rptemplates/",
    "https://www.imsglobal.org/question/qti_v2p1/rptemplates/",
    "http://www.imsglobal.org/question/qti_v2p1/rptemplates/",
    "http://www.imsglobal.org/question/qti_v2p0/rptemplates/",
)

#: Templates with a vendored XML file in this package.
VENDORED: frozenset[str] = frozenset({"match_correct", "map_response"})


def template_name_for_uri(uri: str) -> str:
    """Extract the template name from a built-in template URI.

    Raises :class:`~pyqti.errors.UnsupportedTemplateError` for an unrecognised host
    or an unknown template name.
    """
    for prefix in KNOWN_PREFIXES:
        if uri.startswith(prefix):
            name = uri[len(prefix) :].strip("/").removesuffix(".xml")
            break
    else:
        raise UnsupportedTemplateError(
            f"{uri!r} is not a recognised QTI response processing template URI"
        )

    if name not in VENDORED:
        raise UnsupportedTemplateError(
            f"no vendored copy of response processing template {name!r} "
            f"(have: {', '.join(sorted(VENDORED))})"
        )
    return name


def load_template(uri: str) -> QtiResponseProcessing:
    """Parse the vendored template for ``uri`` into a model."""
    name = template_name_for_uri(uri)
    xml = files(__package__).joinpath(f"{name}.xml").read_text(encoding="utf-8")
    return load_response_processing(xml)
