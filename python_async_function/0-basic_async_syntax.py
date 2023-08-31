#!/usr/bin/env python3
"""Asynchronous coroutine that introduces a random delay and returns the delay duration.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that introduces a random delay and returns the delay duration.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
