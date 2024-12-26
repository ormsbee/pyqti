from dataclasses import dataclass, field
from typing import Dict, List

__NAMESPACE__ = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


@dataclass
class OrderingDtype:
    """The ordering class specifies the rule used to arrange the child elements of
    a section fol- lowing selection.

    If no ordering rule is given, assume that the elements are to be
    ordered in the order in which they are defined. A sub-section is
    always treated as a single block for selection but the way it is
    treated when shuffling depends on its visibility. A visib- le sub-
    section is always treated as a single block but an invisible sub-
    section is only t- reated as a single block if its keep-together
    characteristic is 'true'. Otherwise, the ch- ild elements of the
    invisible sub-section are mixed into the parent's selection prior to
    shuffling. The ordering class also provides an opportunity for
    extensions to this specifi- cation to include support for more
    complex ordering algorithms. The selection and ordering rules define
    a sequence of items for each instance of the test. The sequence
    starts with the first item of the first section of the first test
    part and continues through to the l- ast item of the last section of
    the last test part. This sequence is constant throughout the test.
    Normally this is the logical sequence perceived by the candidate but
    the use of pre-conditions and/or branch-rules can affect the
    specific path taken. The use of selecti- on with replacement enables
    two or more instances of an item referred to by the same asse-
    ssment-item-ref to appear in the sequence of items for a test. It is
    therefore an error to make such an item the target of a branch-rule.
    Furthermore, when reporting test results t- he sequence number of
    each item must also be reported to avoid ambiguity. See QTI Results
    Reporting [QTI-RR-30]. The ordering class also provides an
    opportunity for extensions to this specification to include support
    for more complex ordering algorithms.
    """

    class Meta:
        name = "OrderingDType"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    shuffle: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
