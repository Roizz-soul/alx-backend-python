#!/usr/bin/env python3
'''This file houses a function that takes a list of floats
    or int as argument and returns the sum as a float'''

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Function for summing up a list of floats and ints '''
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
