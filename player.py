import string_utils as su


class Player:
    def __init__(self, name):
        self.name = name
        self.tribe = ''
        self.growth = []
        self.data_size = 8
        self.defeated_ranking = []

    def get_player_data(self):
        return "Name:{0}, Tribe:{1}, Ranking:{2}\n".format(self.name, self.tribe, self.get_ranking_data())

    def set_player_tribe(self, tribe):
        self.tribe = tribe

    def set_ranking_data(self, data):
        for d in data:
            self.defeated_ranking.append(su.parse_data(d))

    def get_ranking_data(self):
        return self.defeated_ranking

    def print_all(self):
        print(self.name)
        for g in self.growth:
            print(g)

    def show_player_activity(self, show_only_inactive):
        inactive = 0
        for i in range(self.data_size):
            if su.parse_data(self.growth[i]) == 0:
                inactive += 1
        if show_only_inactive:
            if inactive > 0:
                return "\nPlayer " + self.name + " was inactive for " + str(inactive) + " days in a week"
            else:
                return ""
        else:
            if inactive > 0:
                return "\nPlayer " + self.name + " was inactive for " + str(inactive) + " days in a week"
            else:
                return "\nPlayer " + self.name + " is active"

    def get_growth(self):
        return self.growth

    def get_growth_by_index(self, ids):
        if ids < 0 or ids >= self.data_size:
            ids = max(0, min(ids, self.data_size))
        return self.growth[ids]

    def get_week_summary(self):
        return self.growth[self.data_size - 1]
