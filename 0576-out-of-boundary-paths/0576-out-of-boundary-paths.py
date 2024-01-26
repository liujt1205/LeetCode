class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        board = [[0] * n for _ in range(m)]
        board[startRow][startColumn] = 1
        res = 0
        mod = 1000000007
        res += (startRow == 0) + (startRow == m - 1)
        res += (startColumn == n - 1) + (startColumn == 0)
        def updateBoard(board, curBoard, row, col):
            m, n = len(board), len(board[0])
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x = col + dx
                y = row + dy
                if 0 <= x < n and 0 <= y < m:
                    curBoard[row][col] += board[y][x]
        for i in range(maxMove - 1):
            curBoard = [[0] * n for _ in range(m)]
            for row in range(m):
                for col in range(n):
                    updateBoard(board, curBoard, row, col)
                    res += curBoard[row][col] * ((row == 0) + (row == m - 1))
                    res += curBoard[row][col] * ((col == n - 1) + (col == 0))
            board = curBoard
        return res % mod