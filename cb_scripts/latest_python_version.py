#!/usr/bin/env python3

"""Get the latest version number of Python."""

import requests
import re
from bs4 import BeautifulSoup
import asyncio
from functools import partial


async def fetch(url):
    """Async function to get URL."""
    r = requests.get(url)
    return r


def regex(pattern):
    """Return compiled regular expression pattern."""
    return re.compile(pattern)


def parse(content, div_select):
    """Find the Download Widget class."""
    soup = BeautifulSoup(content, "html.parser")
    dw = soup.select(div_select)
    return dw


async def pparse(div_select):
    """Build parser partially."""
    return partial(parse, div_select=div_select)


async def handler(url, pattern, div_select):
    """Asyncio handler."""
    py_website = asyncio.ensure_future(fetch(url=url))
    parser = asyncio.ensure_future(pparse(div_select=div_select))
    py_version_regex = regex(pattern=pattern)
    await asyncio.wait([py_website])
    py_website_source = py_website.result().content
    await asyncio.wait([parser])
    py_latest_div_parser = parser.result()
    result = py_latest_div_parser(content=py_website_source)
    py_version = py_version_regex.findall(str(result), re.I)

    return py_version[-1]


def main(url, pattern, div_select):
    """Print the version number."""
    loop = asyncio.get_event_loop()
    c = loop.run_until_complete(asyncio.gather(
        handler(url=url,
                pattern=pattern,
                div_select=div_select)))

    print(*c)


if __name__ == "__main__":
    url = 'https://python.org'
    pattern = r'(?<=Latest: )<a[\w\W\s\S]+(?<=Python )([\d\.]+)(?=</a></p>)'
    div_select = 'div.download-widget'
    main(url=url, pattern=pattern, div_select=div_select)
