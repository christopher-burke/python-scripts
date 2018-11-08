#!/usr/bin/env python3

"""Look up the meaning of a word."""

import requests


def get_meaning(word):
    """Get the defintion from glosbe.com."""
    url = 'http://glosbe.com/gapi/' + \
        'translate?from=eng&dest=eng&' + \
        f'format=json&phrase={word}&pretty=true'
    r = requests.get(url)
    result = r.json()
    meaning = result['tuc'][0]['meanings'][0]["text"]
    return meaning


def main():
    """Get word from user and return the meaning."""
    word = input('Word search: ')
    meaning = get_meaning(word=word)
    return(f'{word}: {meaning}')


if __name__ == "__main__":
    print(main())
