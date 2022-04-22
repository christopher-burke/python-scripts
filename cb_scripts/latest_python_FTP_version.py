#!/usr/bin/env python3

"""Get the latest stable version number of Python from FTP site.

pip install requests beautifulsoup4
"""

import re

import requests
from bs4 import BeautifulSoup


def parse(content):
    """Find the Download Widget class."""
    soup = BeautifulSoup(content, "html.parser")
    ftp_links = [a.text for a in soup.select('a')]
    regex = re.compile(r'(?<!.)(\d[\d.]+)')
    versions = filter(regex.search, ftp_links)
    return list(versions)


def latest(url):
    """Find the latest python version number."""
    response = requests.get(url)
    py_versions = sorted(parse(response.content))
    return py_versions[-1][:-1]


def main(url):
    """Return the version number."""
    version = latest(url)
    print(version)


if __name__ == "__main__":
    url = 'https://www.python.org/ftp/python/'
    main(url=url)
