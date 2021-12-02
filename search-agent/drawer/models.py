from enum import Enum
import random

class State:

    laminate_dimensions = [
        (8, 3),
        (5, 1),
        (2, 2),
        (1, 1),
        (9, 4),
        (6, 2),
        (4, 3),
        (7, 5),
        (3, 2),
        (4, 2)
    ]

    def __init__(self):
        self.laminates = []
        for i in range(10):
            self.laminates.append(Laminate(random.randint(0, 9), random.randint(0, 9), random.randint(0, 1), random.randint(0, 1)))


class Laminate:

    def __init__(self, x, y, rotation, sheet):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.sheet = sheet

    
class Rotation(Enum):
    VERTICAL = 0
    HORIZONTAL = 1