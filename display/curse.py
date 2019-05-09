import curses


class Display:
    def __init__(self, height, width, begin_x, begin_y):
        self.height = height
        self.width = width
        self.begin_x = begin_x
        self.begin_y = begin_y
        self.height = height
        self.scr = curses.initscr()
        self.win = curses.newwin(height, width, begin_y, begin_x)
        curses.curs_set(0)
        pass

    def show(self, board):
        if len(board) > self.height:
            raise ValueError(
                f"num of row in board {len(board)}, max height {self.height}"
            )
        for i, row in enumerate(board):
            if len(row) > self.width:
                raise ValueError(
                    f"num of cell in {i} row is {len(row)}, max width {self.width}"
                )
            for j, cell in enumerate(row):
                self.scr.addstr(i, j, cell)
