#!/usr/bin/env python3

"""Switch variable case.

A function that takes camel cased strings (i.e. ThisIsCamelCased),
and converts them to snake case (i.e. this_is_camel_cased).

"""

import re


def snake_case(input_str: str) -> str:
    """
    Turn camel case into snake case.

    :param input_str: String of variable.
    :return: Snake case string of input_str.
    """
    regex = r"([A-Z])"

    snake_case = input_str[0].lower()+re.sub(regex, r'_\1',
                                             input_str[1:]).lower()

    return f'{snake_case}'


if __name__ == "__main__":
    print(snake_case('ThisIsCamelCased'))
