#!/usr/bin/env python3

"""Lock the Screen."""

from subprocess import Popen, PIPE


def lock_screen():
    """Lock the screen. For macOS."""
    command = r'/System/Library/CoreServices' \
        r'/Menu\ Extras/User.menu' \
        r'/Contents/Resources/CGSession' \
        r' -suspend'
    Popen(command, shell=True, stdout=PIPE)


if __name__ == "__main__":
    lock_screen()
