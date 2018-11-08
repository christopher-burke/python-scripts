#!/usr/bin/env python3

"""Crawler.

Crawl a url for all links and email addresses.
"""

import requests
import re


email_regex = r'([\w]+[\.\-\+]*)+\@\w+\.\w+'
http_link_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a\
-fA-F][0-9a-fA-F]))+'


def main():
    """The Main loop for crawler."""
    raise NotImplementedError("Working on script...")


if __name__ == "__main__":
    main()
