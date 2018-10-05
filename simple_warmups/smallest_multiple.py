#!/usr/bin/env python3

"""2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?

source: https://projecteuler.net/problem=5
"""


from itertools import count


def smallest_divisor(range_=20):
    """Return the samlles positive integer that is evenly divisble.

    Evenly divisible from 1 to the range_.
    """
    divisors = tuple(range(1, range_+1))
    for number in count(2520):
        total = sum([number % x for x in divisors])
        if total == 0:
            return number


if __name__ == "__main__":
    print(smallest_divisor())
