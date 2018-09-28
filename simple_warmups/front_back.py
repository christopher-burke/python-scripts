#!/usr/bin/env python3

"""Front Back.

Given a string, return a new string where the
first and last chars have been exchanged.

front_back('code') == 'eodc'
front_back('a') == 'a'
front_back('ab') == 'ba'
"""


def front_back(str_: str) -> str:
    """Swap the first and last characters of a string."""
    if len(str_) > 1:
        return f'{str_[-1]}{str_[1:-1]}{str_[0]}'
    return str_


if __name__ == "__main__":
    assert front_back('code') == 'eodc'
    assert front_back('a') == 'a'
    assert front_back('ab') == 'ba'
    assert front_back('abc') == 'cba'
    assert front_back('') == ''
    assert front_back('Chocolate') == 'ehocolatC'
    assert front_back('aavJ') == 'Java'
    assert front_back('hello') == 'oellh'
    print('Passed')
