#!/usr/bin/env python3

"""Unlock code.

Simulate the an unlock passcode feature.

Pick four (4) random numbers (0 to 9), display the numbers spelled out.
Allow the user to input the passcode with digits then check if the
digit input matches. On failure, repeat till the correct digits are
entered. Program terminates after correct sequence is entered.
"""

import random
from itertools import islice

NUMBERS = (
    (9, 'nine',),
    (8, 'eight',),
    (7, 'seven',),
    (6, 'six',),
    (5, 'five',),
    (4, 'four',),
    (3, 'three',),
    (2, 'two',),
    (1, 'one',),
    (0, 'zero',),
)

OUTPUTS = {
    'Success': 'Passcode accepted.',
    'Failure': 'Passcode invalid',
    'InputErr': 'Enter passcode in `1 2 3 4` format.',

}


def dialog_output(label: str):
    """Display output to the user."""
    print(OUTPUTS[label])


def user_input(passcode: str) -> str:
    """Get the passcode from the user."""
    code = input(f"Type the numerical value of the passcode `{passcode}`: ")
    return code


def pick_random_number() -> tuple:
    """Generator for picking random numbers."""
    while True:
        yield random.choice(NUMBERS)


def generate_passcode(n: int = 4) -> tuple:
    """Create a passcode of length n."""
    passcode = tuple(islice(pick_random_number(), n))
    return passcode


def check(entered_code: iter, passcode: tuple) -> bool:
    """Check the entered code with the generated passcode."""
    for i in zip(entered_code, [x[0] for x in passcode]):
        if int(i[0]) != i[1]:
            dialog_output('Failure')
            return False
    return True


def main():
    """Unlock program main function."""
    passcode = generate_passcode()
    valid = False
    while not valid:
        entered_code = user_input(", ".join([x[1].upper() for x in passcode]))
        if len(entered_code) > 4:
            entered_code = entered_code.split(' ')
        else:
            entered_code = list(islice(entered_code, 4))
        if len(entered_code) < 4:
            valid = False
            dialog_output('InputErr')
        else:
            valid = check(entered_code, passcode)
    dialog_output('Success')


if __name__ == "__main__":
    main()
