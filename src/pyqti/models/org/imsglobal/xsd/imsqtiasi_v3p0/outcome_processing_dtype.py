from __future__ import annotations

from dataclasses import dataclass, field

from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.empty_primitive_type_dtype import (
    EmptyPrimitiveTypeDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.lookup_outcome_value_dtype import (
    LookupOutcomeValueDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.outcome_condition_dtype import (
    OutcomeConditionDtype,
    OutcomeProcessingFragmentDtype,
)
from pyqti.models.org.imsglobal.xsd.imsqtiasi_v3p0.set_value_dtype import (
    SetValueDtype,
)
from pyqti.models.org.w3.pkg_2001.xinclude.include_type import Include

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass(kw_only=True)
class OutcomeProcessingDtype:
    """
    Outcome processing takes place each time the candidate submits the
    responses for an item (when in individual submission mode) or a group
    of items (when in simultaneous submission mode).

    It happens after any (item level) response processing triggered by the
    submission. The values of the test's outcome variables are always reset
    to their defaults prior to ca- rrying out the instructions described by
    the outcomeRules. Because outcome processing hap- pens each time the
    candidate submits responses the resulting values of the test-level out-
    comes may be used to activate test-level feedback during the test or to
    control the behav- iour of subsequent parts through the use of
    preConditions and branchRules. The structure of outcome processing is
    similar to that or responseProcessing.
    """

    class Meta:
        name = "OutcomeProcessingDType"

    choice: list[
        LookupOutcomeValueDtype
        | OutcomeProcessingFragmentDtype
        | SetValueDtype
        | Include
        | EmptyPrimitiveTypeDtype
        | OutcomeConditionDtype
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "qti-lookup-outcome-value",
                    "type": LookupOutcomeValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-processing-fragment",
                    "type": OutcomeProcessingFragmentDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-set-outcome-value",
                    "type": SetValueDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "include",
                    "type": Include,
                    "namespace": "http://www.w3.org/2001/XInclude",
                },
                {
                    "name": "qti-exit-test",
                    "type": EmptyPrimitiveTypeDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
                {
                    "name": "qti-outcome-condition",
                    "type": OutcomeConditionDtype,
                    "namespace": "http://www.imsglobal.org/xsd/imsqtiasi_v3p0",
                },
            ),
        },
    )
