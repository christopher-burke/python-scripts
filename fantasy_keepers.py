"""Get Fantasy Baseball Keepers from years past."""

from os import environ
from collections import namedtuple
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from time import sleep

DRAFTRESULTS_BASE_URL = "https://baseball.fantasysports.yahoo.com/archive/mlb/{0}/{1}/draftresults?drafttab=team"

username = environ.get('FANTASY_USERNAME')
password = environ.get('FANTASY_PASSWORD')

YearLeagueId = namedtuple('YearLeagueId', ['year', 'league_id'])
Keeper = namedtuple('Keeper', ['last_name',
                               'first_name',
                               'team',
                               'position'
                               ])
# Create your seasons here
year_leagueid = ((2017, 1),
                 (2016, 2),)


seasons = map(lambda x: YearLeagueId(x[0], x[1]), year_leagueid)


def keeper(first_name, last_name, _x, team, _y, position):
    """Create Keeper namedtuple."""
    return Keeper(last_name, first_name, team, position)


delay = 0.5
opts = Options()
browser = Firefox(options=opts)
for season in seasons:
    draft_results_url = DRAFTRESULTS_BASE_URL.format(*season)
    browser.get(draft_results_url)

    # Handle Login
    # Username
    if browser.current_url != draft_results_url:
        sleep(delay)
        logintxt = browser.find_element_by_name("username")
        logintxt.send_keys(username)
        button = browser.find_element_by_id("login-signin")
        button.click()

    # Password
    if browser.current_url != draft_results_url:
        sleep(delay)
        logintxt = browser.find_element_by_name("password")
        logintxt.send_keys(password)
        button = browser.find_element_by_id("login-signin")
        button.click()

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    keepers = soup.select('span[title="This player is a keeper."]')
    keepers = [player.findParent() for player in keepers]
    for k in keepers:
        print(k.text.split())

    x = input("Continue?: ")
    if x == 'n':
        break
