#!/usr/bin/env python3


"""Near Hundred.

Given an int n, return True if it is within 10
 of 100 or 200.
 Note: abs(num) computes the absolute value of a number.


near_hundred(93) -> True
near_hundred(90) -> True
near_hundred(89) -> False


source: https://codingbat.com/prob/p124676
"""


def near_hundred(n: int) -> bool:
    """Integer n is near 100 or 200 by 10."""
    near100 = abs(100 - n) <= 10
    near200 = abs(200 - n) <= 10
    return any((near100, near200,))


if __name__ == "__main__":
    assert near_hundred(93) is True
    assert near_hundred(90) is True
    assert near_hundred(89) is False
    assert near_hundred(110) is True
    assert near_hundred(111) is False
    assert near_hundred(121) is False
    assert near_hundred(-101) is False
    assert near_hundred(-209) is False
    assert near_hundred(190) is True
    assert near_hundred(209) is True
    assert near_hundred(0) is False
    assert near_hundred(5) is False
    assert near_hundred(-50) is False
    assert near_hundred(191) is True
    assert near_hundred(189) is False
    assert near_hundred(200) is True
    assert near_hundred(210) is True
    assert near_hundred(211) is False
    assert near_hundred(290) is False
    print('Passed')
