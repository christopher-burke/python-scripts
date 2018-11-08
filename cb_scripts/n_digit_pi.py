#!/usr/bin/env python3


"""Find Pi to the nth digit.

Find PI to the Nth Digit - Enter a number
and have the program generate PI up to
that many decimal places.

Keep a limit to how far the program will go.

Pi = SUM k=0 to infinity 16^-k [ 4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6) ]
"""


from functools import reduce
from math import pow
from operator import add
from decimal import Decimal, getcontext


def compute_pi(max: int=2000):
    """Calulate pi using Bailey–Borwein–Plouffe formula (BBP formula)."""
    getcontext().prec = 500
    pi = Decimal(0)
    vals = []
    for k in range(max):
        vals.append(Decimal(pow(16, -k)) *  # 1/16^k
                    (Decimal(4/(8*k+1)) -  # 4/8k+1
                     Decimal(2/(8*k+4)) -  # 2/8k+4
                     Decimal(1/(8*k+5)) -  # 1/8k+5
                     Decimal(1/(8*k+6))  # 1/8k+6
                     ))
    pi = reduce(add, vals)  # Sum of vals = pi up to k
    return pi


def main() -> str:
    """Find the nth digit of pi."""
    max = int(input("Enter the number of decmial places for pi:  "))
    pi = compute_pi(max)
    n_digits = str(pi).partition('.')[-1][:max]
    return f'3.{n_digits}'


if __name__ == "__main__":
    print(main())
