#!/usr/bin/python

r"""Dug Dice.

At the DUG Conference (Datatel Users Group conference), I got a gift of dice.
Each die had a saying and when rolled you get a motivational phrase/saying.
"""

import random

die1 = [
    "Without fear",
    "x2",
    "with passion",
    "today",
    "right away",
    "genuinely",
]

die2 = [
    "recognize someone",
    "be sincere",
    "think...",
    "set a goal",
    "be thankful",
    "share an idea",
]

if __name__ == "__main__":
    die1_roll = random.randint(0, 5)
    die2_roll = random.randint(0, 5)

    roll = [die1[die1_roll], die2[die2_roll]]

    saying = roll.pop(random.randint(0, 1)) + " "
    saying += saying.join(roll)

    print(saying)
