#!/usr/bin/env python3

"""Get Articles from website urls.

Creates a Markdown file of Articles.
"""

from itertools import chain
from dataclasses import dataclass
import asyncio
import requests
from bs4 import BeautifulSoup


urls = ('https://news.ycombinator.com/rss',
        'https://planetpython.org/rss20.xml',
        'https://kk.org/cooltools/feed/',
        'https://pypi.org/rss/packages.xml',
        )


def helper(item):
    link = str(item.link).strip()
    if link == '<link/>':
        link = item.link.next_sibling
    else:
        link = item.link
    return {'title': item.title,
            'link': link.strip(),
            'pubdate': item.pubdate,
            'description': item.description,
            'source': item.title(), }


@dataclass
class Article:
    """Class for keeping track of Articles from feeds."""

    title: str
    link: str
    pubdate: str
    description: str
    source: str

    def __post_init__(self):
        """Dataclass clean up."""
        self.title = self.title.text.strip()
        self.pubdate = self.pubdate.text.strip()

    def __lt__(self, other):
        """Less than method for sorting."""
        return self.pubdate < other.pubdate


class Parser:
    """Parser for web content."""

    def __init__(self, content):
        """Parser class init."""
        self.content = content
        self.soup = BeautifulSoup(content, 'html.parser')

    def __repr__(self):
        """Return the parser reper."""
        return f'Parser({self.content})'

    def items(self):
        """Get the Items."""
        return self.soup.select('item')

    def available_tags(self):
        """Return a set of tags in html."""
        return set([_.name for _ in self.soup.find_all(recursive=True)])

    def title(self):
        """Get the HTML title."""
        return soup.title


async def fetch(url):
    """Async function to get URL."""
    r = requests.get(url)
    await asyncio.sleep(0.000000001)
    return r


async def handler(urls):
    """Async handler."""
    futures = []
    loop = asyncio.get_event_loop()
    for url in urls:
        futures.append(
            loop.run_in_executor(None, requests.get, url)
        )

    await asyncio.wait(futures)

    return [Parser(content=task.result().content) for task in futures]


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(asyncio.gather(handler(urls)))
    articles = [Article(**helper(art))
                for item in chain(*result)
                for art in item.items()
                ]

    with open('articles.md', 'w') as f:
        for article in sorted(articles):
            f.write(f'* [{article.title}]({article.link}) - {article.source} -{article.pubdate} \n')
