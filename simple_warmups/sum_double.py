#!/usr/bin/env python3

"""sum_double

Given two int values, return their sum.
Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8

source: https://codingbat.com/prob/p141905
"""


def sum_double(a: int, b: int) -> int:
    """Sum Double.

    Return the sum or if a == b return double the sum.
    """
    multiply = 1
    if a == b:
        multiply += 1
    return (a + b) * multiply


if __name__ == "__main__":
    print(sum_double(1, 2))
    print(sum_double(3, 2))
    print(sum_double(2, 2))
