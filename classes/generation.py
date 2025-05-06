from chessModel. chessModel import ChessModel
from classes. model import Model
from chess import Board

class Generation():
    def __init__(self, size, out):
        self.out = out
        self.chessModels = []
        for i in range(size):
            self.chessModels.append(ChessModel(Model(64, [1048, 512, 512, 1])))

    def start(self):
        while True:
            pass

    def battle(models):
        firstPl = models[0]
        secondPl = models[1]

        board = Board()

        while True:
            if int(board.turn) % 2 == 0:
                board.push(list(board.legal_moves)[firstPl.getMove(board)])
            else:
                board.push(list(board.legal_moves)[secondPl.getMove(board)])

            if board.is_game_over():
                break
    