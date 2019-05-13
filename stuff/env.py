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
        self.board_size = max_x * max_y
        self.all_stuff = all_stuff
        self.all_objects = []
        self._populate(cum_weights)

    @property
    def board(self):
        life_force = defaultdict(lambda: -1000000)
        self._board = [["🍂" for x in range(max_x)] for y in range(max_y)]
        for x, y, obj in self.all_objects:
            if life_force[x, y] < obj.life_force:
                self._board[x][y] = obj.emoji
                life_force[x, y] = obj.life_force

        return self._board

    def _populate(self, cum_weights):
        self.time += 1
        for (x, y), cls in zip(
            product(range(max_x), range(max_y)),
            choices(self.all_stuff, cum_weights=cum_weights, k=self.board_size),
        ):
            obj = cls(x=x, y=y)
            self.all_objects.append([x, y, obj])

    def next_step(self):
        self.time += 1
        dead = []
        for i, (_, _, obj) in enumerate(self.all_objects):
            if hasattr(obj, "move"):
                obj.move()
                if obj.life_force <= 0.1:
                    dead.append(i)
                    continue
                self.all_objects[i] = [*obj.coord, obj]
        dead.sort(reverse=True)
        for d in dead:
            del self.all_objects[d]
