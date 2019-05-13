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
        self.life_force = self.life_force * 0.9

    def eat(self, life_force):
        self.life_force += life_force

    def eaten(self):
        self.life_force = 0


class Tiger(Animal):
    count = 0

    def __init__(self, x, y):
        life_force = np.random.normal(loc=50, scale=2)
        Animal.__init__(
            self, x=x, y=y, life_force=life_force, emoji="🐅", eats=Rabbit.__name__
        )
        Tiger.count += 1

    def __del__(self):
        Tiger.count -= 1


class Rabbit(Animal):
    count = 0

    def __init__(self, x, y):
        life_force = np.random.normal(loc=10, scale=2)
        Animal.__init__(
            self, x=x, y=y, life_force=life_force, emoji="🐇", eats=Grass.__name__
        )
        Rabbit.count += 1

    def __del__(self):
        Rabbit.count -= 1
