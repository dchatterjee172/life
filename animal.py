import numpy as np
from collections import defaultdict
from time import sleep

max_x, max_y = 10, 10


class Animal:
    def __init__(self, emoji, eats_green, eats_meat):
        self.x = np.random.randint(0, max_x)
        self.y = np.random.randint(0, max_y)
        self.emoji = emoji
        self.eats_green = eats_green
        self.eats_meat = eats_meat

    @property
    def coord(self):
        return self.x, self.y

    def move(self, max_x, max_y):
        delta_x = round(np.random.uniform(-1, 1))
        delta_y = round(np.random.uniform(-1, 1))
        self.x = (self.x + delta_x) % max_x
        self.y = (self.y + delta_y) % max_y


class Env:
    def __init__(self, max_x, max_y, initial_animal=50):
        self.max_x = max_x
        self.max_y = max_y
        self.board = [["🌳" for x in range(max_x)] for y in range(max_y)]
        self.board_dict = defaultdict(list)
        for _ in range(initial_animal):
            ani = Animal("🦍", True, True)
            self.board_dict[ani.coord].append(ani)
            x, y = ani.coord
            self.board[x][y] = ani.emoji

    def print(self):
        for row in self.board:
            for cell in row:
                print(cell, end="")
            print()

    def next_step(self):
        for board_dict_key in self.board_dict:
            for i in range(len(self.board_dict[board_dict_key])):
                self.board_dict[board_dict_key][i].move(self.max_x, self.max_y)
                x, y = self.board_dict[board_dict_key][i].coord
                emoji = self.board_dict[board_dict_key][i].emoji
                self.board[x][y] = emoji


e = Env(max_x, max_y)
while 1:
    e.print()
    e.next_step()
    sleep(0.5)
    print()
