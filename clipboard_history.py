#!/usr/bin/env python3

"""Clipboard History.

Create a file that logs the text copied to the clipboard.
"""


import pyperclip
from collections import namedtuple, OrderedDict
from datetime import datetime
import time
import pathlib
import json


CopiedItem = namedtuple('CopiedItem', ['text', 'date', 'time'])


def write(item: CopiedItem):
    """Write the copied item to the file."""
    clipboard_history_file = pathlib.Path.home() / 'clipboard_history.json'
    try:
        with open(f'{clipboard_history_file}', 'a') as fout:
            json.dump(item._asdict(), fout)
    except FileNotFoundError:
        with open(f'{clipboard_history_file}', 'w') as fout:
            json.dump(item._asdict(), fout)


def main():
    """Main function of program."""
    copy_value = ""
    while True:
        new_value = pyperclip.paste()
        if new_value != copy_value:
            copy_value = new_value
            now = datetime.now()
            cp = CopiedItem(text=copy_value,
                            date=now.date().strftime('%Y-%m-%d'),
                            time=now.time().strftime('%I:%M:%S%p'))
            write(cp)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
