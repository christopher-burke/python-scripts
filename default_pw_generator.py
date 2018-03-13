#!/usr/bin/env python3

"""Default initial password generator.

Logic divided into three parts:

1. First letter of first name capitalized.
2. First letter of last name lower case.
3. Date of birth in YYYYMMDD format.
"""

from collections import namedtuple

PasswordGenerator = namedtuple('PasswordGen', 'first_name last_name dob')


def first_part(txt):
    """First logical part for password."""
    return txt[0].upper()


def second_part(txt):
    """Second logical part for password."""
    return txt[0].lower()


def third_part(txt):
    """Third locial part for password."""
    m, d, y = txt.split('/')
    return f'{y.zfill(4)}{m.zfill(2)}{d.zfill(2)}'


def password_gen(txt):
    """Generate a password."""
    password = PasswordGenerator(*txt.split())
    pw_part1 = first_part(password.first_name)
    pw_part2 = second_part(password.last_name)
    pw_part3 = third_part(password.dob)
    pw = f'{pw_part1}{pw_part2}{pw_part3}'
    return pw


if __name__ == "__main__":
    # Fake data to test.
    INPUTS = ('Joseph Smith 4/2/1969',
              'Johnny Appleseed 7/2/1979',
              'Jane Doe 6/10/1999',
              'Sammy Ditch 01/02/1980',
              'Philomena Ledbetter 3/11/1990',
              'Virgen Schoen 07/21/2001',
              'Robin Snook 08/23/1998',
              'Lachelle Mankin 11/8/1955',
              )
    for input_ in INPUTS:
        print(password_gen(input_))
