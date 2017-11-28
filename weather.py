#!/usr/bin/python

"""Weather from weather.gov."""

__author__ = "Christopher James Burke"
__copyright__ = ""
__credits__ = ["Christopher James Burke"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Christopher James Burke"
__email__ = "christopherjamesburke@gmail.com"
__status__ = "Production"
__date__ = "2014/10/02 21:19:35"

import requests
from bs4 import BeautifulSoup as soup

# Go to http://w1.weather.gov/xml/current_obs/ and pick the
# XML weather observations feed.


def main(feed="http://w1.weather.gov/xml/current_obs/"):
    """Weather feed from weather.gov."""
    r = requests.get(feed)
    root = soup(r.text)
    station = root.findAll('station_id')[0].text
    temp = root.findAll('temperature_string')[0].text
    weather = root.findAll('weather')[0].text

    return "{} {} {}".format(station, temp, weather)


if __name__ == "__main__":
    print(main())
