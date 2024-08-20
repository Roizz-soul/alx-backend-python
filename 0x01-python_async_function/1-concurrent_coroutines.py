#!/usr/bin/env python3
""" Module for running multiple coroutines """

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of floats """
    res: List[float] = []

    for task in asyncio.as_completed(
      [wait_random(max_delay) for _ in range(n)]):
        ress: float = await task
        res.append(ress)

    return res
