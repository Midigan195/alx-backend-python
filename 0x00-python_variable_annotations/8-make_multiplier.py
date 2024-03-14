#!/usr/bin/env python3
"""
This module defines a function that retuns another function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function returns the reference to another function
    for multiplication
    """
    def multiplier_function(x: float) -> float:
        """
        Function to be called by multiplier
        """
        return x * multiplier
    return multiplier_function
