#!/usr/bin/env python3

"""Hello, World! Asyncio demo.

Code Source:
    Miguel Grinberg 
    Asynchronous Python for the Complete Beginner PyCon 2017
    https://www.youtube.com/watch?v=iG6fr81xHKA
"""

import asyncio

loop = asyncio.get_event_loop()


async def hello():
    """Print 'Hello, World!'."""
    print('Hello,')
    await asyncio.sleep(3)
    print('World!')


if __name__ == "__main__":
    loop.run_until_complete(hello())
