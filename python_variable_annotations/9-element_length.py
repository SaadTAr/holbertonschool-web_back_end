#!/usr/bin/env python3
"""Module for calculating lengths of iterable elements."""


from typing import Iterable, Sequence, List, Tuple


def element_length(
        lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return each sequence together with its length."""
    return [(element, len(element)) for element in lst]
