#!/usr/bin/env python3


"""Random Name - Generate a random name."""

import json
from random import choice
from collections import OrderedDict


def main():
    """Generate a random name from json files."""
    files_ = ('json/first_names.json', 'json/last_names.json',)
    data = OrderedDict()
    for file_ in files_:
        with open(file_, 'r') as fin:
            data[file_.partition('.')[0]] = json.load(fin)
    return(" ".join([choice(data[key]).title() for key in data]))


if __name__ == "__main__":
    print(main())
