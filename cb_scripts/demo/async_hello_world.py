#!/usr/bin/env python3

"""`Hello, world.` example using asyncio."""

import asyncio


async def main():
    """Print `Hello, world.`."""
    print('Hello, world.')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
