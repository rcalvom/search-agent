from drawer.drawer import Drawer
from agent.hill_climbing.models import *
from agent.hill_climbing.agent import *
import time

# Solución usando el método de busqueda del ascenso de la colina




drawer = Drawer(title="Hill Climbing")

S = State()

for i in range(1000):
    drawer.draw(S, i)
    time.sleep(0.2)
    S = best_neighbour(S)
