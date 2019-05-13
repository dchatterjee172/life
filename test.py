from stuff import Env, Grass, Tiger, Rabbit

from display import Display
import curses
import sys

all_stuff = (Grass, Tiger, Rabbit)
env = Env(all_stuff=all_stuff, cum_weights=(0.8, 0.9, 1))
dis = Display(12, 12, 1, 1)
try:
    while True:
        dis.show(env.board)
        env.next_step()
        curses.napms(100)
except KeyboardInterrupt:
    curses.endwin()
    sys.exit(0)
