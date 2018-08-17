#!/usr/bin/env python3

"""Flatten iterable."""

from itertools import chain


def flatten(iterable):
    """Flatten a nested iterable into chain object."""
    return chain(*iterable)


def flatten_as_list(iterable):
    """Flatten a nested iterable into a list."""
    return list(chain(*iterable))


def flatten_as_tuple(iterable):
    """Flatten a nested iterable into a list."""
    return tuple(chain(*iterable))


if __name__ == "__main__":
    sample = [[1, 2, 3], [4, 5, 6], [7]]
    assert list(flatten(sample)) == list(chain(*[[1, 2, 3], [4, 5, 6], [7]]))
    assert flatten_as_list(sample) == [1, 2, 3, 4, 5, 6, 7]
    assert flatten_as_tuple(sample) == (1, 2, 3, 4, 5, 6, 7,)
