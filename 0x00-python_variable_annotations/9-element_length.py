#!/usr/bin/env python3
"""
This module conatains a function that acepts an iterable
and returns a list of tuples
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Take an iterable of sequences as input and return a
    list of tuples where each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
