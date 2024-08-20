#!/usr/bin/env python3
""" Module to write asynchronous code """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random float between 0 and arg"""
    res: float = random.uniform(0, float(max_delay))
    await asyncio.sleep(res)
    return res
