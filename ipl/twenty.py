import collections
import re

from bs4 import BeautifulSoup

from ipl.base import web


def selection(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    strong_tags = soup.find_all("strong")

    players = []
    words = ['Fantasy Suggestion', 'Captain', 'Vice-Captain']

    for strong_tag in strong_tags:
        if any(word in strong_tag.text for word in words):
            team = cleanup(strong_tag.next_sibling)
            players += team.split(",")

    feq = collections.defaultdict(int)

    for player in players:
        feq[player] += 1

    return {k: v for k, v in sorted(feq.items(), key=lambda item: item[1], reverse=True)}


def cleanup(string):
    team = string.replace('and', ',')
    team = team.replace(u'\xa0', u'')
    return re.sub('[!@#$: ]', '', team)


def fantasy():
    playing_xi = web()
    playing_xi_url = playing_xi.find_fanatsy()

    if playing_xi_url:
        resp, status = playing_xi.read(playing_xi.base_url + playing_xi_url)
        if status:
            selection(resp)
        else:
            return 'Please check again later'
