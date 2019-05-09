from stuff import Env
from display import Display

env = Env()
env.print()
dis = Display(10, 10, 0, 0)
dis.show(env.board)
