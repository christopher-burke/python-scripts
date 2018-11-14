#!/usr/bin/env python3

"""Time Zone - Resolve what time is it?

Find out what time of a given location.
"""

import os
import pytz
from datetime import datetime
from timezonefinder import TimezoneFinder
from pygeocoder import Geocoder
from collections import namedtuple

TimeZoneResult = namedtuple('TimeZoneResult', ['location', 'time'])

API_KEY = os.getenv('API_KEY')


def main():
    """Find the time of a given location.

    :return: A namedtuple, TimeZoneResult with location and time.
    """
    location = str(input('Location : '))
    geocode_result = Geocoder(API_KEY).geocode(location)
    coordinates = geocode_result.data[0]['geometry']['location']
    location = geocode_result.data[0]['formatted_address']
    timezone = TimezoneFinder().timezone_at(**coordinates)
    time = datetime.now(pytz.timezone(timezone))
    return TimeZoneResult(location=location, time=time)


if __name__ == "__main__":
    print(main())
