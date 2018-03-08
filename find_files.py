#!/usr/bin/env python3

"""Find all files matching a pattern."""

import fnmatch
from pathlib import Path

PATTERN = '*.py'
HOME_DIR = Path.home()
SEARCH_DRIVE = HOME_DIR
matches = 0


def search(path, pattern):
    """Search path with pattern.

    Print the files found in the directory first,
    then search any subdirectories.

    Returns total number of matches.
    """
    global matches
    directories = [dir_ for dir_ in path.iterdir() if dir_.is_dir()]
    files = [file_.as_posix() for file_ in path.iterdir()
             if file_.is_file() and fnmatch.fnmatchcase(file_.name, pattern)]
    if files:
        matches += len(files)
        print("\n".join(files))
    for dir_ in directories:
        search(dir_, pattern)


if __name__ == "__main__":
    search(SEARCH_DRIVE, PATTERN)
    print(f'Total of {matches} "{PATTERN}" files found in {SEARCH_DRIVE}.')
