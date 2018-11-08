#!/usr/bin/env python3

"""Useful Weekday wrappers."""


from datetime import date
from calendar import day_name


def week_num() -> int:
    """Return the current week number."""
    return date.today().isocalendar()[1]


def weekday_num() -> int:
    """Return the current weekday number.

    Using the Python datetime: 0 is Sunday, 6 is Saturday.
    """
    weekday_num = date.today().isocalendar()[2]
    return weekday_num


def weekday() -> str:
    """Return the currecnt weekday name."""
    weekday_num = date.today().isocalendar()[2]
    return day_name[weekday_num]


if __name__ == "__main__":
    print(week_num())
