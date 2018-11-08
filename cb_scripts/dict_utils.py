#!/usr/bin/env python3

"""Dictonary Utils.

Dictionary Utilities.
"""

from functools import reduce
from operator import mul, add, sub


def create_power_dict(length=1):
    return {x: x**x for x in range(1, length+1)}


def operate(func, *dicts):
    """Apply func to values of *dicts and return the result."""
    result = [value for d in dicts for value in d.values()]
    result = reduce(func, result, 1)
    return result


def combine(d1, d2):
    """Combine dictionaries into one."""
    return {**d1, **d2}


if __name__ == "__main__":

    d1 = {'a': 1, 'b': 2, 'c': 3, }
    d2 = {'d': 4, 'e': 5, 'f': 6, }

    print(combine(d1, d2))

    print(operate(mul, d1, d2))
    print(operate(add, d1, d2))
    print(operate(sub, d1, d2))

    print(create_power_dict(1))
    print(create_power_dict(3))
    print(create_power_dict(10))
