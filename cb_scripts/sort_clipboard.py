#!/usr/bin/env python3


"""Sort Clipboard using pyperclip.

requirement pyperclip:
`pip install pyperclip`

"""

from pyperclip import copy, paste


def main():
    """Sort clipboard."""
    clipboard = paste().split('\n')
    clipboard.sort()
    copy("\n".join(clipboard))


if __name__ == "__main__":
    main()
