#!/usr/bin/env python3

"""Programming Quotes.

Grab the quotes from http://quotes.cat-v.org/programming/ and pick one
at random to display.
"""

import requests
import random
from bs4 import BeautifulSoup


def get_source(debug=False):
    """Get the source page of quotes from quotes.cat-v.org/programming.

    To limit network requests and read from a local file:
        1. Download html from site.
        2. Rename file 'programming_quotes.html' in same directory.
        3. Change debug arg to True.

    :return: String of HTML.
    """
    if debug:
        with open('programming_quotes.html', 'r') as fin:
            content = fin.read()
        return content
    return requests.get('http://quotes.cat-v.org/programming/').content


def find_all_quotes(html):
    """Find all the quotes, return a list of quotes."""
    soup = BeautifulSoup(html, 'html.parser')
    quotes = soup.find('div', attrs={'id': 'main-copy'})
    quotes_list = str(quotes).split('\n<hr/>\n')
    quotes_list[0] = quotes_list[0].partition('</h1>\n')[-1]
    return quotes_list


def get_random_quote(quotes_list):
    """Return a random quote to user."""
    upper_limit = len(quotes_list)-1
    select = random.randint(0, upper_limit)
    selected_quote = quotes_list[select]
    soup = BeautifulSoup(selected_quote, 'html.parser')
    return soup.text


def main():
    """Main."""
    html = get_source()
    quotes_list = find_all_quotes(html)
    random_quote = get_random_quote(quotes_list)
    return random_quote


if __name__ == "__main__":
    print(main())
