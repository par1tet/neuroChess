from chess import Board

class ParserBoard():
    def fromFenToNumbers(fen):
        table = []
        fenSplit = fen.split("/")

        for x in range(len(fenSplit)):
            for y in range(len(fenSplit[x])):
                if not fenSplit[x][y].isnumeric():
                    color = "w"

                    if fenSplit[x][y].islower():
                        color = "b"

                    table.extend(ParserBoard.ordHotFiga(fenSplit[x][y].islower(), color, [x, y]))
                else:
                    for i in range(int(fenSplit[x][y])):
                        table.extend(ParserBoard.ordHotFiga("e", "b", [x + i, y]))

        return table

    def allPosiblePositionsNumbers(board: Board):
        allLegalMoves = list(board.legal_moves)
        posiblePositions = []

        for i in allLegalMoves:
            board.push(i)
            posiblePositions.append(ParserBoard.fromFenToNumbers(board.fen().split(" ")[0]))
            board.pop()

        return posiblePositions

    def ordHotFiga(typeOfFig, color, position):
        if typeOfFig == "e":
            whatReturn = ([0] * 8)
            whatReturn.extend([position[0] / 8, position[1] / 8])
            return whatReturn

        typeFig = [0] * 6
        whereChange = 0

        if typeOfFig == "n":
            whereChange = 1
        elif typeOfFig == "b":
            whereChange = 2
        elif typeOfFig == "r":
            whereChange = 3
        elif typeOfFig == "q":
            whereChange = 4
        elif typeOfFig == "k":
            whereChange = 5

        typeFig[whereChange] = 1

        cost = [1, 3, 4, 5, 9, 100][whereChange] / 100

        colorN = 1
        if color == "b":
            colorN = 0

        typeFig.append(cost)
        typeFig.append(colorN)
        typeFig.extend([position[0] / 8, position[1] / 8])

        return typeFig