import numpy as np
from stuff.conf import max_x, max_y
from stuff.vegetation import Grass


class Animal:
    def __init__(self, emoji, eats):
        self.x = np.random.randint(0, max_x)
        self.y = np.random.randint(0, max_y)
        self.emoji = emoji
        self.eats = eats

    @property
    def coord(self):
        return self.x, self.y

    def move(self):
        delta_x = round(np.random.uniform(-1, 1))
        delta_y = round(np.random.uniform(-1, 1))
        self.x = (self.x + delta_x) % max_x
        self.y = (self.y + delta_y) % max_y


class Tiger(Animal):
    def __init__(self):
        Animal.__init__(self, emoji="🐅", eats=[Rabbit])


class Rabbit(Animal):
    def __init__(self):
        Animal.__init__(self, emoji="🐇", eats=[Grass])
