#!/usr/bin/env python3

"""Rhythmic breathing."""

from time import sleep
import sys


def breathe(inhale_time: int = 4, exhale_time: int = 6):
    """Breathe in and out at a set pace.

    inhale_time int time in seconds.
    exhale_time int time in seconds.
    """
    for _ in range(0, inhale_time+1):
        sys.stdout.write('\r')
        sys.stdout.write("[BREATH IN ] {}".format(_))
        sys.stdout.flush()
        sleep(1)

    for _ in reversed(range(0, exhale_time+1)):
        sys.stdout.write('\r')
        sys.stdout.write("[BREATH OUT] {}".format(_))
        sys.stdout.flush()
        sleep(1)


if __name__ == "__main__":
    try:
        while True:
            breathe()
    except KeyboardInterrupt:
        print("\nThank you")
