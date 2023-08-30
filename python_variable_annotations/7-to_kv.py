#!/usr/bin/env python3
"""function that takes two data type of argument annotated as float."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple"""
    result_k: int = k
    result_square: float = v ** 2
    return result_k, result_square
