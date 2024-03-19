#!/usr/bin/env python3
"""
This module defines a function for asynchronously genrating
random numbers
"""
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This generator function accepts no arguments
    and yields 10 random numbers asynchronously
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
