#!/usr/bin/env python3

"""Get the latest stable version number of Python from FTP site."""

import requests
import re
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
    r = requests.get(url)
    py_versions = parse(r.content)
    return py_versions[-1][:-1]


def main(url):
    """Return the version number."""
    c = latest(url)
    print(c)


if __name__ == "__main__":
    url = 'https://www.python.org/ftp/python/'
    main(url=url)
