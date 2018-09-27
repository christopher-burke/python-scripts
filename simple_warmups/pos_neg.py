#!/usr/bin/env python3


"""Positive Negative.

Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True, then return
True only if both are negative.

source: https://codingbat.com/prob/p162058
"""


def pos_neg(a: int, b: int, negative: bool) -> bool:
    """Differences in signed digits.

    Return True if:
        - negative is True and both a,b < 0.
        - negative is False and
        ((a > 0 and b < 0) or (a < 0 and b > 0).
    Return False otherwise.
    """
    if negative:
        return (a < 0 and b < 0)
    return (a > 0 and b < 0) or (a < 0 and b > 0)


if __name__ == "__main__":
    assert pos_neg(1, -1, False) is True
    assert pos_neg(-1, 1, False) is True
    assert pos_neg(-4, -5, True) is True
    assert pos_neg(-4, -5, False) is False
    assert pos_neg(-4, 5, False) is True
    assert pos_neg(-4, 5, True) is False
    assert pos_neg(1, 1, False) is False
    assert pos_neg(-1, -1, False) is False
    assert pos_neg(1, -1, True) is False
    assert pos_neg(-1, 1, True) is False
    assert pos_neg(1, 1, True) is False
    assert pos_neg(-1, -1, True) is True
    assert pos_neg(5, -5, False) is True
    assert pos_neg(-6, 6, False) is True
    assert pos_neg(-5, -6, False) is False
    assert pos_neg(-2, -1, False) is False
    assert pos_neg(1, 2, False) is False
    assert pos_neg(-5, 6, True) is False
    assert pos_neg(-5, -5, True) is True

    print('Passed')
