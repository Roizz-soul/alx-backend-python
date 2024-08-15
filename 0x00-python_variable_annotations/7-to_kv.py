#!/usr/bin/env python3
'''This file houses a function that takes a string and int
    or float as argument and returns a tuple'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Function for returning a tuple containg a stringa snd float '''
    return (k, v ** 2)
