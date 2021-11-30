#!/usr/bin/env python3

import random
from typing import NewType
import copy 

class Model:

  def __init__(self, pieces, board, animals, rows):
    self.pieces = self.create_pieces(pieces)
    self.board = board
    self.animals = animals
    self.rows = rows
    self.placed_pieces = self.placed_pieces()

  def create_pieces(self, pieces):
    new_pieces = []
    for piece in pieces:
      new_pieces.append(Piece(piece))
    return new_pieces

  def placed_pieces(self):
    pieces = []
    for piece in self.pieces:
      pieces.append(Piece(["empty", "empty", "empty"]));
    return pieces

  def find_empty_space(self):
    for i in range(len(self.placed_pieces)):
      if self.placed_pieces[i].zero == "empty":
        return i
    return -1
  
  def all_pieces_placed(self):
    for piece in self.placed_pieces:
      if piece.zero == "empty":
        return False
    return True


  def get_legal_actions(self):

    if self.all_pieces_placed():
      return []

    legal_actions = []
    next_emtpy_space = self.find_empty_space()
    for piece in self.pieces:
      for rotation in range(3):
        piece_copy = copy.deepcopy(piece)
        if rotation == 1:
          piece_copy.rotate("clockwise")
        elif rotation == 2:
          piece_copy.rotate("clockwise")
          piece_copy.rotate("clockwise")

        if self.rows == 3:
          if next_emtpy_space == 0:
            if no_conflict(piece_copy.zero, self.board[0]) and no_conflict(piece_copy.one, self.board[3]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 1:
            if no_conflict(piece_copy.zero, self.board[1]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 2:
            if no_conflict(piece_copy.zero, self.placed_pieces[1].one) and no_conflict(piece_copy.one, self.placed_pieces[0].two):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 3:
            if no_conflict(piece_copy.zero, self.placed_pieces[2].two) and no_conflict(piece_copy.one, self.board[4]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 4:
            if no_conflict(piece_copy.zero, self.board[2]) and no_conflict(piece_copy.two, self.board[6]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 5:
            if no_conflict(piece_copy.zero, self.placed_pieces[4].one) and no_conflict(piece_copy.one, self.placed_pieces[1].two):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 6:
            if no_conflict(piece_copy.zero, self.placed_pieces[5].two) and no_conflict(piece_copy.two, self.board[7]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 7:
            if no_conflict(piece_copy.zero, self.placed_pieces[6].one) and no_conflict(piece_copy.one, self.placed_pieces[3].two):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 8:
            if no_conflict(piece_copy.zero, self.placed_pieces[7].two) and no_conflict(piece_copy.one, self.board[5]) and no_conflict(piece_copy.two, self.board[8]):
              legal_actions.append(piece_copy)

        elif self.rows == 4:
          if next_emtpy_space == 0:
            if no_conflict(piece_copy.zero, self.board[0]) and no_conflict(piece_copy.one, self.board[4]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 1:
            if no_conflict(piece_copy.zero, self.board[1]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 2:
            if no_conflict(piece_copy.zero, self.placed_pieces[1].one) and no_conflict(piece_copy.one, self.placed_pieces[0].two):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 3:
            if no_conflict(piece_copy.zero, self.placed_pieces[2].two) and no_conflict(piece_copy.one, self.board[5]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 4:
            if no_conflict(piece_copy.zero, self.board[2]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 5:
            if no_conflict(piece_copy.zero, self.placed_pieces[4].one) and no_conflict(piece_copy.one, self.placed_pieces[1].two):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 6:
            if no_conflict(piece_copy.zero, self.placed_pieces[5].two):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 7:
            if no_conflict(piece_copy.zero, self.placed_pieces[6].one) and no_conflict(piece_copy.one, self.placed_pieces[3].two):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 8:
            if no_conflict(piece_copy.zero, self.placed_pieces[7].two) and no_conflict(piece_copy.one, self.board[6]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 9:
            if no_conflict(piece_copy.zero, self.board[3]) and no_conflict(piece_copy.two, self.board[8]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 10:
            if no_conflict(piece_copy.zero, self.placed_pieces[9].one) and no_conflict(piece_copy.one, self.placed_pieces[4].two):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 11:
            if no_conflict(piece_copy.zero, self.placed_pieces[10].two) and no_conflict(piece_copy.two, self.board[9]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 12:
            if no_conflict(piece_copy.zero, self.placed_pieces[11].one) and no_conflict(piece_copy.one, self.placed_pieces[6].two):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 13:
            if no_conflict(piece_copy.zero, self.placed_pieces[12].two) and no_conflict(piece_copy.two, self.board[10]):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 14:
            if no_conflict(piece_copy.zero, self.placed_pieces[13].one) and no_conflict(piece_copy.one, self.placed_pieces[8].two):
              legal_actions.append(piece_copy)
          elif next_emtpy_space == 15:
            if no_conflict(piece_copy.zero, self.placed_pieces[14].two) and no_conflict(piece_copy.one, self.board[7]) and no_conflict(piece_copy.two, self.board[11]):
              legal_actions.append(piece_copy)

    return legal_actions



  # def get_legal_actions(self):
  #   actions = []
  #   original_conflicst = self.calc_num_conflicts()
  #   # by the time all pieces have been placed, there should be a winning configuration
  #   index = self.find_empty_space()

  #   for piece in self.pieces:
  #     self.placed_pieces[index] = piece 
  #     for rotation in range(3):
  #       if self.calc_num_conflicts() < (original_conflicst):
  #         piece_copy = copy.deepcopy(piece)
  #         if len(actions) == 0:
  #           actions.append(piece_copy)
  #           piece.rotate("clockwise")
  #           continue
  #         duplicate = False
  #         for a in actions:
  #           if self.same_piece_and_rotation(a, piece_copy):
  #             duplicate = True
  #             break
  #         if not duplicate:
  #           actions.append(piece_copy)
  #         piece.rotate("clockwise")
  #       else:
  #         piece.rotate("clockwise")
  #     self.placed_pieces[index] = Piece(["empty", "empty", "empty"])
  #   return actions

  def apply_action(self, piece):
    ind = self.index_of_piece(piece)
    new_state = copy.deepcopy(self)
    new_state.pieces.pop(ind)
    index = new_state.find_empty_space()
    new_state.placed_pieces[index] = piece
    return new_state
  
  def index_of_piece(self, piece):
    for i in range(len(self.pieces)):
      if self.same_piece(self.pieces[i], piece):
        return i
    return -1

  def same_piece(self, piece1, piece2):
    if piece1.zero == piece2.zero and piece1.one == piece2.one and piece1.two == piece2.two:
      return True
    elif piece1.zero == piece2.two and piece1.one == piece2.zero and piece1.two == piece2.one:
      return True
    elif piece1.zero == piece2.one and piece1.one == piece2.two and piece1.two == piece2.zero:
      return True
    return False

  def same_piece_and_rotation(self, piece1, piece2):
    if piece1.zero == piece2.zero and piece1.one == piece2.one and piece1.two == piece2.two:
      return True
    # elif piece1.zero == piece2.two and piece1.one == piece2.zero and piece1.two == piece2.one:
    #   return True
    # elif piece1.zero == piece2.one and piece1.one == piece2.two and piece1.two == piece2.zero:
      # return True
    return False

  def calc_num_conflicts(self):
    conflicts = 0
    if self.rows == 3:
      # piece 0
      if is_conflict(self.board[0], self.placed_pieces[0].zero):
        conflicts += 1
      if is_conflict(self.board[3], self.placed_pieces[0].one):
        conflicts += 1
      if is_conflict(self.placed_pieces[0].two, self.placed_pieces[2].one):
        conflicts += 1
      #piece 1
      if is_conflict(self.board[1], self.placed_pieces[1].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[1].one, self.placed_pieces[2].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[1].two, self.placed_pieces[5].one):
        conflicts += 1
      #piece 2
      if is_conflict(self.placed_pieces[2].two, self.placed_pieces[3].zero):
        conflicts += 1
      #piece 3
      if is_conflict(self.placed_pieces[3].one, self.board[4]):
        conflicts += 1
      if is_conflict(self.placed_pieces[3].two, self.placed_pieces[7].one):
        conflicts += 1
      #piece 4
      if is_conflict(self.board[2], self.placed_pieces[4].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[4].one, self.placed_pieces[5].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[4].two, self.board[6]):
        conflicts += 1
      #piece 5
      if is_conflict(self.placed_pieces[5].two, self.placed_pieces[6].zero):
        conflicts += 1
      #piece 6
      if is_conflict(self.placed_pieces[6].one, self.placed_pieces[7].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[6].two, self.board[7]):
        conflicts += 1
      #piece 7
      if is_conflict(self.placed_pieces[7].two, self.placed_pieces[8].zero):
        conflicts += 1
      #piece 8
      if is_conflict(self.placed_pieces[8].one, self.board[5]):
        conflicts += 1
      if is_conflict(self.placed_pieces[8].two, self.board[8]):
        conflicts += 1
      
    elif self.rows == 4:
      # piece 0
      if is_conflict(self.board[0], self.placed_pieces[0].zero):
        conflicts += 1
      if is_conflict(self.board[4], self.placed_pieces[0].one):
        conflicts += 1
      if is_conflict(self.placed_pieces[0].two, self.placed_pieces[2].one):
        conflicts += 1
      #piece 1
      if is_conflict(self.board[1], self.placed_pieces[1].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[1].one, self.placed_pieces[2].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[1].two, self.placed_pieces[5].one):
        conflicts += 1
      #piece 2
      if is_conflict(self.placed_pieces[2].two, self.placed_pieces[3].zero):
        conflicts += 1
      #piece 3
      if is_conflict(self.placed_pieces[3].one, self.board[5]):
        conflicts += 1
      if is_conflict(self.placed_pieces[3].two, self.placed_pieces[7].one):
        conflicts += 1
      #piece 4
      if is_conflict(self.board[2], self.placed_pieces[4].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[4].one, self.placed_pieces[5].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[4].two, self.placed_pieces[10].one):
        conflicts += 1
      #piece 5
      if is_conflict(self.placed_pieces[5].two, self.placed_pieces[6].zero):
        conflicts += 1
      #piece 6
      if is_conflict(self.placed_pieces[6].one, self.placed_pieces[7].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[6].two, self.placed_pieces[12].one):
        conflicts += 1
      #piece 7
      if is_conflict(self.placed_pieces[7].two, self.placed_pieces[8].zero):
        conflicts += 1
      #piece 8
      if is_conflict(self.placed_pieces[8].one, self.board[6]):
        conflicts += 1
      if is_conflict(self.placed_pieces[8].two, self.placed_pieces[14].one):
        conflicts += 1
      #piece 9
      if is_conflict(self.board[3], self.placed_pieces[9].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[9].one, self.placed_pieces[10].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[9].two, self.board[8]):
        conflicts += 1
      #piece 10
      if is_conflict(self.placed_pieces[10].two, self.placed_pieces[11].zero):
        conflicts += 1
      #piece 11
      if is_conflict(self.placed_pieces[11].one, self.placed_pieces[12].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[11].two, self.board[9]):
        conflicts += 1
      #piece 12
      if is_conflict(self.placed_pieces[12].two, self.placed_pieces[13].zero):
        conflicts += 1
      #piece 13
      if is_conflict(self.placed_pieces[13].one, self.placed_pieces[14].zero):
        conflicts += 1
      if is_conflict(self.placed_pieces[13].two, self.board[10]):
        conflicts += 1
      #piece 14
      if is_conflict(self.placed_pieces[14].two, self.placed_pieces[15].zero):
        conflicts += 1
      #piece 15
      if is_conflict(self.placed_pieces[15].one, self.board[7]):
        conflicts += 1
      if is_conflict(self.placed_pieces[15].two, self.board[11]):
        conflicts += 1
    
    return conflicts


  def print_solution(self):
    for piece in self.placed_pieces:
      print(piece.zero + piece.one + piece.two)

def no_conflict(side1, side2):
  if side1.isupper() and side2.islower():
    if side1.lower() == side2:
      return True
  elif side1.islower() and side2.isupper():
    if side1 == side2.lower():
      return True
  elif side1 == "[" and side2 == "{":
    return True
  elif side1 == "{" and side2 == "[":
    return True
  elif side1 == "}" and side2 == "]":
    return True
  elif side1 == "]" and side2 == "}":
    return True
  elif side1 == "^" and side2 == "~":
    return True
  elif side1 == "~" and side2 == "^":
    return True
  elif side1 == "|" and side2 == "\\":
    return True
  elif side1 == "\\" and side2 == "|":
    return True
  return False


def is_conflict(side1, side2):
  if side1.isupper() and side2.islower():
    if side1.lower() == side2:
      return False
  elif side1.islower() and side2.isupper():
    if side1 == side2.lower():
      return False
  elif side1 == "[" and side2 == "{":
    return False
  elif side1 == "{" and side2 == "[":
    return False
  elif side1 == "}" and side2 == "]":
    return False
  elif side1 == "]" and side2 == "}":
    return False
  elif side1 == "^" and side2 == "~":
    return False
  elif side1 == "~" and side2 == "^":
    return False
  elif side1 == "|" and side2 == "\\":
    return False
  elif side1 == "\\" and side2 == "|":
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

  