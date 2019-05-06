# from ABC import ABC, abstractmethod
import curses
import numpy as np


class Animal():  # class Animal(ABC):
    def move():
        pass


class Rabbit(Animal):
    def __init__(self):
        Animal.__init__()

    def get_emoji(self):
        return "🐰"


class Environment:
    def __init__(self):
        self.xrange = 145
        self.yrange = 35
        self.animals = [
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
            " "  # no animal
        ]
        self.get_init_prob()

    def get_init_prob(self):
        constant = 250
        self.init_prob = [
            1 / (len(self.animals) + constant)] * (len(self.animals) - 1)
        self.init_prob.append((constant + 1) / (len(self.animals) + constant))

    def initialize_env(self, stdscr):
        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()
        for i in range(self.yrange):
            for j in range(self.xrange):
                stdscr.addstr(
                    i,
                    j,
                    list(np.random.choice(self.animals, 1, p=self.init_prob))[0]
                )
        return stdscr


def main(stdscr):
    obj = Environment()
    stdscr = obj.initialize_env(stdscr)
    stdscr.getkey()


curses.wrapper(main)
