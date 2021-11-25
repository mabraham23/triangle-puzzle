#!/usr/bin/env python3

import random
from typing import NewType

class Model:

  def __init__(self, pieces, board, animals, rows):
    self.pieces = self.create_pieces(pieces)
    self.board = board
    self.animals = animals
    self.rows = rows

  def create_pieces(self, pieces):
    new_pieces = []
    for piece in pieces:
      new_pieces.append(Piece(piece))
    return new_pieces


  def calc_num_conflicts(self):
    conflicts = 0
    if self.rows == 3:
      # piece 0
      if is_conflict(self.board[0], self.pieces[0].zero):
        conflicts += 1
      if is_conflict(self.board[3], self.pieces[0].one):
        conflicts += 1
      if is_conflict(self.pieces[0].two, self.pieces[2].one):
        conflicts += 1
      #piece 1
      if is_conflict(self.board[1], self.pieces[1].zero):
        conflicts += 1
      if is_conflict(self.pieces[1].one, self.pieces[2].zero):
        conflicts += 1
      if is_conflict(self.pieces[1].two, self.pieces[5].one):
        conflicts += 1
      #piece 2
      if is_conflict(self.pieces[2].two, self.pieces[3].zero):
        conflicts += 1
      #piece 3
      if is_conflict(self.pieces[3].one, self.board[4]):
        conflicts += 1
      if is_conflict(self.pieces[3].two, self.pieces[7].one):
        conflicts += 1
      #piece 4
      if is_conflict(self.board[2], self.pieces[4].zero):
        conflicts += 1
      if is_conflict(self.pieces[4].one, self.pieces[5].zero):
        conflicts += 1
      if is_conflict(self.pieces[4].two, self.board[6]):
        conflicts += 1
      #piece 5
      if is_conflict(self.pieces[5].two, self.pieces[6].zero):
        conflicts += 1
      #piece 6
      if is_conflict(self.pieces[6].one, self.pieces[7].zero):
        conflicts += 1
      if is_conflict(self.pieces[6].two, self.board[7]):
        conflicts += 1
      #piece 7
      if is_conflict(self.pieces[7].two, self.pieces[8].zero):
        conflicts += 1
      #piece 8
      if is_conflict(self.pieces[8].one, self.board[5]):
        conflicts += 1
      if is_conflict(self.pieces[8].two, self.board[8]):
        conflicts += 1
      
    elif self.rows == 4:
      # piece 0
      if is_conflict(self.board[0], self.pieces[0].zero):
        conflicts += 1
      if is_conflict(self.board[3], self.pieces[0].one):
        conflicts += 1
      if is_conflict(self.pieces[0].two, self.pieces[2].one):
        conflicts += 1
      #piece 1
      if is_conflict(self.board[1], self.pieces[1].zero):
        conflicts += 1
      if is_conflict(self.pieces[1].one, self.pieces[2].zero):
        conflicts += 1
      if is_conflict(self.pieces[1].two, self.pieces[5].one):
        conflicts += 1
      #piece 2
      if is_conflict(self.pieces[2].two, self.pieces[3].zero):
        conflicts += 1
      #piece 3
      if is_conflict(self.pieces[3].one, self.board[4]):
        conflicts += 1
      if is_conflict(self.pieces[3].two, self.pieces[7].one):
        conflicts += 1
      #piece 4
      if is_conflict(self.board[2], self.pieces[4].zero):
        conflicts += 1
      if is_conflict(self.pieces[4].one, self.pieces[5].zero):
        conflicts += 1
      if is_conflict(self.pieces[4].two, self.pieces[10].one):
        conflicts += 1
      #piece 5
      if is_conflict(self.pieces[5].two, self.pieces[6].zero):
        conflicts += 1
      #piece 6
      if is_conflict(self.pieces[6].one, self.pieces[7].zero):
        conflicts += 1
      if is_conflict(self.pieces[6].two, self.pieces[12].one):
        conflicts += 1
      #piece 7
      if is_conflict(self.pieces[7].two, self.pieces[8].zero):
        conflicts += 1
      #piece 8
      if is_conflict(self.pieces[8].one, self.board[5]):
        conflicts += 1
      if is_conflict(self.pieces[8].two, self.pieces[14].one):
        conflicts += 1
      #piece 9
      if is_conflict(self.board[3], self.pieces[9].zero):
        conflicts += 1
      if is_conflict(self.pieces[9].one, self.pieces[10].zero):
        conflicts += 1
      if is_conflict(self.pieces[9].two, self.board[8]):
        conflicts += 1
      #piece 10
      if is_conflict(self.pieces[10].two, self.pieces[11].zero):
        conflicts += 1
      #piece 11
      if is_conflict(self.pieces[11].one, self.pieces[12].zero):
        conflicts += 1
      if is_conflict(self.pieces[11].two, self.board[9]):
        conflicts += 1
      #piece 12
      if is_conflict(self.pieces[12].two, self.pieces[13].zero):
        conflicts += 1
      #piece 13
      if is_conflict(self.pieces[13].one, self.pieces[14].zero):
        conflicts += 1
      if is_conflict(self.pieces[13].two, self.board[10]):
        conflicts += 1
      #piece 14
      if is_conflict(self.pieces[14].two, self.pieces[15].zero):
        conflicts += 1
      #piece 15
      if is_conflict(self.pieces[15].one, self.board[7]):
        conflicts += 1
      if is_conflict(self.pieces[15].two, self.board[11]):
        conflicts += 1
    
    return conflicts


  def print_pieces(self):
    count = 0
    for piece in self.pieces:
      print( count, "zero:", piece.zero, "one:", piece.one, "two:", piece.two)
      count += 1


def is_conflict(side1, side2):
  if side1.isupper() and side2.islower():
    if side1.lower() == side2:
      return False
  elif side1.islower() and side2.isupper():
    if side1 == side2.lower():
      return False
  return True




class Piece:

  def __init__(self, sides):
    self.zero = sides[0]
    self.one = sides[1]
    self.two = sides[2]

  def rotate(self, direction):
    if direction == "clockwise":
      self.zero, self.one, self.two = self.two, self.zero, self.one
    elif direction == "counterclockwise":
      self.zero, self.one, self.two = self.one, self.two, self.zero

  