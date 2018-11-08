#!/usr/bin/env python3

"""Fibonacci."""


from functools import lru_cache
import timeit

from datetime import datetime as dt


@lru_cache(maxsize=1000)
def fibonacci(x):
    """Fibonacci of a number."""
    # Type Error
    if type(x) != int:
        raise TypeError("x is not a positive integer.")
    # Value Error
    if x < 0:
        raise ValueError("x is not a positive integer.")
    if x < 3:
        #  fibonacci(0) = 0,  fibonacci(1) = 1,  fibonacci(2) = 1
        return (0, 1, 1)[x]
    else:
        #  fibonacci(n) =  fibonacci(n-1) +  fibonacci(n-2)
        return fibonacci(x - 1) + fibonacci(x - 2)


def fibonacci_gen(n=1):
    """Fibonacci of a number using a generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a + b) * n


if __name__ == "__main__":
    start1 = dt.now()
    for x in range(1, 1000):
        print(fibonacci(x))
    end1 = dt.now()

    start2 = dt.now()
    fg = fibonacci_gen()
    for x in range(1, 1000):
        print(next(fg))
    end2 = dt.now()

    print(end1 - start1)
    print(end2 - start2)

    mysetup = """
    x = 1000
    def fibonacci(x):
        # Type Error
        if type(x) != int:
            raise TypeError("x is not a positive integer.")
        # Value Error
        if x < 0:
            raise ValueError("x is not a positive integer.")
        if x < 3:
            #  fibonacci(0) = 0,  fibonacci(1) = 1,  fibonacci(2) = 1
            return (0, 1, 1)[x]
        else:
            #  fibonacci(n) =  fibonacci(n-1) +  fibonacci(n-2)
            return fibonacci(x - 1) + fibonacci(x - 2)
    """

    mycode = """
    for x in range(1, 1000):
        print(fibonacci(x))
    """

    print(timeit.timeit(fibonacci_gen, number=1000))
