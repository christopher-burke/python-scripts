#!/usr/bin/env python3

"""Sieve of Eratosthenes.


From wikipedia (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes):

To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
2. Initially, let p equal 2, the smallest prime number.
3. Enumerate the multiples of p by counting to n from 2p in increments of p, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
"""


class SieveOfEratosthenes:
    """Sieve of Eratosthenes."""

    def __init__(self, limit: int):
        """Create the SieveOfEratosthenes object."""
        self.limit = limit
        self.marked = set()
        self.primes = set()

    def prime(self, p: int):
        """Mark number prime."""
        if p not in self.marked:
            self.primes.add(p)

    def mark(self, pn: int):
        """Mark number."""
        if pn < self.limit:
            self.marked.add(pn)

    def __repr__(self):
        """Return the SieveOfEratosthenes magic __repr__."""
        return f'SieveOfEratosthenes(limit={self.limit})'


def main():
    """Run the program."""
    limit = 10000000
    se = SieveOfEratosthenes(limit)
    for p in range(2, limit):
        se.prime(p)
        pn = 2 * p
        while pn < limit:
            se.mark(pn)
            pn += p

    print(sorted(se.marked, key=lambda x: int(x)))
    print(sorted(se.primes, key=lambda x: int(x)))


if __name__ == "__main__":
    main()
