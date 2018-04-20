#!/usr/bin/env python3

"""Week number matchups for Fantasy Baseball."""

import calendar
from datetime import date, timedelta


def matchup_start_dates(start, end, skip_dates):
    """Find the start date for each matchup."""
    yield start
    next_matchup = start + timedelta(days=7)
    while (next_matchup < end):
        weekday_num = next_matchup.weekday()
        if calendar.day_name[weekday_num] is not 'Monday':
            add_days = timedelta(7 - weekday_num)
            next_matchup = next_matchup + add_days
        if next_matchup in skip_dates:
            continue
        if next_matchup < end:
            yield next_matchup


if __name__ == "__main__":
    start = date(2018, 3, 29)  # start day of season.
    end = date(2018, 9, 30)  # last day of season.
    skip_dates = [date(2018, 7, 23), ]  # All Start break is extened.
    matchup_gen = matchup_start_dates(start, end, skip_dates)

    today = date.today()

    # Get the current week number matchup.
    for weekno, start_date in list(enumerate(matchup_gen, 1)):
        if today < start_date:  # find the next week matchup.
            print(weekno - 1)  # Current week matchup.
            break
    # matchup_gen = matchup_start_dates(start, end, skip_dates)
