from time import sleep
from drawer.drawer import Drawer
from agent.annealing.sa import SimulatedAnnealing
from drawer.models import *

drawer = Drawer()
state = State()
sa = SimulatedAnnealing(state) # simulated annealing solution

# drawer.draw(state)
newLaminates = sa.solution()
# for i in newLaminates:
  # print('x: {}, y: {}, used: {}'.format(i.x, i.y, i.used))
state.laminates = newLaminates

# drawer.draw(state) # draw the best configuration
