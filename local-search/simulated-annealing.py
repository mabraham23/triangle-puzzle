#!/usr/bin/env python3

from __future__ import with_statement
import random
import math
from contextlib import contextmanager
import sys
from triangle_model import Model
import copy

def neighbors(model):
  model_copy = copy.deepcopy(model)
  # reanoomly pick piece swap or piece rotation
  r = random.randint(0, 2)
  if r >= 1:
    # swap
    # pick two random pieces that are not the same
    while True:
      p1 = random.randint(0, len(model_copy.pieces)-1)
      p2 = random.randint(0, len(model_copy.pieces)-1)
      if p1 != p2:
        break
    # swap the pieces
    model_copy.pieces[p1], model_copy.pieces[p2] = model_copy.pieces[p2], model_copy.pieces[p1]
    return model_copy
  else:
    # rotate
    # pick a random piece
    p = random.randint(0, len(model_copy.pieces)-1)
    # pick a random rotation
    piece = model_copy.pieces[p]
    # pick a random direction in clockwise or counterclockwise
    r = random.randint(0, 1)
    direction = ""
    if r == 0:
      direction = "clockwise"
    else:
      direction = "counterclockwise"
    piece.rotate(direction)
    return model_copy

# returns the board with the least conflicts
def simulated_annealing(model):
  T_min = pow(10, 0)
  T = pow(10, 5)
  u_curr =  -1 * model.calc_num_conflicts()
  B = 0.9
  updated = True
  best_run = copy.deepcopy(model)
  while updated or T > T_min:
    updated = False
    for i in range(len(model.pieces)):
      n = neighbors(model)
      u = n.calc_num_conflicts()
      if u == 0:
        return n, 0
      delta_u = - u - u_curr
      x = delta_u / T
      y = random.uniform(0, 1)
      z = pow(math.e, x)
      if y <= z:
        u_curr = -1 * u
        best_run = n
        updated = True
        break
    T = B*T
  return best_run, -1 * u_curr


def read_data(filename):
  f = open(filename, 'r')
  lines = f.readlines()

  count = 0
  pieces = []
  board = []
  for line in lines:
    line = line.strip()
    if line == 'load' or line == '' or line == 'solve hillclimb':
      continue
    if count == 0:
      rows = int(line)
    elif count == 1:
      animals = int(line)
    elif len(line) == 3:
      pieces.append(line)
    elif count > 2 and len(line) == 1:
      board.append(line)
    count += 1

  model = Model(pieces, board, animals, rows)
  return model

def main():

  global best_board
  global best_conflicts
  

  # filepath = sys.argv[1]
  filepath = 'puzzles/puzzle-3-01-01'
  model = read_data(filepath)
  best_board = model
  best_conflicts = model.calc_num_conflicts()
  random_restarts = 0

  while True:
    random_restarts += 1
    print(random_restarts)

    random.shuffle(model.pieces)

    best_run, conflicts = simulated_annealing(model)

    if conflicts == 0:
      best_board = best_run
      best_conflicts = conflicts
      print("Solution found!")
      break

    if conflicts < best_conflicts:
      best_board = best_run
      best_conflicts = conflicts
      print('new best board:')
      print(conflicts)
      print(best_board.print_pieces())
      print('\n')

  


# def signal_handler(signum, frame):
#   for team in best_teams:
#     print(team["score"], team["team"])
#   quit()

# signal.signal(signal.SIGALRM, signal_handler)
# signal.alarm(60)   
# try:
#     main()
# except:
#   quit()

if __name__ == '__main__':
  main()

