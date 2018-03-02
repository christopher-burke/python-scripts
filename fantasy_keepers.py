"""Get Fantasy Baseball Keepers from years past."""


from collections import namedtuple
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from time import sleep

DRAFTRESULTS_BASE_URL = "https://baseball.fantasysports.yahoo.com/archive/mlb/{0}/{1}/draftresults?drafttab=team"

username = ''
password = ''

YearLeagueId = namedtuple('YearLeagueId', ['year', 'league_id'])
Keeper = namedtuple('Keeper', ['last_name',
                               'first_name',
                               'team',
                               'position'
                               ])
# Create your seasons here
seasons = [
    # YearLeagueId(2018, 64152),
    YearLeagueId(2017, 1),
    YearLeagueId(2016, 2),
]


def keeper(first_name, last_name, _x, team, _y, position):
    """Create Keeper namedtuple."""
    return Keeper(last_name, first_name, team, position)


delay = 0.5
opts = Options()
browser = Firefox(options=opts)
for x in seasons:
    draft_results = DRAFTRESULTS_BASE_URL.format(*x)
    browser.get(draft_results)

    # Handle Login
    if browser.current_url != draft_results:
        sleep(delay)
        logintxt = browser.find_element_by_name("username")
        logintxt.send_keys(username)
        button = browser.find_element_by_id("login-signin")
        button.click()

    if browser.current_url != draft_results:
        sleep(delay)
        logintxt = browser.find_element_by_name("password")
        logintxt.send_keys(password)
        button = browser.find_element_by_id("login-signin")
        button.click()

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    keepers = soup.select('span[title="This player is a keeper."]')
    players = [player.findParent() for player in keepers]

    # movie_player = browser.find_element_by_id('')
    x = input("Continue?: ")
    if x == 'n':
        break
