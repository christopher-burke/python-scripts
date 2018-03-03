"""Get Fantasy Baseball Keepers from years past."""

from os import environ
from collections import namedtuple, Counter, defaultdict
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep

DRAFTRESULTS_BASE_URL = "https://baseball.fantasysports.yahoo.com/archive/mlb/{0}/{1}/draftresults?drafttab=team"

username = environ.get('FANTASY_USERNAME')
password = environ.get('FANTASY_PASSWORD')

YearLeagueId = namedtuple('YearLeagueId', ['year',
                                           'league_id',
                                           'draft_years'])

Keeper = namedtuple('Keeper', ['id',
                               'last_name',
                               'first_name',
                               'team_postion',
                               ])
# Create your seasons here
year_leagueid = ((2015, 111111111), (2016, 111111111), (2017, 111111111), (2018, 111111111),
                 )

seasons = map(lambda x: YearLeagueId(x[0], x[1], (x[0]-1, x[0]-2,)), year_leagueid)


def strip(txt: str):
    return txt.strip()


def keeper(tag):
    """Create Keeper namedtuple."""

    player_id = tag.parent.a['href'].split('/')[-1]
    name, team_postion = tag.parent.text.split('\ue03e')
    last_name = strip(name.split()[-1])
    first_name = strip(" ".join(name.split()[:-1]))
    print(player_id, last_name, first_name, team_postion)
    return Keeper(player_id, last_name, first_name, strip(team_postion))


def get_player_id(tag):
    return tag.parent.a['href'].split('/')[-1]


def get_player_name(tag):
    print(tag.parent)
    print(tag.parent.text.split('\ue03e'))
    return map(strip, tag.parent.text.split('\ue03e'))


keepers = {}
cal_eligibility = defaultdict(Counter)
final = {}

delay = 3
opts = Options()
browser = Firefox(options=opts)
link = True
for season in seasons:
    draft_results_url = DRAFTRESULTS_BASE_URL.format(*season)
    browser.get(draft_results_url)
    while link:
        sleep(delay)
        current_url = browser.current_url.split('&')[0]
        link = current_url != draft_results_url
        try:
            username_login_box = browser.find_element_by_name("username")
            username_login_box.send_keys(username)
        except NoSuchElementException:
            print('No username element')  # log

        try:
            password_login_box = browser.find_element_by_name("password")
            password_login_box.send_keys(password)
        except NoSuchElementException:
            print('No password element')  # log

        try:
            button = browser.find_element_by_id("login-signin")
            button.click()
        except NoSuchElementException:
            print('No button element')
            browser.get(draft_results_url)
            sleep(delay)
            break

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    players = soup.select('span[title="This player is a keeper."]')
    players = [keeper(player)
               for player in players]

    keepers[season.year] = players
    if set(season.draft_years) <= keepers.keys():
        for y in season.draft_years:
            cal_eligibility[season.year] += Counter(keepers[y])
        eligibility = defaultdict(list)
        for k, v in cal_eligibility[season.year].items():
            eligibility[v].append(k)
        final[season.year] = eligibility
browser.close()
