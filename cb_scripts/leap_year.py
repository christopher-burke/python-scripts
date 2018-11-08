#!/usr/bin/env python3

"""Leap Year tester.

Given a year, determine if the it's a leap year.
"""
import sys
from datetime import date


def leap_year(year):
    """Determine if a year is a leap year."""
    try:
        d = date(year, 2, 29)
    except ValueError:
        return f"{year} is not a leap year."
    return f"{d.year} is a leap year."


if __name__ == "__main__":
    try:
        year = int(sys.argv[1])
        print(leap_year(year))
    except TypeError:
        print("Please type a numeric year.")
