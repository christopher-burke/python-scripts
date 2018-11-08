#!/usr/bin/env python3

"""Monty Hall Game."""


from random import shuffle, randint


class MontyHallGame:
    """Class to simulate the Monty Hall Problem."""

    def __init__(self, debug: bool = False, shuffle: int = 0):
        """Create MonthHallGame object."""
        self.DEBUG = debug
        shuffle_count = shuffle or randint(1, 100)
        PRIZES = self.mixup_door_prizes(shuffle_count)
        self.DOORS = dict(zip([f'{x}' for x in range(1, 4)], PRIZES))
        self.DOORS_SET = set(self.DOORS.keys())
        self.selection = 0
        self.win = self.main()

    def mixup_door_prizes(self, shuffle_count):
        """Randomly mix up the door prizes."""
        PRIZES = ['CAR', 'GOAT', 'GOAT', ]
        for x in range(shuffle_count):
            shuffle(PRIZES)
        return PRIZES

    def select(self, message):
        """Get user door selection."""
        self.selection = input(f'{message}')

    def results(self):
        """Determine if user won or lost."""
        if self.DOORS[self.selection] == 'CAR':
            print('You win!')
            return True
        else:
            print('You lose.')
            return False

    def make_a_deal(self):
        """Let's Make a Deal game logic."""
        start_message = 'Choose door 1, 2, or 3: '
        self.select(start_message)
        unselected = self.DOORS_SET.difference((self.selection,))
        for door in unselected:
            if self.DOORS[door] == 'GOAT':
                self.selection = 0
                doors_left = sorted(self.DOORS_SET.difference((door,)))
                change_door_message = f'Door {door} has a GOAT. ' \
                    f'Choose {", ".join(doors_left)}: '
                while self.selection not in doors_left:
                    self.select(change_door_message)
                break
        return self.results()

    def main(self):
        """Run game."""
        win = self.make_a_deal()

        if self.DEBUG:
            print(self.DOORS)

        return win


if __name__ == "__main__":
    mhg = MontyHallGame()

    results = {'win': 0, 'loss': 0}
    for x in range(1, 201):
        mhg = MontyHallGame()
        if mhg.win:
            results
