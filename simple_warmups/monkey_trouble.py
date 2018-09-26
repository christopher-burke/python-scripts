#!/usr/bin/env python3

"""monkey_trouble

We have two monkeys, a and b, and the parameters a_smile and b_smile 
indicate if each is smiling. We are in trouble if they are both smiling
 or if neither of them is smiling.  Return True if we are in trouble.


source: https://codingbat.com/prob/p120546
"""


def monkey_trouble(a_smile: bool, b_smile: bool) -> bool:
    """Monkey trouble.

    True if both values for a_simle and b_smile are the same.
    """
    return a_smile is b_smile


if __name__ == "__main__":
    print(monkey_trouble(True, True))
    print(monkey_trouble(False, False))
    print(monkey_trouble(True, False))
