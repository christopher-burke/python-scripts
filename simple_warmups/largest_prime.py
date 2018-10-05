#!/usr/bin/env python3

""" Largest prime factor.

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

source: https://projecteuler.net/problem=3
"""

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
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if len(factors(n)) == 2:
        return True
    else:
        return False


def prime_factorization(number: int):
    """Return set of prime factors."""
    p = number // 2
    s = set()
    for n in range(1, p+1):
        if number % n == 0 and prime(n):
            s = s | {n}
    return s


if __name__ == "__main__":
    print(13195, sorted(prime_factorization(13195)))
    print(600851475143, sorted(prime_factorization(600851475143)))
