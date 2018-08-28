#!/usr/bin/env python3


"""Count words and the three most common ones."""

import sys
from string import punctuation
from collections import Counter


def main(text: str) -> str:
    """Print the count and most common 3 words.

    All strings are converted to lowercase for counting.
    """
    table = str.maketrans({_: ' ' for _ in punctuation})
    text = text.translate(table)
    length = len(text.split())
    most_common = ", ".join([
                            f'{a[0]} {a[1]}'
                            for a in
                            Counter(
                                map(str.lower, text.split())
                            ).most_common(3)
                            ])
    return f'There are {length} words ({most_common}).'


if __name__ == "__main__":
    text_or_filepath = sys.argv[1]
    try:
        with open(text_or_filepath, 'r') as f:
            text = "".join(f.readlines())
    except (FileNotFoundError, NameError):
        print(sys.exc_info()[0])
        text = text_or_filepath

    output = main(text)
    print(output)
