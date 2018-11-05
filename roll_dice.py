#!/usr/bin/env python3

"""Roll a die.

Uses random module to simulate rolling a die.
"""

import random


def roll_dice(sides=6) -> int:
    """Simulate Rolling a die.

    Uses random.randrange to calculate the roll.
    sides defaults to 6 sides.

    :param sides: number of sides the die has.
    :return: the int value of the roll.
    """
    sides += 1  # Include the last number for randrange.
    roll = random.randrange(1, sides)
    return roll


def main():
    """Roll the die."""
    print('Rolling a 10-sided die.')
    for _ in range(1, 11):
        print(roll_dice())

    print('Rolling a 10-sided die.')
    for _ in range(1, 11):
        print(roll_dice(sides=10))


if __name__ == "__main__":
    main()
