#!/usr/bin/env python3
""" Module to create an async generator """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Generator function to generate a list"""
    for i in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
