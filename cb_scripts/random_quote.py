#!/usr/bin/env python3

"""Random Quote: Pick a Quote at random from a text file.

Text file of quotes are separated by a blank new line ("\n").
"""

import random


def load_quotes(quotes_file) -> tuple:
    """Load quotes from file, return tuple of quotes."""
    with open(quotes_file, 'r') as f:
        build_quote = []
        quotes = []
        for line in f:
            if line.isspace():
                quotes.append(''.join(build_quote).strip())
                build_quote = []
            build_quote.append(line.replace("\n", "").strip() + " ")
    return tuple(quotes)


def main() -> str:
    """Return a random quote."""
    try:
        quotes = load_quotes(
            quotes_file='')
    except FileNotFoundError:
        return "".join(['File Not Found: '
                        'Check `quotes_file` path in script.\n',
                        ])
    return random.sample(quotes, 1)[0]


if __name__ == "__main__":
    print(main())
