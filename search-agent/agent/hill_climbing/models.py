from enum import Enum
import random

class State:

    laminate_dimensions = [(8, 3), (5, 1), (2, 2), (1, 1), (9, 4), (6, 2), (4, 3), (7, 5), (3, 2), (4, 2)]
    sheet_dimensions = (10, 10)

    def __init__(self):
        self.laminates = []
        for i in range(10):
            self.laminates.append(
                Laminate(
                    x=0,
                    y=0,
                    width=State.laminate_dimensions[i][0],
                    heigth=State.laminate_dimensions[i][1],
                    placed=False
                    #x=random.randrange(State.sheet_dimensions[0]),
                    #y=random.randrange(State.sheet_dimensions[1]),
                    #width=State.laminate_dimensions[i][0],
                    #heigth=State.laminate_dimensions[i][1],
                    #placed=random.choice([True, False])
                    
                )
            )


class Laminate:

    def __init__(self, x, y, width, heigth, placed):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.placed = placed
