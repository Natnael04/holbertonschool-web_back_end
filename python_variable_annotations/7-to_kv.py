#!/usr/bin/env python3
"""a function that takes two data type of argument annotated as float"""


def to_kv(k: str, v: float) -> float:
    """return a tuple"""
    result_k = k
    result_square = v ** 2
    return result_k, result_square
