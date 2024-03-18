#!/usr/bin/env python3
"""
This module defines an async function that waits
for a random amount of time.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function waits for a random amount of time with a maximum
    and returns the result
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
