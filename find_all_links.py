#!/usr/bin/env python3


"""Find all links from url."""

import requests
import re
from dev_utils import shell


URL_REGEX = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


def get_url():
    """Get the URL from the clipboard or raw input."""
    url = None
    output = shell('pbpaste').decode("utf-8")
    try:
        url = re.findall(URL_REGEX, output, re.I)
    except TypeError as e:
        print("error caught")
    if url:
        return url[0]
    return input('What is the URL?: ')


def main():
    """Get the url page and find all the url links."""
    url = get_url()
    page = requests.get(url)
    html = page.text
    links = re.findall(URL_REGEX, html, re.I)
    for link in set(links):
        print(link)


if __name__ == "__main__":
    main()
