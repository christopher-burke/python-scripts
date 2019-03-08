#!/usr/bin/env python3

"""Find Biggest file.

Find the biggest file in a path."""

from pathlib import Path


def compare(a, b):
    """Compare the file sizes."""
    if a[1] < b[1]:
        return b
    else:
        return a


def find_biggest(path):
    """Find the biggest directory and file in path."""
    max_dir = ('', 0,)
    max_file = ('', 0,)
    path_ = Path(path)
    print(f"Drive {path_} is {path_.stat().st_size}.")

    max_dir = compare(max_dir, (f"{path_}", path_.stat().st_size,))
    for i in Path(path).iterdir():
        if i.is_dir():
            biggest_dir_, biggest_file_ = find_biggest(i)
            max_dir = compare(max_dir, biggest_dir_)
            max_file = compare(max_file, biggest_file_)
        else:
            try:
                max_file = compare(max_file, (f'{i}', i.stat().st_size,))
            except FileNotFoundError:
                print(f"File not found. {i}")

    return (max_dir, max_file,)


def main():
    """Run find_biggest with Home dir."""
    print(find_biggest(f"{Path('~').expanduser()}"))


if __name__ == "__main__":
    main()
