#!/usr/bin/env python3
"""
This module conatins a function that totals the values of a list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function adds the sum of floats in a list
    and returns a float value
    """
    return sum(input_list)
