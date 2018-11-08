#!/usr/bin/env python3

"""Bingo caller.

    The Bingo balls letters and numbers:
        * "B" (numbers 1–15)
        * "I" (numbers 16–30)
        * "N" (numbers 31–45)
        * "G" (numbers 46–60)
        * "O" (numbers 61–75)
"""

import pickle
from time import sleep
from ball import BingoBall
from drum import bingo_drum


class BingoCaller:
    """Bingo Game Caller."""

    def __init__(self):
        """Create and shuffle the drum of bingo balls."""
        self.drum = bingo_drum()
        self.pick_index = 0

    def reset(self):
        """Reset the bingo_run.p file."""
        reset_game = input("Reset previous ran game? ")
        if reset_game in ('Y', 'y', 'Yes', 'YES'):
            f = open('bingo_run.p', 'w')
            f.truncate()
            f.close()

    def load(self):
        """Load new or previous game."""
        try:
            with open('bingo_run.p', 'rb') as f:
                self.drum = pickle.load(f)
                self.pick_index = pickle.load(f)
        except EOFError:
            self.drum = self.drum
            self.pick_index = 0

    def call_log(self, sort=False):
        """Return Called ball log."""
        if sort:
            return sorted(self.drum[:self.pick_index],
                        key=lambda b: b.number)
        return self.drum[:self.pick_index]

    @staticmethod
    def read(ball, sleep_timer=1.5):
        """Read the picked ball with sleep timer delay."""
        print(f'\t{ball.letter}', end='\r')
        sleep(sleep_timer)
        print(f'\t{ball.number}', end='\r')
        sleep(sleep_timer)
        print(f"\t{ball}")
        sleep(sleep_timer)

    def call(self):
        """Call the Bingo Balls picked."""
        self.reset()
        while True:
            self.load()

            for sort in(True, False):
                for ball in self.call_log(sort):
                    print(ball)
                print()

            try:
                for pick in self.drum[self.pick_index:]:
                    self.read(pick)
            except KeyboardInterrupt:
                with open('bingo_run.p', 'wb+') as f:
                    pickle.dump(self.drum, f)
                    pickle.dump(self.drum.index(pick), f)
            game_over = input("Do we have a winner? ")
            if game_over in ('Y', 'y', 'Yes', 'YES'):
                print('We have a winner!')
                break


if __name__ == "__main__":
    BingoCaller().call()
