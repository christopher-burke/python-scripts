#!/usr/bin/env python3

"""Demo on asyncio."""

import asyncio
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

urls = ('https://news.ycombinator.com/rss',
        'https://planetpython.org/rss20.xml',

        )


def title(content):
    """Get the HTML title."""
    soup = BeautifulSoup(content, 'html.parser')
    return soup.title


async def fetch(url):
    """Async function to get URL."""
    r = requests.get(url)
    return r


async def handler(urls):
    """Async handler."""
    tasks = []
    for url in urls:
        tasks.append(asyncio.ensure_future(fetch(url=url)))

    print(dt.now().today())
    print('Getting the RSS feeds.')
    print('Printing the titles.')
    await asyncio.wait(tasks)

    for task in tasks:
        print(title(task.result().content))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(handler(urls)))
