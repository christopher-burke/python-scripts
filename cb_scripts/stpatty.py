#!/usr/bin/env python3

"""St.Patrick's Day blessing."""

from pathlib import Path
from random import shuffle, choice


def choose_blessing() -> str:
    """Choose a blessing for St.Patrick's Day."""
    base_dir = Path(__file__).resolve().parent
    with open(f'{base_dir}/data/stpatty/blessings.txt', mode='r', encoding='utf-8') as bf:
        blessings = bf.readlines()
        shuffle(blessings)
    return f"☘️ {choice(blessings).strip()}☘️  Happy St.Patrick's Day"


def main():
    """Get a St. Patrick's Day blessing."""
    return choose_blessing()


if __name__ == "__main__":
    print(main())
