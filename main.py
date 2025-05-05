import numpy
from classes.model import Model
from chessModel. chessModel import ChessModel
from chess import Board
from chessModel. parserBoard import ParserBoard
import time
import chess.pgn
import os

firstPl = ChessModel(Model(64, [1048, 512, 512, 1]))
secondPl = ChessModel(Model(64, [1048, 512, 512, 1]))

board = Board()

while True:
    os.system("clear")

    print(board)

    if int(board.turn) % 2 == 0:
        board.push(list(board.legal_moves)[firstPl.getMove(board)])
    else:
        board.push(list(board.legal_moves)[secondPl.getMove(board)])

    if board.is_game_over():
        break

moves = board.move_stack

game = chess.pgn.Game()
game.headers["Event"] = "Example"

node = game.add_variation(moves[0])

for i in range(len(moves)):
    if i == 0: continue
    node = node.add_variation(moves[i])

print(game)