#!/usr/bin/env python3

"""Bingo ball class.

    The Bingo balls letters and numbers:
        * "B" (numbers 1–15)
        * "I" (numbers 16–30)
        * "N" (numbers 31–45)
        * "G" (numbers 46–60)
        * "O" (numbers 61–75)
"""


class BingoBall:
    """Bingo Ball."""
    def __init__(self,letter,number):
        self.letter = letter
        self.number = number

    def __str__(self):
        return f'{self.letter}{self.number}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.letter}, {self.number})'


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
            yield BingoBall(letter, value)
            if value % 15 == 0:
                break
