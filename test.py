from stuff import Env, Grass, Tiger, Rabbit, max_x, max_y

from display import Display
import curses
import sys

all_stuff = (Grass, Tiger, Rabbit)
env = Env(all_stuff=all_stuff, cum_weights=(0.8, 0.9, 1))
dis = Display(max_x + 2, max_y + 2, 1, 1)
try:
    while True:
        dis.show(env.board)
        env.next_step()
        curses.napms(500)
except KeyboardInterrupt:
    curses.endwin()
    sys.exit(0)
