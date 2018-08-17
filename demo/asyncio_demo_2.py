#!/usr/bin/env python3


"""Asyncio demo finding next prime numbers for a list."""


import asyncio
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


async def find_next_prime(n):
    while True:
        n = n + 1
        if prime(n):
            return n
        else:
            await asyncio.sleep(0.000000000001)


async def main():
    next_prime_1 = loop.create_task(find_next_prime(2123123123112))
    next_prime_2 = loop.create_task(find_next_prime(222))
    next_prime_3 = loop.create_task(find_next_prime(45022222222))
    next_prime_4 = loop.create_task(find_next_prime(1000))
    await asyncio.wait([next_prime_1, next_prime_2, next_prime_3, next_prime_4, ])
    return next_prime_1, next_prime_2, next_prime_3, next_prime_4


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(1)
    p1, p2, p3, p4 = loop.run_until_complete(main())
    print(p1.result())
    print(p2.result())
    print(p3.result())
    print(p4.result())
    loop.close()
