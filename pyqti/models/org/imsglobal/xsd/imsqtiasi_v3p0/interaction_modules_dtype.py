from dataclasses import dataclass, field
from typing import List

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.interaction_module_dtype import (
    InteractionModuleDtype,
)

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class InteractionModulesDtype:
    """The set of interaction configuration settings to be used by the PCI.

    These settings are d- efined with respect to the set of JavaScript
    library modules.
    """

    class Meta:
        name = "InteractionModulesDType"

    qti_interaction_module: List[InteractionModuleDtype] = field(
        default_factory=list,
        metadata={
            "name": "qti-interaction-module",
            "type": "Element",
            "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
            "min_occurs": 1,
        },
    )
    primary_configuration: str = field(
        default="modules/module_resolution.js",
        metadata={
            "name": "primary-configuration",
            "type": "Attribute",
        },
    )
    secondary_configuration: str = field(
        default="modules/fallback_module_resolution.js",
        metadata={
            "name": "secondary-configuration",
            "type": "Attribute",
        },
    )
