class Village:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.cords = '000|000'
        self.ai = False
        self.owner = ''
        self.owner_tribe = ''
        self.previous_owner = ''
        self.previous_owner_tribe = ''
        self.conqueror_time = ''

    def get_data(self):
        n = "Name: " + self.name
        p = " Points: " + str(self.points)
        c = " Cords: " + self.cords
        o = " Owner: "+self.owner
        ot = " Tribe: "+self.owner_tribe
        po = " Previous owner: "+self.previous_owner
        pot = " Previous tribe"+self.previous_owner_tribe
        ct = " Conquerors time: "+self.conqueror_time + '\n'
        return n + p + c + o + ot + po + pot + ct
