from stuff import Env
from display import Display
import curses

env = Env()
env.print()
dis = Display(12, 12, 1, 1)
dis.show(env.board)
curses.napms(1000)
curses.endwin()
