from classes. model import Model
from chess import Board
from chessModel. parserBoard import ParserBoard

class ChessModel():
    def __init__(self, model: Model):
        self.model = model

    def getMove(self, board: Board):
        positions = ParserBoard.allPosiblePositionsNumbers(board)
        rank = []

        for i in positions:
            for k in range(len(i)):
                i[k] /= 20

            rank.append(float(self.model.getRes(i)[0]))

        print(rank)

        if int(board.turn) == 1:
            return rank.index(max(rank))

        return rank.index(min(rank))