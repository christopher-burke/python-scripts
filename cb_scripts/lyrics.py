#!/usr/bin/env python3

"""How does it go? - Lyrics scraper."""

import requests
from bs4 import BeautifulSoup


def main(artist: str, song: str):
    """Return the lyrics to the artist and song provided."""
    base_url = f'https://www.azlyrics.com/lyrics/{artist}/{song}.html'
    response = requests.get(f'{base_url}')
    soup = BeautifulSoup(response.text, "lxml")
    elements = soup.find_all(['a', 'b', 'h1', 'script',
                              'small', 'span', 'title']
                             )
    hidden = soup.select('.hidden')
    for text in [*hidden, *elements]:
        text.decompose()
    return soup.get_text(strip=True, separator=" ")


if __name__ == "__main__":
    artist = str(input("Artist: "))
    song = str(input("Song: "))
    song = song.replace(' ', '')

    lyrics = main(artist=artist.lower(), song=song.lower())

    print(lyrics)
