#!/usr/bin/env python3
"""
This module defines a function for asynchronously genrating
random numbers
"""
from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This generator function accepts no arguments
    and yields 10 random numbers asynchronously
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
