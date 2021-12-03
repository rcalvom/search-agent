# this solution was made based on the code from https://www.youtube.com/watch?v=T28fr9wDZrg

import time
import math
import random
from agent.func import objective_function, movements
import matplotlib.pyplot as plt

class SimulatedAnnealing:
  
  def __init__(self, state):
    self.state = state

  def solution(self):
    cooling = 0.8 # cooling coefficient
    computing_time = 1 # seconds
    initial_solution = self.state.laminates
    current_solution = initial_solution
    best_solution = initial_solution
    n = 1  # no of solutions accepted
    best_fitness = objective_function(best_solution)
    current_temperature = 100 # current status
    start = time.time()
    no_attempts = 100 # number of attempts in each level of temperature
    record_best_fitness =[best_fitness]

    for i in range(9999999):
      for j in range(no_attempts):
        current_solution = movements(current_solution) #current solution is the old solution (current solution variable) moved
        current_fitness = objective_function(current_solution)
        E = abs(current_fitness - best_fitness)

        if i == 0 and j == 0:
          EA = E

        if current_fitness < best_fitness: # minimization problem
          accept = True
        else:
          p = math.exp(-E/(EA*current_temperature))
          # make a decision to accept the worse solution or not based on probability
          if random.random() < p:
            accept = True # this worse solution is accepted
          else:
            accept = False # this worse solution is not accepted
        
        if accept:
          best_solution = current_solution # update the best solution
          best_fitness = objective_function(best_solution) # update the best fitness
          n += 1
          EA = (EA*(n - 1) + E)/n # update EA
      
      record_best_fitness.append(best_fitness)
      # cooling the temperature
      current_temperature *= cooling
      # stop by computing time
      end = time.time()
      if end - start >= computing_time:
        break

    plt.plot(record_best_fitness)
    plt.show()
  
    return best_solution


  



