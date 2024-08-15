#!/usr/bin/env python3
'''This file houses a function that takes a float
    as argument and returns a function that takes a float
    and multiplies it with the previous float'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Function for returning a fuction that multiplies a float '''
    return lambda value: value * multiplier
