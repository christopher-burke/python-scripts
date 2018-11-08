#!/usr/bin/env python3

"""Convert CSV file to JSON file."""

import sys
import json
import csv


def make_json(in_file):
    """Read CSV file, create a JSON list."""
    with open(in_file, 'r') as infile:
        line = infile.readline()
        fieldnames = line.strip().split(',')
        reader = csv.DictReader(infile, fieldnames)
        return [json.dumps(row) for row in reader]


if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = sys.argv[1].split(".")[0] + '.json'
    with open(out_file, 'w') as outfile:
        outfile.write("[")
        outfile.write(",\n".join(make_json(in_file)))
        outfile.write("]")
