#!/usr/bin/env python3


"""Demo of aiohttp package."""


import aiohttp
import asyncio


async def fetch(session, url):
    """Fetch the url."""
    async with session.get(url) as response:
        return await response.text(encoding='utf-8')


async def task(url):
    """Async task function."""
    print(f'{url} started.')
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
    print(f'{url} done.')


async def main():
    """Main function."""
    tasks = []

    urls = ('https://news.ycombinator.com/rss',
            'https://planetpython.org/rss20.xml',
            'https://python.org',
            )

    for url in urls:
        tasks.append(loop.create_task(task(url)))

    await asyncio.wait(tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
