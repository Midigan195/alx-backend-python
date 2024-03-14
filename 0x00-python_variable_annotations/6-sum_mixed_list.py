#!/usr/bin/env python3
"""
This module defines a functions to sum all numeric values
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function sums all the float and integer values
    and returns the sum as a float.
    """
    return sum(mxd_lst)
