from stuff import Env, Grass, Tiger, Rabbit, max_x, max_y

from display import Display
import curses
import sys
from collections import defaultdict
import multiprocessing as mp

all_stuff = (Grass, Tiger, Rabbit)
env = Env(all_stuff=all_stuff, cum_weights=(0.8, 0.9, 1))
dis = Display(max_x + 2, max_y + 2, 1, 1)


def run_env(queue, env):
    while True:
        env.next_step()
        queue.put(env.all_objects)


def run_display(queue, dis):
    while True:
        all_objects = queue.get()
        life_force = defaultdict(lambda: -1000000)
        _board = [["🍂" for x in range(max_x)] for y in range(max_y)]
        for x, y, obj in all_objects:
            if life_force[x, y] < obj.life_force:
                _board[x][y] = obj.emoji
                life_force[x, y] = obj.life_force
        dis.show(_board)
        curses.napms(500)


try:
    mp.set_start_method("spawn")
    queue = mp.Queue()
    env_p = mp.Process(target=run_env, args=(queue, env))
    dis_p = mp.Process(target=run_display, args=(queue, dis))
    env_p.start()
    dis_p.start()
except KeyboardInterrupt:
    curses.endwin()
    sys.exit(0)
