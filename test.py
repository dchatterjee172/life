from stuff import Env, Grass, Tiger, Rabbit
from display import Display
import curses

all_stuff = (Grass, Tiger, Rabbit)
env = Env(all_stuff=all_stuff, cum_weights=(0.5, 0.7, 1))
dis = Display(12, 12, 1, 1)
dis.show(env.board)
curses.napms(1000)
curses.endwin()
