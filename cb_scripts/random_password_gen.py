#! /usr/bin/env python
"""Class based random password generator.  Uses string, random, sys modules."""


import random
import string
import sys


class RandomPassword:
    """RandomPassword class."""

    def __init__(self, length=20):
        """Random Passord class __init__ method."""
        self.length = length

    def password_gen(self):
        """password_gen method that generates a passwords randomly."""
        # remove all escape characters
        x = repr(string.printable.replace(' \t\n\r\x0b\x0c', ''))
        s = ""
        for i in range(self.length):
            s += random.choice(x)
        return s


if __name__ == "__main__":
    if len(sys.argv) > 1:
        rp = RandomPassword(int(sys.argv[1]))
    else:
        rp = RandomPassword()
    print(rp.password_gen())
