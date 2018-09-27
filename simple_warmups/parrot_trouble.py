#!/usr/bin/env python3


"""Parrot trouble.

We have a loud talking parrot.
The "hour" parameter is the current hour time in the range 0..23.
We are in trouble if the parrot is talking and the hour is
before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False

source: https://codingbat.com/prob/p166884
"""


def parrot_trouble(talking: bool, hour: int) -> bool:
    """Determine if the parrot is causing trouble."""
    if talking and hour not in range(7, 21):
        return True
    return False


if __name__ == "__main__":
    assert parrot_trouble(True, 6) is True
    assert parrot_trouble(True, 7) is False
    assert parrot_trouble(False, 6) is False
    assert parrot_trouble(True, 21) is True
    assert parrot_trouble(False, 21) is False
    assert parrot_trouble(False, 20) is False
    assert parrot_trouble(True, 23) is True
    assert parrot_trouble(False, 23) is False
    assert parrot_trouble(True, 20) is False
    assert parrot_trouble(False, 12) is False
    print('Passed')
