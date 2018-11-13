#!/usr/bin/env python3

"""Lock the Screen."""

from subprocess import Popen, PIPE
from platform import system


os_lock_commands = {
    'darwin':
        ['/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession',
         '-suspend',
         ],
    'linux':
        ['gnome-screensaver-command',
         '--lock',
         ],
}


def lock_screen():
    """Lock the screen.

    For macOS, Linux or Windows operating systems.
    """
    os_system = system().lower()
    if os_system == 'windows':
        import ctypes
        ctypes.windll.user32.LockWorkStation()
    else:
        command = os_lock_commands[os_system]
        Popen(command, shell=False, stdout=PIPE)


if __name__ == "__main__":
    lock_screen()
