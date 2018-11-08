#!/usr/bin/env python3

"""Fake Names and addresses.

Using Faker, generate fake names and addresses.

Requires Faker:
`pip install Faker`
"""

from faker import Factory
from itertools import islice


def name():
    """Fake name generator."""
    fake = Factory().create('en_US')
    while True:
        yield (fake.name(), fake.address(),)


def main():
    """Generate 10 Fake name and address tuples."""
    names = list(islice(name(), 10))
    for fake_name in names:
        print(fake_name)
    return names


if __name__ == "__main__":
    main()
