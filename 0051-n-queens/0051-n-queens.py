class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        rows = [0] * n
        self.column = 0
        self.majorDiagonal = 0
        self.minorDiagonal = 0
        def getBoard(rows):
            board = []
            for row in range(n):
                cur = ""
                for col in range(n):
                    if rows[row] & (1 << col):
                        cur = "Q" + cur
                    else:
                        cur = "." + cur
                board.append(cur)
            return board
            
        def tryRow(row):
            if row == n:
                board = getBoard(rows)
                res.append(board)
            else:
                for col in range(n):
                    if rows[row] == 0:
                        rows[row] = 1
                    else:
                        rows[row] = rows[row] << 1
                    noConflict = ((rows[row] & self.column) == 0) and ((rows[row] & self.majorDiagonal) == 0) and ((rows[row] & self.minorDiagonal) == 0)
                    if noConflict:
                        prevCol = self.column
                        prevMajor = self.majorDiagonal
                        prevMinor = self.minorDiagonal
                        self.column = self.column | rows[row]
                        self.majorDiagonal = self.majorDiagonal | rows[row]
                        self.minorDiagonal = self.minorDiagonal | rows[row]
                        self.majorDiagonal = self.majorDiagonal >> 1
                        self.minorDiagonal = self.minorDiagonal << 1
                        tryRow(row + 1)
                        self.column = prevCol
                        self.majorDiagonal = prevMajor
                        self.minorDiagonal = prevMinor
                rows[row] = 0
                
        tryRow(0)
        return res
                        