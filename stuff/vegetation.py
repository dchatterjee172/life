class Vegetation:
    def __init__(self, x, y, emoji):
        self.x = x
        self.y = y
        self.emoji = emoji

    @property
    def coord(self):
        return self.x, self.y


class Grass(Vegetation):
    def __init__(self, x, y):
        Vegetation.__init__(self, x, y, emoji="🌱")
