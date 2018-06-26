#!/usr/bin/env python3


"""Next Prime Number."""

import random
import sys
from math import sqrt
from functools import reduce


def factors(n):
    """Find all factors of a number n.

    https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """
    n_factors = ([i, n//i] for i in range(1, int(sqrt(n) + 1)) if n % i == 0)
    return set(reduce(list.__add__, n_factors))


def prime(n):
    """Return True if x is prime, False otherwise."""
    if n % 2 == 0:
        return False
    if len(factors(n)) == 2:
        return True
    else:
        return False


def next_prime(n):
    """Return the next prime number after n."""
    while True:
        n = n + 1
        if prime(n):
            return n


if __name__ == "__main__":
    try:
        n = sys.argv[1]
    except IndexError:
        n = input('Enter an integer > 1: ')

    try:
        n = int(n)
    except ValueError:
        n = random.randint(2, 2**56)
        print(f'{n} is being used.')

    print(f'The next prime number greater than {n} is {next_prime(n)}.')
