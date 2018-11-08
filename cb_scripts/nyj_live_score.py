#!/usr/bin/env python

"""Get the New York Jets schedule and scores of a season from NFL.com."""

from urllib.request import urlopen
from xml.etree import ElementTree


url_2 = 'http://www.nfl.com/ajax/scorestrip?season=%d&seasonType=REG&week=%d'


def main(year):
    """Return the Jets scores for a given year (season)."""
    for week in range(1, 18):
        url = f'http://www.nfl.com/ajax/scorestrip?season={year}&seasonType=REG&week={week}'
        results = urlopen(url)
        tree = ElementTree.parse(results)
        results.close()
        for node in tree.iter('g'):
            date = node.attrib.get('eid')
            weekday = node.attrib.get('d')
            time = node.attrib.get('t')
            home_team = node.attrib.get('h')
            visitor_team = node.attrib.get('v')
            home_score = node.attrib.get('hs')
            visitor_score = node.attrib.get('vs')
            if 'NYJ' in (visitor_team, home_team):
                print(
                    f'{home_team} '
                    f'{home_score} '
                    f'{visitor_team} '
                    f'{visitor_score} '
                    f'{weekday} '
                    f'{date[4:6]} '
                    f'{date[6:8]} '
                    f'{date[:4]} '
                    f'{time}'
                )


if __name__ == "__main__":
    main(2018)
