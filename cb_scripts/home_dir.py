#!/usr/bin/env python3

"""Home directory."""

from pathlib import Path


def home_directory() -> str:
    """Return the user home directory as string."""
    home = str(Path.home())
    return home


if __name__ == "__main__":
    print(home_directory())
