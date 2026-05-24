from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.w3.org/2001/10/synthesis"


@dataclass(kw_only=True)
class Aws:
    """
    The 'allowed-within-sentence' group uses this abstract element.
    """

    class Meta:
        name = "aws"
        namespace = "http://www.w3.org/2001/10/synthesis"
