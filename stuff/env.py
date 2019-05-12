from stuff.conf import max_x, max_y
from itertools import product
from random import choices
from collections import defaultdict


class Env:
    def __init__(self, all_stuff, cum_weights):
        if len(all_stuff) != len(cum_weights):
            raise ValueError("all_stuff, cum_weights should have same length")
        self.max_x = max_x
        self.max_y = max_y
        self.time = -1
        self._board = [[" " for x in range(max_x)] for y in range(max_y)]
        self.board_dict = defaultdict(list)
        self.board_size = max_x * max_y
        self.all_stuff = all_stuff
        self._populate(cum_weights)

    @property
    def board(self):
        for (x, y), obj_list in self.board_dict.items():
            try:
                print(x, y)
                self._board[x][y] = max(obj_list, key=lambda x: x.life_force).emoji
            except ValueError:
                self._board = " "
        return self._board

    def _populate(self, cum_weights):
        self.time += 1
        for (x, y), cls in zip(
            product(range(max_x), range(max_y)),
            choices(self.all_stuff, cum_weights=cum_weights, k=self.board_size),
        ):
            obj = cls(x=x, y=y)
            self.board_dict[x, y].append(obj)

    def next_step(self):
        self.time += 1
