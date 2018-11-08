#!/usr/bin/env python3


"""YouTube utilities.

Using the YouTube URL:
* Get the YouTube Title
* Get the YouTube Shortened URL
"""

import sys
import re
import requests
from bs4 import BeautifulSoup


def video_id(url: str) -> str:
    """Return the YouTube Video Id from URL."""
    REGEX = '(?:https:\/\/www.youtube.com\/watch\?v=)([^&\n\r]*)'
    youtube_id = re.match(REGEX, url, re.I | re.M)
    try:
        return f'{youtube_id.group(1)}'
    except AttributeError:
        raise Exception('Not a valid YouTube url.')


def title(url: str) -> str:
    """Return the title of the YouTube video."""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find('title').text


def shorten_url(youtube_id: str) -> str:
    """Return the shortened url for YouTube video."""
    return f'https://youtu.be/{youtube_id}'


def markdown_list(url: str, title: str) -> str:
    """Return the Markdown list syntax for YouTube video."""
    return f'* [{title}]({url})'


def main(url: str) -> str:
    """Run the program."""
    try:
        youtube_id = video_id(url)
    except Exception as e:
        return e
    title_ = title(url)
    short_url = shorten_url(youtube_id)
    markdown = markdown_list(url=short_url, title=title_)
    return markdown


if __name__ == "__main__":
    used_shell = False
    try:
        url = sys.argv[1]
    except IndexError:
        from dev_utils import shell
        url = shell('pbpaste').decode("utf-8")
        used_shell = True

    output = main(url)

    if used_shell:
        url = shell(f'echo \'{output}\' | pbcopy').decode("utf-8")

    print(output)
