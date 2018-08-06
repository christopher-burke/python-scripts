#!/usr/bin/env python3

"""Get the latest version number of Python."""

import requests
import re
from bs4 import BeautifulSoup


def parse(content):
    """Find the Download Widet class."""
    soup = BeautifulSoup(content, "html.parser")
    dw = soup.select('div.download-widget')
    return dw[-1].text


def latest(url):
    """Find the latest python version number."""
    r = requests.get(url)
    result = parse(r.content)
    py_version = re.findall(r'Python ([\d,\.]+)+', result, re.I)
    return py_version[-1]


def main(url):
    """Return the version number."""
    c = latest(url)
    print(c)


if __name__ == "__main__":
    url = 'https://python.org'
    main(url=url)
