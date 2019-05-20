#!/usr/bin/env python3

"""Mouse Mover.

Script to move the mouse cursor to the main screen. Useful for
multiple screen setup.

Requires pyautogui

## Windows needs:
    pip install pyautogui

## macOS needs:
    pip3 install pyobjc-core
    pip3 install pyobjc
    pip3 install pyautogui

## Linux needs:
    pip3 install python3-xlib
    sudo apt-get install scrot
    sudo apt-get install python3-tk
    sudo apt-get install python3-dev
    pip3 install pyautogui
"""


try:
    import pyautogui
except ImportError:
    import sys
    print(__doc__)
    sys.exit(0)


def move_mouse(x: int, y: int, num_seconds: int = 0):
    """Helper function to pyautogui.moveTo."""
    pyautogui.moveTo(x, y, duration=num_seconds)


def move_mouse_main_screen():
    """Move mouse cursor to location (100,100)."""
    move_mouse(100, 100)


def main():
    """Move mouse main method. Do not import."""
    move_mouse_main_screen()


if __name__ == "__main__":
    main()
