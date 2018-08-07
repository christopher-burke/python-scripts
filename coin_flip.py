#!/usr/bin/env python3

"""Coin Flip.

Simple coin flip example.
"""

import sys
from random import getrandbits
from collections import defaultdict


def create_coin(coin: tuple=('HEADS', 'TAILS',)):
    """Define a your coin.

    coin - tuple with 2 values. Default (heads, tails,)
    """
    COIN = {True: coin[0], False: coin[1]}
    return COIN


def flip():
    """Simulate the flip of a coin using getrandbits."""
    return bool(getrandbits(1))


def main(times):
    """Flip a coin main function."""
    coin = create_coin()
    RESULTS = defaultdict(lambda: 0)

    if times > 1:
        for _ in range(times):
            result = coin[flip()]
            RESULTS[result] += 1
        return f'{coin[True]}: {RESULTS[coin[True]]}, ' \
               f'{coin[False]}: {RESULTS[coin[False]]}'
    else:
        return f'{coin[flip()]}'


if __name__ == "__main__":
    try:
        times = sys.argv[1]
    except IndexError:
        times = 1
    times = int(times)
    print(main(times))
