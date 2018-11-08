#!/usr/bin/env python3

"""Fake text generator.


Requires:
Faker

pip install Faker
"""

from faker import Faker
from functools import partial


def fake_text(length: int) -> str:

    fake = Faker()
    return fake.text(length)


five_hundred = partial(fake_text, length=500)
one_thousand = partial(fake_text, length=1000)


def main():
    print(five_hundred())
    print('-'*10)
    print(one_thousand())


if __name__ == "__main__":
    main()
