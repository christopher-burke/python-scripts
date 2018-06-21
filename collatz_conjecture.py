#!/usr/bin/env python3


"""Collatz Conjecture."""

import sys


def handle_even(n: int):
    """If n is even, divide it by 2."""
    return n // 2


def handle_odd(n: int):
    """If n is odd, multiply it by 3 and add 1."""
    return ((n * 3) + 1)


def collatz_conjecture(n: int, step: int=0, verbose: bool=False):
    """Collatz Conjecture function.

    Start with a number n > 1.
    Find the number of steps it takes to reach one using the following process:
    * If n is even, divide it by 2.
    * If n is odd, multiply it by 3 and add 1.

    returns steps - number of steps.
    """
    if n == 1:
        return step
    step += 1

    if n % 2 == 0:
        new_n = handle_even(n)
    else:
        new_n = handle_odd(n)

    if verbose:
        print(f'{n} => {new_n}')

    return collatz_conjecture(new_n, step, verbose)


if __name__ == "__main__":
    if sys.argv[-1] in ('-v', '--verbose',):
        verbose = True
    else:
        verbose = False
    n = input("Enter a number greater than 1: ")
    print(collatz_conjecture(int(n), verbose=verbose))
