#!/usr/bin/env python3
"""annotate the function parameter"""
from typing import Iterable, Tuple


def element_length(lst):
    """return the value."""
    return [(i, len(i)) for i in lst]


element_length.__annotations__ = {
    'lst': Iterable[str],
    'return': Iterable[Tuple[str, int]]
}
