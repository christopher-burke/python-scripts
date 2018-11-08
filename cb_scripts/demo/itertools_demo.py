#!/usr/bin/env python3

"""Itertools demo."""

from itertools import permutations, combinations, product, repeat


def p(iterable, length=2):
    """A Permutations wrapper function."""
    return permutations(iterable, r=length)


def c(iterable, length=2):
    """A Combinations wrapper function."""
    return combinations(iterable, r=length)


def prod(item, iterable, length=2):
    """A Product wrapper function."""
    return product([item], iterable)


def r(item, times=2):
    """A Repeat wrapper function."""
    return repeat(object=item, times=times)


if __name__ == "__main__":
    t = (1, 2, 3, 4, 5, 6,)
    print(t)
    print(list(p(t, 2)))
    print(list(c(t, 2)))
    print(list(prod(t[0], t, 2)))
    print(list(r(t, 10)))
