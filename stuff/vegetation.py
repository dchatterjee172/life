class Vegetation:
    def __init__(self, x, y, emoji):
        self.x = x
        self.y = y
        self.life_force = 10
        self.emoji = emoji

    @property
    def coord(self):
        return self.x, self.y

    def move(self):
        self.life_force = 0.9 * self.life_force

    def eaten(self):
        self.life_force = 0


class Grass(Vegetation):
    count = 0

    def __init__(self, x, y):
        Vegetation.__init__(self, x, y, emoji="🌱")
        Grass.count += 1

    def __del__(self):
        Grass.count -= 1
