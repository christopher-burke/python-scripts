#!/usr/bin/env python3


"""Given a string, we'll say that the front is the
first 3 chars of the string. If the string length
is less than 3, the front is whatever is there.
Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'

source: https://codingbat.com/prob/p147920
"""


def front3(str_: str) -> str:
    """Three copies of the front."""
    return str_[0:3] * 3


if __name__ == "__main__":
    assert front3('Java') == 'JavJavJav'
    assert front3('Chocolate') == 'ChoChoCho'
    assert front3('abc') == 'abcabcabc'
    assert front3('abcXYZ') == 'abcabcabc'
    assert front3('ab') == 'ababab'
    assert front3('a') == 'aaa'
    assert front3('') == ''
    print('Passed.')
