#!/usr/bin/env python3

"""sleep_in

The parameter weekday is True if it is a weekday, and 
the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. 
Return True if we sleep in.


source: https://codingbat.com/prob/p173401
"""


def sleep_in(weekday: bool, vacation: bool) -> bool:
    """Sleep in or not.

    This solution uses the built in any().
    """
    if not any((weekday, vacation,)):
        return True
    return vacation


if __name__ == "__main__":
    print(sleep_in(False, False))
    print(sleep_in(True, False))
    print(sleep_in(False, True))
