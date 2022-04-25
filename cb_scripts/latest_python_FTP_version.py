#!/usr/bin/env python3

"""Get the latest stable version number of Python from FTP site.
pip install requests beautifulsoup4
"""

import re
import sys
from typing import Optional

import requests
from bs4 import BeautifulSoup


def parse(content):
    """Find the Download Widget class."""
    soup = BeautifulSoup(content, "html.parser")
    ftp_links = [a.text for a in soup.select('a')]
    regex = re.compile(r'(?<!.)(\d[\d.]+)')
    versions = filter(regex.search, ftp_links)
    versions = [tuple(map(int, re.sub("/", "", version).split('.')))
                for version in versions]
    return versions


def latest(url: str) -> Optional[str]:
    """Find the latest python version number."""
    response = requests.get(url)
    if response.status_code == 200:
        py_versions = sorted(parse(response.content))
        return py_versions[-1]
    return None


def main(url: str) -> None:
    """Return the version number."""
    version = latest(url)
    if version:
        print(".".join(map(str, version)))
    else:
        print('Error')
        sys.exit(1)


if __name__ == "__main__":
    url = 'https://www.python.org/ftp/python/'
    main(url=url)
