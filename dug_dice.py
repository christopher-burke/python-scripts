#!/usr/bin/python

r"""Dug Dice.

At the DUG Conference (Datatel Users Group conference), I got a gift of dice.
Each die had a saying and when rolled you get a motivational phrase/saying.
"""

__author__ = "Christopher James Burke"
__copyright__ = ""
__credits__ = ["Christopher James Burke"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Christopher James Burke"
__email__ = "christopherjamesburke@gmail.com"
__status__ = "Production"
__date__ = "2013/09/13 10:04:31"

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
