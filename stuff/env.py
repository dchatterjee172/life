from stuff.conf import max_x, max_y
from itertools import product
from random import choices


class Env:
    def __init__(self):
        self.max_x = max_x
        self.max_y = max_y
        self.time = -1
        self.board = [[" " for x in range(max_x)] for y in range(max_y)]
        self.board_dict = {(x, y): [] for x in range(max_x) for y in range(max_y)}
        self.board_size = max_x * max_y

    def populate(self, all_stuff, cum_weights):
        if len(all_stuff) != len(cum_weights):
            raise ValueError("all_stuff, cum_weights should have same length")
        self.time += 1
        for (x, y), cls in zip(
            product(range(max_x), range(max_y)),
            choices(all_stuff, cum_weights=cum_weights, k=self.board_size),
        ):
            obj = cls(x=x, y=y)
            self.board_dict[x, y].append(obj)
            self.board[x][y] = obj.emoji

    def print(self):
        for row in self.board:
            for cell in row:
                print(cell, end="")
            print()

    def next_step(self):
        if self.time < 0:
            raise Exception("populate first")
        self.time += 1
