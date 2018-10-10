#!/usr/bin/env python3

"""10001th prime.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?

source: https://projecteuler.net/problem=7
"""

from itertools import count
from math import sqrt
from functools import reduce


def prime(n):
    """
    Return True if x is prime, False otherwise.

    :param n: integer n
    :return: True or False
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if len(factors(n)) == 2:
        return True
    else:
        return False


def factors(n):
    """
    Find the set of factors for n.

    :param n: integer n
    :return: set of factors.
    """
    n_factors = ([i, n//i]
                 for i in range(1, int(sqrt(n) + 1)) if n % i == 0)
    return set(reduce(list.__add__, n_factors))


def main():
    """
    Find the 10001th prime main method.

    :param n: integer n
    :return: 10001th prime
    """
    primes = {2, }
    for x in count(3, 2):
        if prime(x):
            primes.add(x)
        if len(primes) >= 10001:
            break
    return sorted(primes)[-1]


if __name__ == "__main__":
    print(main())
