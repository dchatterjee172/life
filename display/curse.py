import curses


class Display:
    def __init__(self, env, height, width, begin_x, begin_y):
        win = curses.newwin(height, width, begin_y, begin_x)
        curses.curs_set(0)
        pass
