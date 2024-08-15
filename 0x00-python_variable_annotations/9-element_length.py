#!/usr/bin/env python3
'''This file houses a function that is to be annotated'''

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Function for returning a list of tuples '''
    return [(i, len(i)) for i in lst]
