#!/usr/bin/env python3

"""Bingo Drum class."""


from ball import bingo_balls
from random import shuffle


def bingo_drum():
    """Bingo Drum, shuffled."""
    drum = [ball for ball in bingo_balls()]
    for _ in range(100):
        shuffle(drum)
    return drum
