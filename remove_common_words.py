#!/usr/bin/env python3


"""Remove common words from text.

Requires requests, nltk, and BeautifulSoup:

    `pip install nltk requests beautifulsoup4`
"""

import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from collections import Counter
import string
import re

from pprint import pprint


def get_url_text(url, selector):
    """Use requests and get HTML for a page."""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.select(f'{selector}')[0].text


def remove_common_words(text):
    """Remove common words from text.

    This function will remove punctuations and HTML tags.

    :return: String with common words removed.
    """
    punctuations = string.punctuation
    punctuations = r"[{}]".format(punctuations)

    text = re.sub(punctuations, '', text)
    text = re.sub('<[^>]*>', '', text)
    return text


def main():
    """Run remove common words."""
    # Place text into text object.

    url = 'URL'
    selector = 'SELECTOR'

    if url != 'URL':
        text = get_url_text(url=url,
                            selector=selector
                            )  # """TEXT INPUT"""
    else:
        print('No url provided. Using sample text.')
        text = 'Need URL provided or text set.'

    s = set(stopwords.words('english'))
    text = remove_common_words(text)

    pprint(
        Counter(list(filter(lambda w:  w.lower() not in s, text.split()))
                ).most_common(20))


if __name__ == "__main__":
    main()
