from stuff.conf import max_x, max_y
from itertools import product, filterfalse
from random import choices, randrange
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

    def _populate(self, cum_weights):
        self.time += 1
        for (x, y), cls in zip(
            product(range(max_x), range(max_y)),
            choices(self.all_stuff, cum_weights=cum_weights, k=self.board_size),
        ):
            obj = cls(x=x, y=y)
            self.all_objects.append((x, y, obj))

    def next_step(self):
        self.time += 1
        board_dict = defaultdict(lambda: defaultdict(list))
        for i, (_, _, obj) in enumerate(self.all_objects):
            obj.move()
            board_dict[obj.coord][type(obj).__name__].append(obj)
            self.all_objects[i] = (*obj.coord, obj)
        for _, obj_dict in board_dict.items():
            for k, v in obj_dict.items():
                for x in filterfalse(lambda x: not hasattr(x, "eat"), v):
                    if x.eats in obj_dict.keys() and len(obj_dict[x.eats]):
                        pray = obj_dict[x.eats].pop(randrange(len(obj_dict[x.eats])))
                        x.eat(pray.life_force)
                        pray.eaten()
        self.all_objects[:] = [t for t in self.all_objects if t[-1].life_force >= 0.1]
