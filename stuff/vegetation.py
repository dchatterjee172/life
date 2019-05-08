import numpy as np
from stuff.conf import max_x, max_y


class Vegetation:
    def __init__(self, emoji):
        self.x = np.random.randint(0, max_x)
        self.y = np.random.randint(0, max_y)
        self.emoji = emoji

    @property
    def coord(self):
        return self.x, self.y
