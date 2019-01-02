#!/usr/bin/env python3

"""Today Holiday?

Uses third party library holidays.
`pip install holidays`
"""

import holidays
from datetime import date


def main() -> str:
    """Determine if today is a US Holiday."""
    today = date.today()
    us_holidays = holidays.UnitedStates(years=today.year)
    today_holiday = today in us_holidays

    if today_holiday:
        return us_holidays[today]

    return "Not a holiday today."


if __name__ == "__main__":
    print(main())
