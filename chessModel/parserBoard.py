from chess import Board

class ParserBoard():
    def fromFenToNumbers(fen):
        table = []
        fenSplit = fen.split("/")

        for col in fenSplit:
            for f in col:
                if not f.isnumeric():
                    numF = 0

                    if f.lower() == 'r':
                        numF += 5
                    elif f.lower() == 'b':
                        numF += 4
                    elif f.lower() == 'n':
                        numF += 3
                    elif f.lower() == 'q':
                        numF += 9
                    elif f.lower() == 'k':
                        numF += 10
                    elif f.lower() == 'p':
                        numF += 1

                    if f.islower():
                        numF += 10

                    table.append(numF)
                else:
                    for i in range(ord(f) - 48):
                        table.append(0)

        return table

    def allPosiblePositionsNumbers(board: Board):
        allLegalMoves = list(board.legal_moves)
        posiblePositions = []

        for i in allLegalMoves:
            board.push(i)
            posiblePositions.append(ParserBoard.fromFenToNumbers(board.fen().split(" ")[0]))
            board.pop()

        return posiblePositions