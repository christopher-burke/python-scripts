#!/usr/bin/env python3

"""Create Coffee-Repo Master list."""

import re
import os
from calendar import month_name
from pathlib import Path


# Set a environment variable to the coffee-repo directory path.
COFFEE_REPO_DIR = os.environ.get('COFFEE_REPO')

settings = {

    'LINKS_REGEX': r'\* \[.*\]\(.*\)',
    'archive-dir': f'{COFFEE_REPO_DIR}/archives',
    'master-dir': f'{COFFEE_REPO_DIR}/master',
}


def month_num(month):
    """Return the month number."""
    return list(month_name).index(month.strip())


def read_readme(filename):
    """Return contents of README.md."""
    with open(filename,
              'r',
              encoding='utf8') as f:
        readme = f.read()
    return readme


def write_master(filename, data):
    """Create Archive file."""
    with open(filename, 'w') as f:
        for line in data:
            f.write(f'{line}\n')


def parse_readme(readme_content):
    """Parse readme input(in) and return Month, Year and URLs."""
    # month_regex = settings['MONTHS_REGEX']
    # matches = re.search(month_regex, readme_content, re.I)

    links_regex = settings['LINKS_REGEX']
    urls = re.findall(links_regex, readme_content, re.I)
    return urls


def run():
    """Run the coffee-repo archive."""
    archive_full_path = f'{settings["archive-dir"]}'

    p = Path(archive_full_path)
    urls = ['## MASTER LIST ##']
    for path in p.iterdir():
        if path.is_dir():
            continue

        print(path)
        content = read_readme(path)
        urls += parse_readme(content)

    master_full_path = f'{settings["master-dir"]}/MASTER.md'
    write_master(master_full_path, list(urls))
    for url in list(urls):
        print(url)


def main():
    """Run the program."""
    run()


if __name__ == "__main__":
    main()
