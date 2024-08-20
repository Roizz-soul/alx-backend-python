#!/usr/bin/env python3
""" Module of function for a task """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of floats """
    res:  List[float] = []

    for task in asyncio.as_completed(
      [task_wait_random(max_delay) for _ in range(n)]):
        ress: float = await task
        res.append(ress)

    return res
