#!/usr/bin/env python3


"""Missing Character.

Given a non-empty string and an int n, return a new
string where the char at index n has been removed.
The value of n will be a valid index of a char in
the original string(i.e. n will be in the range
0..len(str)-1 inclusive).


missing_char('kitten', 1) == 'ktten'
missing_char('kitten', 0) == 'itten'
missing_char('kitten', 4) == 'kittn'

source: https://codingbat.com/prob/p149524
"""


def missing_char(str_: str, n: int) -> str:
    """Remove character at index n."""
    return f'{str_[:n]}{str_[n+1:]}'


if __name__ == "__main__":
    assert missing_char('kitten', 1) == 'ktten'
    assert missing_char('kitten', 0) == 'itten'
    assert missing_char('kitten', 4) == 'kittn'
    assert missing_char('Hi', 0) == 'i'
    assert missing_char('Hi', 1) == 'H'
    assert missing_char('code', 0) == 'ode'
    assert missing_char('code', 1) == 'cde'
    assert missing_char('chocolate', 8) == 'chocolat'
    assert missing_char('code', 2) == 'coe'
    assert missing_char('code', 3) == 'cod'
    print('Passed')
