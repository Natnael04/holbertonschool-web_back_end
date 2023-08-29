#!/usr/bin/env python3
"""take a list of float as argument and return the sum"""


def sum_list(input_list: list[float]) -> float:
    """create the varible and  return sum of the list"""
    total = 0.0
    for num in input_list:
        total += num
    return total
