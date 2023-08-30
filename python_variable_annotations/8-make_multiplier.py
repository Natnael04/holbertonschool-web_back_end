#!/usr/bin/env python3
"""a function that take a float multiplier as argument."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """create a multiplier function."""
    def multiplier_function(x: float) -> float:
        """multiply a given float by the specified multiplier."""
        return x * multiplier
    return multiplier_function


double = make_multiplier(2.0)
triple = make_multiplier(3.0)

result_double = double(5.0)
result_triple = triple(5.0)
