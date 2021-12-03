import numpy as np
import random

def board_calc(lams):
  board = np.zeros((6, 6))

  for laminate in lams:
    if laminate.used:
      width = laminate.width if laminate.rotation else laminate.height
      height = laminate.height if laminate.rotation else laminate.width
      for i in range(laminate.y, laminate.y + height): # y movement into the matrix
        for j in range(laminate.x, laminate.x + width): # x movement into the matrix
          if 0 <= i < 6 and 0 <= j < 6:
            if board[i, j] == 0:
              board[i, j] = 1
            elif board[i, j] != 0:
              board[i, j] += 1

  return board
 
def objective_function(lams):
  return np.count_nonzero(board_calc(lams) != 1) # number of overlap and blank cells

def movements(lams): # movement of laminates based on a random number
  result = []

  for lam in lams:
      randnumber = random.randint(0, 5) # 0: up, 1: down, 2: left, 3: right, 4: rotation, 5: used
      if randnumber == 0 and lam.y - 1 >= 0: # upward movement
        lam.y = lam.y - 1
      elif randnumber == 1 and lam.y + 1 < 6: # downward movement
        lam.y = lam.y + 1
      elif randnumber == 2 and lam.x - 1 >= 0: # leftward movement
        lam.x = lam.x - 1
      elif randnumber == 3 and lam.x + 1 < 6: # rightward movement
        lam.x = lam.x + 1
      elif randnumber == 4: # rotation
        lam.rotation = not lam.rotation
      elif randnumber == 5: # present
        lam.used = not lam.used
      
      result.append(lam)
  
  return result