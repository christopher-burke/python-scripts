#!/usr/bin/env python3

"""Archive Coffee-Repo list in README.md."""

import re
import os
from calendar import month_name

# Set a environment variable to the coffee-repo directory path.
COFFEE_REPO_DIR = os.environ.get('COFFEE_REPO')

settings = {
    'months': "|".join([month for month in list(month_name) if month]),
    'LINKS_REGEX': r'\* \[.*\)',
    'README.md': f'{COFFEE_REPO_DIR}/README.md',
    'archive-dir': f'{COFFEE_REPO_DIR}/archives',
}

settings['MONTHS_REGEX'] = f'###\s+({settings["months"]})(.*)'


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


def write_archive(filename, data):
    """Create Archive file."""
    with open(filename, 'w') as f:
        for line in data:
            f.write(f'{line}\n')


def parse_readme(readme_content):
    """Parse readme input(in) and return Month, Year and URLs."""
    month_regex = settings['MONTHS_REGEX']
    links_regex = settings['LINKS_REGEX']

    matches = re.search(month_regex, readme_content, re.I)
    urls = re.findall(links_regex, readme_content, re.I)

    month = matches.group(1)
    year = matches.group(2)
    return (month, year, urls,)


def run():
    """Run the coffee-repo archive."""
    readme_content = read_readme(settings['README.md'])
    month, year, urls = parse_readme(readme_content)
    month_index = month_num(month)

    archive_filename = f'{year.strip()}-{month_index:0>2d}.md'
    archive_full_path = f'{settings["archive-dir"]}/{archive_filename}'
    archive_content = list([f'## {month}{year} ##\n', *urls])
    write_archive(archive_full_path, archive_content)


def main():
    """Run the program."""
    run()


if __name__ == "__main__":
    main()
