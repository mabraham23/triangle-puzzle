#!/usr/bin/env python3

from __future__ import with_statement
import random
import math
from contextlib import contextmanager
import sys
from triangle_model import Model
import copy

def depth_first_search(initial_state):
  Q = []
  Q.append(initial_state)
  while len(Q) != 0:
    state = Q.pop(0)
    conf = state.calc_num_conflicts()
    if state.calc_num_conflicts() == 0:
      return state
    actions = state.get_legal_actions()
    if len(actions) == 0:
      continue
    for a in actions:
      new_state = state.apply_action(a)
      Q.insert(0, new_state)
      # Q.append(new_state)
  return


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
  filepath = 'puzzles/puzzle-4-30-01'
  model = read_data(filepath)
  num = model.calc_num_conflicts()
  complete_puzzle = depth_first_search(model)
  complete_puzzle.print_solution()



if __name__ == '__main__':
  main()

