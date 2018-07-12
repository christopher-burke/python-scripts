#!/usr/bin/env python3


"""Packt Free Learning book."""


import requests
from bs4 import BeautifulSoup


HEADERS = {'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'  # noqa E501
                         '(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}  # noqa E501


def book_details(url):
    """Get the image and title of book."""
    session = requests.Session()
    r = session.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, parser='html.parser')
    image = soup.findAll("img", {"class": 'bookimage'})[0]['src']
    title = soup.findAll("div", {"class": 'dotd-title'})[0].text.strip()
    return (image, title,)


def notify_ifttt(url):
    """Push notification of book title via IFTTT."""
    from ifttt.ifttt_event_trigger import post_ifttt
    img, title = book_details(url)
    post_ifttt(title)


if __name__ == "__main__":
    url = 'https://www.packtpub.com//packt/offers/free-learning'
    notify_ifttt(url)
