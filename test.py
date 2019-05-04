import curses
import numpy as np

animals = [
    "🐰",
    "🐅",
    "🐆",
    "🐘",
    "🦏",
    "🐂",
    "🐃",
    "🐄",
    "🐎",
    "🦌",
    "🐐",
    "🐏",
    "🐑",
    "🐖",
    "🐗",
    "🦛",
    "🐪",
    "🐫",
    "🦍",
    "🦙",
]


def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    for i in range(20):
        for j in range(50):
            stdscr.addstr(i, j, animals[int(np.random.uniform(high=len(animals)))])
    stdscr.getkey()


curses.wrapper(main)
