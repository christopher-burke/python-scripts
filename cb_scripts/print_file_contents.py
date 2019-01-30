#!/usr/bin/env python3

"""Print file contents.

Read file line by line print to terminal.

Useful when files exceed the limit of being open by text editors.
"""

import sys


def print_lines(file_name):
    """Print Lines to Terminal."""
    with open(f'{file_name}', 'r')as fin:
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
