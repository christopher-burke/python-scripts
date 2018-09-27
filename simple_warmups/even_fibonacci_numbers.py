#!/usr/bin/env python3

"""Even Fibonacci Numbers.

Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.

source: https://projecteuler.net/problem=2
"""


UPPER_LIMIT = 4000000


def fibonacci_gen(n=1):
    """Fibonacci of a number using a generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a + b) * n


def main():
    """Sum all even fibonacci numbers less than limit."""
    even = []
    fib = fibonacci_gen()
    while True:
        n = next(fib)
        if n > UPPER_LIMIT:
            break
        if n % 2 == 0:
            even.append(n)
    print(sum(even))


if __name__ == "__main__":
    main()
