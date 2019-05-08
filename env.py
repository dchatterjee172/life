from collections import defaultdict


class Env:
    def __init__(self, max_x, max_y, initial_animal=50):
        self.max_x = max_x
        self.max_y = max_y
        self.board = [["🌳" for x in range(max_x)] for y in range(max_y)]
        self.board_dict = defaultdict(list)

    def print(self):
        for row in self.board:
            for cell in row:
                print(cell, end="")
            print()

    def next_step(self):
        pass
