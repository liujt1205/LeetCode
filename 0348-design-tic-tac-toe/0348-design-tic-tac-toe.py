class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        res = 0
        if res == 0 and row == col:
            res = self.checkMain(player)
        if res == 0 and row + col == len(self.board) - 1:
            res = self.checkDiag(player)
        if res == 0:
            res = self.checkCol(col, player)
        if res == 0:
            res = self.checkRow(row, player)
        
        return res
    
    def checkMain(self, player):
        for i in range(len(self.board)):
            if self.board[i][i] != player:
                return 0
        return player
    
    def checkDiag(self, player):
        for i in range(len(self.board)):
            if self.board[i][len(self.board) - 1 - i] != player:
                return 0
        return player
    
    def checkCol(self, col, player):
        for i in range(len(self.board)):
            if self.board[i][col] != player:
                return 0
        return player
    
    def checkRow(self, row, player):
        for i in range(len(self.board)):
            if self.board[row][i] != player:
                return 0
        return player

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)