#!/usr/bin/env python3
'''This file houses a function that is to be annotated'''

from typing import Union, Mapping, Any, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    ''' Function for returning a list of tuples '''
    if key in dct:
        return dct[key]
    else:
        return default
