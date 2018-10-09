#!/usr/bin/env python3

"""Sum square difference.

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.

source: https://projecteuler.net/problem=6
"""


def main():
    """Difference between the sum of the squares and the square of the sum.

    Find the difference between the sum of the squares of the
    first one hundred natural numbers and the square of the sum.
    """
    sum_of_squares = sum([x**2 for x in range(1, 101)])
    square_sum = sum(range(1, 101))**2
    return square_sum - sum_of_squares


if __name__ == "__main__":
    main()
