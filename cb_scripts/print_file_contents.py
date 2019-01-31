#!/usr/bin/env python3

"""Print file contents.

Read file line by line print to terminal.

Useful when files exceed the limit of being open by text editors.
"""

import sys


class FileManager:
    """File Manager class."""

    def __init__(self, name):
        """File Manager init method."""
        self.name = name

    def __enter__(self):
        """Context Manager enter method.s"""
        self.file = open(self.name, 'r')
        return self.file

    def __exit__(self, *args):
        """Exit magic method."""
        if self.file:
            self.file.close()


def print_lines(file_name):
    """Print Lines to Terminal."""
    with FileManager(f'{file_name}') as fin:
        for line in fin:
            print(line)


def main(file_name):
    """Run the main program."""
    print_lines(file_name=file_name)


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        print('No file name provided.')
        sys.exit(1)
    main(file_name=file_name)
    sys.exit(0)
