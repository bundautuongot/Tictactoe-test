def isEndGame(self, board):
    for x in range(2, self.SIZE - 2):
        for y in range(2, self.SIZE - 2):
            if board[x][y] != 0:
                if board[x][y] == board[x][y - 1] == board[x][y + 1] == board[x][y + 2] == board[x][y - 2]:
                    return board[x][y]
                elif (board[x][y] == board[x - 1][y] == board[x + 1][y]
                      == board[x + 2][y] == board[x - 2][y]):
                    return board[x][y]
                elif (board[x][y] == board[x + 1][y + 1] == board[x - 1][y - 1]
                      == board[x + 2][y + 2] == board[x - 2][y - 2]):
                    return board[x][y]
                elif (board[x][y] == board[x - 1][y + 1] == board[x - 1][y + 1]
                      == board[x - 2][y + 2] == board[x - 2][y + 2]):
                    return board[x][y]
    for x in range(self.SIZE):
        for y in range(self.SIZE):
            if (board[x][y]) == 0:
                return 2
    return 0