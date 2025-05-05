import numpy
from classes.model import Model
from chessModel. chessModel import ChessModel
from chess import Board
from chessModel. parserBoard import ParserBoard

firstPl = ChessModel(Model(65, [12500, 2000, 1600, 1]))
secondPl = ChessModel(Model(65, [12500, 2000, 1600, 1]))

board = Board()

print(firstPl.getMove(board))