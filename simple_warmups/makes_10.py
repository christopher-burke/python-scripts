#!/usr/bin/env python3


"""Makes 10.

Given 2 ints, a and b, return True
if one if them is 10 or if their sum is 10.
"""


def makes10(a: int, b: int) -> bool:
    """Determine if the sum or if either a,b  is 10."""
    return (a + b == 10 or a == 10 or b == 10)


if __name__ == "__main__":
    assert makes10(9, 10) is True
    assert makes10(9, 9) is False
    assert makes10(1, 9) is True
    assert makes10(10, 1) is True
    assert makes10(10, 10) is True
    assert makes10(8, 2) is True
    assert makes10(8, 3) is False
    assert makes10(10, 42) is True
    assert makes10(12, -2) is True
    print('Passed')
