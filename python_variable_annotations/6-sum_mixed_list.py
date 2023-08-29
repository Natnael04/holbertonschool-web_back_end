#!/usr/bin/env python3
"""to write a type-annotated function whick takes to type"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return their sum as a float"""
    total = 0.0
    for num in mxd_lst:
        total += num
    return total
