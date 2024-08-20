#!/usr/bin/env python3
""" Module for function to return task """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """ Function to return task """
    return asyncio.create_task(wait_random(max_delay))
