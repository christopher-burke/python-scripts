#!/usr/bin/env python3


"""Salutation.

Determine whether to say "Good Morning", "Good Afternoon" or "Good Evening".
"""

from datetime import datetime


def salutation(hour: int) -> str:
    """Determine the correct salutation using the hour parameter."""
    greetings = ((range(0, 12), "Good Morning",),
                 (range(12, 17), "Good Afternoon"),
                 (range(17, 24), "Good Evening"),)
    return list(filter(lambda x: hour in x[0], greetings))[0][1]


def main(hour: int) -> str:
    """Salutation main method."""
    return salutation(hour)


if __name__ == "__main__":
    now = datetime.now().hour
    print(main(now))
