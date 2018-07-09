#!/usr/bin/env python3

"""Sieve of Eratosthenes.

To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
2. Initially, let p equal 2, the smallest prime number.
3. Enumerate the multiples of p by counting to n from 2p in increments of p, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
"""


class SieveOfEratosthenes:

    def __init__(self, limit: int):
        self.limit = limit
        self.marked = set()
        self.primes = set()

    def prime(self, p):
        if p not in self.marked:
            self.primes.add(p)

    def mark(self, pn: int):
        if pn < self.limit:
            self.marked.add(pn)



def main():
    limit = 121 # 10000000
    se = SieveOfEratosthenes(limit)
    for p in range(2, limit):
        se.prime(p)
        pn = 2 * p
        while pn < limit:
            se.mark(pn)
            pn += p

    print(se.marked)
    print(se.primes)


if __name__ == "__main__":
    main()
