class Vegetation:
    def __init__(self, x, y, emoji):
        self.x = x
        self.y = y
        self.life_force = 1
        self.emoji = emoji

    @property
    def coord(self):
        return self.x, self.y


class Grass(Vegetation):
    count = 0

    def __init__(self, x, y):
        Vegetation.__init__(self, x, y, emoji="🌱")
        Grass.count += 1

    def __del__(self):
        Grass.count -= 1
