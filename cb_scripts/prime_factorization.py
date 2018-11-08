#!/usr/bin/env python3


"""Prime Factorization.

User enter a number and find all Prime Factors (if there are any) and display them.
"""

from next_prime_number import prime


def prime_factorization(number: int):
    """Return set of prime factors."""
    p = number // 2
    s = set()
    for n in range(1, p+1):
        if number % n == 0 and prime(n):
            s = s | {n}
    return s


def main():
    """Return string of prime factors."""
    number = input("Enter a number: ")
    number = int(number)
    if prime(number):
        return f'{number} is prime.'

    prime_factors = prime_factorization(number)
    if len(prime_factors) > 1:
        plural = 's are'
    else:
        plural = ' is'
    return f'{number} prime factor{plural} {sorted(prime_factors)}.'


if __name__ == "__main__":
    print(main())
