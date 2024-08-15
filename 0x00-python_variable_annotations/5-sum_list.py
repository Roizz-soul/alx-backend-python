#!/usr/bin/env python3
'''This file houses a function that takes a list of floats as
    argument and returns the sum as a float'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' Function for summing up a list of floats '''
    sum = 0
    for i in input_list:
        sum += i
    return sum
