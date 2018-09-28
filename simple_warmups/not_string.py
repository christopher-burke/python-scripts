#!/usr/bin/env python3

"""Not String.

Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.


not_string('candy') -> 'not candy'
not_string('x') -> 'not x'
not_string('not bad') -> 'not bad'

source: https://codingbat.com/prob/p189441
"""


def not_string(str_: str) -> str:
    """Add `not` to string.

    Returns a new string with `not` in front or
    an unchanged string if `not` was already there.
    """
    if str_[:3] == 'not':
        return str_
    return f'not {str_}'


if __name__ == "__main__":

    assert not_string('candy') == 'not candy'
    assert not_string('x') == 'not x'
    assert not_string('not bad') == 'not bad', not_string('not bad')
    assert not_string('bad') == 'not bad'
    assert not_string('not') == 'not'
    assert not_string('is not') == 'not is not'
    assert not_string('no') == 'not no'
    print('Passed')
