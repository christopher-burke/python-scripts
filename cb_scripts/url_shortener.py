#!/usr/bin/env python3

"""Shorten URLs using TinyURL."""

import requests


def get_tinyurl(url):
    """Create and return the tinyURL."""
    tiny_url_api = f'http://tinyurl.com/api-create.php?url={url}'
    response = requests.get(tiny_url_api)
    return response.text


def main(url):
    """Return the tinyURL."""
    return get_tinyurl(url)


if __name__ == "__main__":
    # Test using url='http://www.github.com'
    print(main(url='http://www.github.com'))
