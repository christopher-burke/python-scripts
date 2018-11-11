#!/usr/bin/env python3

"""Traffic light simulation.

Got the idea from Python Bites (https://pybit.es/).
"""

from time import sleep
from itertools import cycle

RED, YELLOW, GREEN = 'RED', 'YELLOW', 'GREEN'
LIGHT = cycle((RED, YELLOW, GREEN))


def traffic_light(delay):
    """Simulate a traffic light."""
    for color in LIGHT:
        print(color, end='\r')
        if color == 'YELLOW':
            sleep(delay // 3)
        else:
            sleep(delay)


def main(delay):
    """Run simulated traffic light."""
    traffic_light(delay)


if __name__ == "__main__":
    main(delay=10)
