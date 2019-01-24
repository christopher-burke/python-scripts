#!/usr/bin/env python3

"""What next?

Script that chooses a random action from a set of actions and suggests
an action to the user.
"""


import random


class WhatNextAction:
    """What Next Action Class."""

    def __init__(self, *args, **kwargs):
        """Create a list of common actions and create a random action order."""
        self.actions = set(
            (
                'play games (video/board)',
                'play Guitar',
                'nap/rest/relax 10-20 mins',
                'read a Book (non-programming)',
                'read a programming Book',
                'watch a YouTube Video',
                'clean',
                'move around',
            )
        )
        self.message = 'You could'
        self.random_actions = random.sample(self.actions,
                                            len(self.actions))

    def pick(self):
        """Random Action Picker, implemented as a generator.

        Pick a random order to actions.
        """
        for action in self.random_actions:
            yield f'{self.message} {action}.'

    def one(self):
        """Pick one action from actions."""
        for action in self.random_actions:
            yield f'{self.message} {action}.'

    def all(self):
        """Return a random ordered set action from actions."""
        yield from self.pick()


if __name__ == "__main__":
    # Create WhatNextAction object.
    actions = WhatNextAction()
    # Pick one action.
    print(next(actions.one()))

    # Pick All actions:
    # for action in actions.all():
    #    print(action)
