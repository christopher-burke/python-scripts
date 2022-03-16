#!/usr/bin/env python3

"""Wordle word starter.

Wordle is a daily word game where players have six attempts to guess a 
five letter word. Feedback for each guess is given in the form of 
colored tiles to indicate if letters match the correct position.

URL: https://www.nytimes.com/games/wordle/index.html
"""

import json
from random import choice
from pathlib import Path
from typing import Iterable, List


def _load_wordle_list() -> List:
    """Load json word file to object."""
    base_dir = Path(__file__).resolve().parent
    with open(f'{base_dir}/data/json/wordle_list.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def _choose_random(iterable: Iterable) -> str:
    """Random choose from iterable."""
    return choice(iterable)


def main() -> str:
    """Select a random word from the wordle list."""
    words = _load_wordle_list()
    word = _choose_random(words)
    return word


if __name__ == "__main__":
    print(main())
