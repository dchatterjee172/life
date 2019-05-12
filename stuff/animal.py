import numpy as np
from stuff.conf import max_x, max_y
from stuff.vegetation import Grass


class Animal:
    def __init__(self, x, y, life_force, emoji, eats):
        self.x = x
        self.y = y
        self.life_force = life_force
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
        self.life_force -= self.life_force * 0.01


class Tiger(Animal):
    def __init__(self, x, y):
        life_force = np.random.normal(loc=50, scale=2)
        Animal.__init__(self, x=x, y=y, life_force=life_force, emoji="🐅", eats=[Rabbit])


class Rabbit(Animal):
    def __init__(self, x, y):
        life_force = np.random.normal(loc=10, scale=2)
        Animal.__init__(self, x=x, y=y, life_force=life_force, emoji="🐇", eats=[Grass])
