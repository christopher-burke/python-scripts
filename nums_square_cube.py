#!/usr/bin/env python3

"""Squares and Cubes for a range of numbers.

Given a start and end, calucate the Square x**2 and
the Cube x**3 for all numbers.

Example of generator and tuple packing/unpacking.
"""


def main(start, end):
    """Square and cube all numbers in range of start to end."""
    for i in range(start, end+1):
        square, cube = i**2, i**3
        yield i, square, cube


if __name__ == "__main__":
    print("number\tsquare\tcube")
    for x in main(1, 10):
        print("{}\t{}\t{}".format(*x))
