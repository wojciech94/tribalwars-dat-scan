from typing import List, Any

from requests import get
from bs4 import BeautifulSoup

from player import Player
from village import Village

Players = []


def show_active_tribe(world_number):
    wn_url = 'https://pl.twstats.com/pl' + world_number + '/index.php'
    wn_page = get(wn_url)

    wn_response = BeautifulSoup(wn_page.content, 'html.parser')
    tribes = wn_response.find_all('table', class_='widget')[1]
    for tr in tribes.find_all('tr'):
        for idx in tr.find_all('a'):
            link = idx['href']
            if idx.parent.parent.find('td', class_='foot'):
                continue
            offset = link.rfind('=')
            tribe_id = link[offset + 1:len(link)]
            name = idx.get_text()
            print(name + ':' + tribe_id)


def show_inactive_members():
    wn = str(input("Enter word number to analize\n"))
    show_active_tribe(wn)
    idp = str(input("Enter tribe id\n"))
    tribe_url = 'https://pl.twstats.com/pl' + wn + '/index.php?page=tribe&mode=members&id=' + idp
    page = get(tribe_url)

    response = BeautifulSoup(page.content, 'html.parser')
    value = response.find('table', class_='widget')
    names = []
    idx = -1
    span_offset = 0
    for v in value.find_all('tr'):
        trr = v.find_all('td')
        for t in trr:
            try:
                n = t.find('a').get_text()
                if n not in names:
                    idx += 1
                    span_offset = 0
                    pl = Player(n)
                    Players.append(pl)
                    names.append(n)
                for sp in t.find_all('span'):
                    Players[idx].growth.append(sp.get_text())
                    span_offset += 1
            except AttributeError:
                pass
    for i in range(idx):
        Players[i].show_player_activity(True)


def show_rank_stats():
    rank_url = 'https://pl.twstats.com/pl157/index.php?page=rankings&mode=playersod&tribe=572'
    rank_page = get(rank_url)

    rank_bs = BeautifulSoup(rank_page.content, 'html.parser')
    rank_response = rank_bs.find('table', class_='widget')

    for tr in rank_response.find_all('tr'):
        td = tr.find_all('td')
        data = []
        for ids in range(len(td)):
            tt = td[ids]
            if try_get_text(tt):
                if ids == 0:
                    pl = Player(tt.get_text())
                    Players.append(pl)
                elif ids == 1:
                    pl.set_player_tribe(tt.get_text())
                else:
                    data.append(tt.get_text())
                    if ids == len(td) - 1:
                        pl.set_ranking_data(data)


def try_get_text(text):
    try:
        txt = text.get_text()
        return True
    except AttributeError:
        return False


def find_enemy_conquerors():
    conquerors_url = 'https://pl.twstats.com/pl157/index.php?page=ennoblements&live=live'
    page = get(conquerors_url)

    response = BeautifulSoup(page.content, 'html.parser')
    conquerors_response = response.find('table', class_='widget')

    for tr in conquerors_response.find_all('tr'):
        td = tr.find_all('td')
        villages = []
        for idx in range(len(td)):
            if idx == 0:
                village_offset = td[idx].get_text().rfind('(') + 1
                name = td[idx].get_text()[0:village_offset - 1]
                coord = td[idx].get_text()[village_offset:village_offset + 7]
                v = Village(name)
                villages.append(v)
                v.cords = coord
                print("Village Name: " + v.name)
                print("Village Cords: " + coord)
            elif idx == 1:
                points = td[idx].get_text().replace(',', '')
                v.points = points
                print("Points: " + v.points)
            elif idx == 2:
                length = len(td[idx].find_all('a'))
                if length == 0:
                    name = td[idx].get_text()
                    v.ai = True
                    v.previous_owner = name
                    print("AI: " + name)
                else:
                    if length == 1:
                        name = td[idx].find('a').get_text()
                        v.previous_owner = name
                        print("Player: " + name)
                    else:
                        name = td[idx].find('a').get_text()
                        tribe = td[idx].find('a', class_='tribelink').get_text()
                        v.previous_owner = name
                        v.previous_owner_tribe = tribe
                        print("Player: " + name)
                        print("Tribe: " + tribe)
            elif idx == 3:
                length = len(td[idx].find_all('a'))
                if length == 1:
                    name = td[idx].find('a').get_text()
                    v.owner = name
                    print("Player: " + name)
                else:
                    name = td[idx].find('a').get_text()
                    tribe = td[idx].find('a', class_='tribelink').get_text()
                    v.owner = name
                    v.owner_tribe = tribe
                    print("Player: " + name)
                    print("Tribe " + tribe)
            else:
                date = td[4].get_text()
                v.conqueror_time = date
                print("Conqueror date: " + date + '\n')


if __name__ == '__main__':
    show_inactive_members()
    show_rank_stats()
    find_enemy_conquerors()