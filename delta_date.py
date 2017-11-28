#!/usr/bin/python

r"""Return the delta of the current date.

Based on the past/futureand number of days/weeks.
"""

__author__ = "Christopher James Burke"
__credits__ = ["Christopher James Burke"]
__version__ = "1.0.0"
__maintainer__ = "Christopher James Burke"
__email__ = "christopherjamesburke@gmail.com"
__date__ = "2013/02/01 13:01:42"

import sys
from operator import add, sub
from datetime import timedelta, datetime


def time_date_n(time, time_frame, n):
    """Return the date based on.

    time = past or future
    time_frame = days or weeks
    n = interger base 10
    """
    weeks = 1
    if time_frame.lower() == 'weeks':
        weeks = 7
    operation = add
    if time.lower() == 'past':
        operation = sub
    n = operation(datetime.now(), timedelta(days=(n * weeks)))
    return n.date()


def time_diff(date_in):
    """Time diff."""
    if date_in > datetime.now().date():
        return ((date_in - datetime.now().date()).days, 'Until',)
    else:
        return ((datetime.now().date() - date_in).days, 'From',)


def time_diff_print(date_in):
    """time_diff."""
    print(date_in.strftime("%B %d, %Y"))
    print('{0} {1}'.format('%d days %s' % (time_diff(date_in)),
                           date_in.strftime("%B %d, %Y")))


if __name__ == "__main__":
    kwargs = {
        'time': sys.argv[1],
        'time_frame': sys.argv[2],
        'n': int(sys.argv[3])
    }
    if kwargs['n'] == 1:
        print("{n} %s in the {time}".format(**kwargs) %
              (kwargs['time_frame'][:-1]))
    else:
        print("{n} {time_frame} in the {time}:".format(**kwargs))
    date_in = time_date_n(**kwargs)
    print(date_in.strftime("%B %d, %Y"))
