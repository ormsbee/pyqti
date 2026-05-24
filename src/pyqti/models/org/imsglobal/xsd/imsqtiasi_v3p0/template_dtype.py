from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class TemplateDtype:
    """
    This is the 'template' tag in HTML.

    This tag acts as an extension point for the HTML-based content.
    """

    class Meta:
        name = "TemplateDType"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
