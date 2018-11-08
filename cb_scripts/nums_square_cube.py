#!/usr/bin/env python3

"""Squares and Cubes for a range of numbers.

Given a start and end, calucate the Square x**2 and
the Cube x**3 for all numbers.

Example of generator and functools.partial.
"""


from functools import partial


def power(base, exponent):
    """Raise a base to the exponent."""
    return base ** exponent


square = partial(power, exponent=2)
cube = partial(power, exponent=3)


def main(start, end):
    """Square and cube all numbers in range of start to end."""
    for i in range(start, end+1):
        yield i, square(i), cube(i)


if __name__ == "__main__":
    print("number\tsquare\tcube")
    for x in main(1, 10):
        print("{}\t{}\t{}".format(*x))
