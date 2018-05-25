#!/usr/bin/env python3

"""Python Generator - Crawl Star Wars API (swapi.io).

Example using Python Generator to crawl an API and
display results to the terminal.
"""


import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)


def crawl(link):
    """Crawl generator for the swapi.io link.

    This crawler is set to find all characters in
    Revenge of the Sith (https://swapi.co/api/films/6/).
    """
    response = requests.get(link)
    results = json.loads(response.content)
    logging.info('results: %s', results)
    for character in results['results']:
        if 'https://swapi.co/api/films/6/' in character['films']:
            yield character['name']
    if 'next' in results and results['next'] is not None:
        next_page = crawl(results['next'])
        for page in next_page:
            yield page


if __name__ == "__main__":
    revenge_of_the_sith = crawl('https://swapi.co/api/people/')
    for x in revenge_of_the_sith:
        print(x)
