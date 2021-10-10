from requests import get
from bs4 import BeautifulSoup

from player import Player
from village import Village

Players = []


def show_active_tribe(world_number):
    wn_url = 'https://pl.twstats.com/pl' + world_number + '/index.php?page=rankings&mode=tribes'
    wn_page = get(wn_url)
    if wn_page.status_code >= 400:
        return 'HTML Error cannot find specyfic world number\n' \
               'Ensure you enter correct world number'
    wn_response = BeautifulSoup(wn_page.content, 'html.parser')
    res = wn_response.find_all('table', class_='widget')
    if len(res) == 0:
        return 'HTML Error cannot find specyfic world number\n' \
               'Ensure you enter correct world number'
    tribes = wn_response.find_all('table', class_='widget')[0]
    text = ''
    for tr in tribes.find_all('tr'):
        for idx in tr.find_all('a'):
            link = idx['href']
            if idx.parent.parent.find('td', class_='foot'):
                continue
            offset = link.rfind('=')
            tribe_id = link[offset + 1:len(link)]
            name = idx.get_text()
            text = text + name + ':' + tribe_id + '\n'
            print(name + ':' + tribe_id)
    return text


def show_inactive_members(world_number, tribe_id, show_inact):
    Players.clear()
    wn = world_number
    show_active_tribe(wn)
    idp = tribe_id
    only_inactive = show_inact
    tribe_url = 'https://pl.twstats.com/pl' + wn + '/index.php?page=tribe&mode=members&id=' + idp
    page = get(tribe_url)

    response = BeautifulSoup(page.content, 'html.parser')
    value = response.find('table', class_='widget')
    try:
        value.find_all('tr')
    except AttributeError:
        return "HTML error - cannot find any data"
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
    PlayersData = ''
    for i in range(idx):
        PlayersData += Players[i].show_player_activity(only_inactive)
    return PlayersData.strip()


def show_rank_stats(wn, idp):
    Players.clear()
    rank_url = 'https://pl.twstats.com/pl' + wn + '/index.php?page=rankings&mode=playersod&tribe=' + idp
    rank_page = get(rank_url)

    rank_bs = BeautifulSoup(rank_page.content, 'html.parser')
    rank_response = rank_bs.find('table', class_='widget')
    PlayersData = ''
    k = 0

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
                        PlayersData += pl.get_player_data()
                        k += 1
    return PlayersData


def try_get_text(text):
    try:
        text.get_text()
        return True
    except AttributeError:
        return False


def find_enemy_conquerors(world_number, conquerors_count):
    conquerors_count = max(min(int(conquerors_count), 400), 0)
    temp_count = 0
    page_number = 0
    conquerors_url = 'https://pl.twstats.com/pl' + world_number + '/index.php?page=ennoblements&live=live'
    page = get(conquerors_url)

    response = BeautifulSoup(page.content, 'html.parser')
    conquerors_response = response.find('table', class_='widget')

    villages = []
    break_condition = False
    text_data = ''
    while not break_condition:
        if page_number == 0:
            temporary_tr = conquerors_response.find_all('tr')
        else:
            next_conquerors_url = 'https://pl.twstats.com/pl' + world_number + '/index.php?page=ennoblements&pn=' + str(
                page_number) + '&k=-1&maxpoints=0&minpoints=0&filtertribe=0'
            next_page = get(next_conquerors_url)
            next_response = BeautifulSoup(next_page.content, 'html.parser')
            next_conc_response = next_response.find('table', class_='widget')
            while next_conc_response.find_parent('form') is not None:
                next_conc_response = next_conc_response.find_next('table', class_='widget')
            temporary_tr = next_conc_response.find_all('tr')
        i = 0
        for tr in temporary_tr:
            td = tr.find_all('td')
            i += 1
            for idx in range(len(td)):
                if idx == 0:
                    village_offset = td[idx].get_text().rfind('(') + 1
                    name = td[idx].get_text()[0:village_offset - 1]
                    coord = td[idx].get_text()[village_offset:village_offset + 7]
                    v = Village(name)
                    villages.append(v)
                    v.cords = coord
                elif idx == 1:
                    points = td[idx].get_text().replace(',', '')
                    v.points = points
                elif idx == 2:
                    length = len(td[idx].find_all('a'))
                    if length == 0:
                        name = td[idx].get_text()
                        v.ai = True
                        v.previous_owner = name
                    else:
                        if length == 1:
                            name = td[idx].find('a').get_text()
                            v.previous_owner = name
                        else:
                            name = td[idx].find('a').get_text()
                            tribe = td[idx].find('a', class_='tribelink').get_text()
                            v.previous_owner = name
                            v.previous_owner_tribe = tribe
                elif idx == 3:
                    length = len(td[idx].find_all('a'))
                    if length == 0:
                        return "HTML error\nWorld is probably closed"
                    elif length == 1:
                        name = td[idx].find('a').get_text()
                        v.owner = name
                    else:
                        name = td[idx].find('a').get_text()
                        tribe = td[idx].find('a', class_='tribelink').get_text()
                        v.owner = name
                        v.owner_tribe = tribe
                else:
                    date = td[4].get_text()
                    v.conqueror_time = date
                    text_data += v.get_data()
            if temp_count == conquerors_count:
                return text_data.strip()
            if i != len(temporary_tr):
                temp_count += 1
        page_number += 1
