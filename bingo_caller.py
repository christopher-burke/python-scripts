#!/usr/bin/env python3

"""Bingo ball generator.

    The Bingo balls letters and numbers:
        * "B" (numbers 1–15)
        * "I" (numbers 16–30)
        * "N" (numbers 31–45)
        * "G" (numbers 46–60)
        * "O" (numbers 61–75)
"""

from collections import namedtuple
from random import shuffle
from time import sleep
import sys

bingo_ball = namedtuple("BingoBall", ["letter", "number"])


def letters():
    """Bingo Ball letter generator."""
    letters = "BINGO"
    for letter in letters:
        yield letter


def numbers():
    """Bingo Ball values generator."""
    for number in range(1, 76):
        yield number


def bingo_balls():
    """Bingo Balls."""
    bingo_letters = letters()
    bingo_number = numbers()
    for letter in bingo_letters:
        for value in bingo_number:
            yield bingo_ball(letter, value)
            if value % 15 == 0:
                break


def bingo_drum():
    """Bingo Drum, shuffled."""
    drum = [ball for ball in bingo_balls()]
    shuffle(drum)
    return drum


def call():
    """Call the Bingo Balls picked."""
    for pick in bingo_drum():
        print(f' {pick.letter}', end='\r')
        sleep(1.5)
        print(f' {pick.number}', end='\r')
        sleep(1.5)
        print(f"{pick.letter} {pick.number}")


if __name__ == "__main__":
    call()
