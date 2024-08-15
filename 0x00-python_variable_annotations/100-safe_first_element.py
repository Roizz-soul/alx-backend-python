#!/usr/bin/env python3
'''This file houses a function that is to be annotated'''

from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Function for returning a list of tuples '''
    if lst:
        return lst[0]
    else:
        return None
