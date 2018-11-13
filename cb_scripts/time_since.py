#!/usr/bin/env python3

"""Time since a given date.

requires dateutil package:
`pip install python-dateutil`
"""

import sys
import time
from datetime import datetime
from dateutil import relativedelta


def print_time_since(date):
    """Print the time since in a while True loop."""
    while True:
        output = time_since(date)
        print(output, end='\r')
        time.sleep(0.1)


def time_since(date):
    """Print the time since the given date."""
    now = datetime.now()
    difference = relativedelta.relativedelta(now, date)
    years = difference.years
    months = difference.months
    days = difference.days
    hours = difference.hours
    minutes = difference.minutes
    seconds = difference.seconds

    return f'\t{years:02} years, {months:02} months, {days:02} days ' \
        f'{hours:02}:{minutes:02}:{seconds:02}'


if __name__ == "__main__":
    try:
        start_date = datetime(1969, 1, 12)  # Jets won SBIII
        print_time_since(date=start_date)
    except KeyboardInterrupt:
        sys.exit(0)
