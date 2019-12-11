#!/usr/bin/env python3

"""Replace all code letters with X.

From ITT 2016 - Kevlin Henney - Seven Ineffective
Coding Habits of Many Programmers (https://youtu.be/ZsHMHukIlJY?t=1260),
Code samples are shown and then replaced with all X's
to show identation and alignement.

This script removes all punctuations and replaces
all characteters with X's.
"""

import re
import sys
import string

punctuations = string.punctuation
punctuations = r"[{}]".format(punctuations)

PATTERNS_REPLACEMENTS = ((r'\w', 'X',), (punctuations, '',),)


def read_text():
    """Read file, if no file provided, use a sample."""
    try:
        file_ = sys.argv[1]
        with open(file_, 'r') as f:
            text = f.read()
    except IndexError:
        text = """lambda x: x+1"""
    return text


def replacer(pattern, replace, text):
    """Substitution wrapper from the re module."""
    return re.sub(pattern, replace, text)


def main():
    """Replace input with X's."""
    text = read_text()
    new_text = text
    for pattern, replace in PATTERNS_REPLACEMENTS:
        new_text = replacer(pattern, replace, new_text)
    return (new_text, text)


if __name__ == "__main__":
    print(main()[0])
