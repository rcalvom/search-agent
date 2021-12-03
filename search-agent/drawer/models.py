from enum import Enum
import random

class State:
    laminate_dimensions = [(8, 3), (5, 1), (2, 2), (1, 1), (9, 4), (6, 2), (4, 3), (7, 5), (3, 2), (4, 2)]

    def __init__(self):
        self.laminates = []
        for i in self.laminate_dimensions:
            self.laminates.append(Laminate(random.randint(0, 9), random.randint(0, 9), i[0], i[1], random.randint(0, 1), random.randint(0, 1)))


class Laminate:

    def __init__(self, x, y, width, height, rotation, used):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation
        self.used = used

    
# class Rotation(Enum):
    # VERTICAL = 0
    # HORIZONTAL = 1