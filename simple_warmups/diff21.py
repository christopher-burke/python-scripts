#!/usr/bin/env python3

"""Difference 21.

Given an int n, return the absolute difference between n and 21,
except return double the absolute difference if n is over 21.

source: https://codingbat.com/prob/p197466
"""


def diff21(n: int) -> int:
    """Absolute difference between n and 21.

    Returns abs(n-21) if n <= 21 and abs(n-21) * 2 if n > 21.
    """
    diff = abs(n - 21)
    if n > 21:
        return diff * 2
    return diff


if __name__ == "__main__":
    assert diff21(19) == 2
    assert diff21(10) == 11
    assert diff21(21) == 0
    assert diff21(22) == 2
    assert diff21(25) == 8
    assert diff21(30) == 18
    assert diff21(0) == 21
    assert diff21(1) == 20
    assert diff21(2) == 19
    assert diff21(-1) == 22
    assert diff21(-2) == 23
    assert diff21(50) == 58
    print('Passed')
