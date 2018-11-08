#!/usr/bin/env python3

"""Divisors: Find all the divisors of a number.

Also determine if a number is prime.
"""


def divisors(n: int):
    """Return list of divisors.

    Using list comprhension.
    n : int
    returns a list of divisor(s).
    """
    return [divisor for divisor in range(1, n+1) if n % divisor == 0]


def prime(n: int):
    """Determine if a number is prime.

    Prime numbers are divisible by 1 and itself.

    n: int
    returns True if prime and False if not prime.
    """
    return [1, n] == divisors(n)


if __name__ == "__main__":
    n = int(input("Choose a number to find all divisors: "))
    print(divisors(n),)

    if prime(n):
        prime_ = ""
    else:
        prime_ = "not"

    print(f"{n} is {prime_} a prime number.")
