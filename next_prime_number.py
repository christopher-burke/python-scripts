#!/usr/bin/env python3


"""Next Prime Number."""

from math import sqrt, ceil
from functools import reduce


def factors(n):
    """Find all factors of a number n.

    https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(sqrt(n) + 1)) if n % i == 0)))


def is_prime(x):
    """Return True if x is prime, False otherwise."""
    if len(factors(x)) == 2:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_prime(337))
