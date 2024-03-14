#!/usr/bin/env python3
"""
This module defines a function for returning a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function accpets a string and numeric value
    and returns a tuple of these values
    """
    return k, float(v ** 2)
