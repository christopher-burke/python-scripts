#!/usr/bin/env python3

"""Multiples of 3 and 5.

If we list all the natural numbers below 10 that are multiples of
 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. (n < 1000)

problem source: https://projecteuler.net/problem=1
"""


def main():
    """Return the sum of all the multiples of 3 or 5 below 1000."""
    return sum([i for i in range(2, 1000)
                if i % 3 == 0 or i % 5 == 0])


if __name__ == "__main__":
    print(main())
