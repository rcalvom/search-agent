import numpy as np
import copy

def f(x):
    """f(x) : = 'La suma del desperdicio con la suma de los solapes' """
    sheet = np.zeros((10, 10))

    for laminate in x.laminates:
        out = 0
        for i in range(laminate.x, laminate.x + laminate.width):
            for j in range(laminate.y, laminate.y + laminate.heigth):
                if laminate.placed:
                    if (0 <= i and i < 10) and (0 <= j and j < 10):
                        sheet[i, j] += 1
                    else:
                        out += 1
                
    return np.count_nonzero(sheet == 0)

def find_neighbor_states(x):
    neighbours = []
    for i in range(len(x.laminates)):
        x_p = copy.deepcopy(x)
        x_p.laminates[i].x += 1
        neighbours.append(x_p)
    for i in range(len(x.laminates)):
        x_p = copy.deepcopy(x)
        x_p.laminates[i].x -= 1
        neighbours.append(x_p)
    for i in range(len(x.laminates)):
        x_p = copy.deepcopy(x)
        x_p.laminates[i].y += 1
        neighbours.append(x_p)
    for i in range(len(x.laminates)):
        x_p = copy.deepcopy(x)
        x_p.laminates[i].y -= 1
        neighbours.append(x_p)
    for i in range(len(x.laminates)):
        x_p = copy.deepcopy(x)
        x_p.laminates[i].width, x_p.laminates[i].heigth = x_p.laminates[i].heigth, x_p.laminates[i].width
        neighbours.append(x_p)
    for i in range(len(x.laminates)):
        x_p = copy.deepcopy(x)
        x_p.laminates[i].placed = not x_p.laminates[i].placed
        neighbours.append(x_p)
    return neighbours


def best_neighbour(x):
    neighbours = find_neighbor_states(x)
    best_neighbour = x
    for neighbour in neighbours:
        if f(neighbour) < f(best_neighbour):
            best_neighbour = neighbour
    return best_neighbour
