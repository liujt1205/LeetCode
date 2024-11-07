class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        m, n = len(board), len(board[0])
        
        def reveal(row, col):
            if not (0 <= row < m and 0 <= col < n) or board[row][col] != 'E':
                return
            count = countMines(row, col)
            if count != 0:
                board[row][col] = str(count)
                return
            board[row][col] = 'B'
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                newRow = row + dx
                newCol = col + dy
                reveal(newRow, newCol)
                
        def countMines(row, col):
            res = 0
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                newRow = row + dx
                newCol = col + dy
                if 0 <= newRow < m and 0 <= newCol < n and board[newRow][newCol] == 'M':
                    res += 1
                    
            return res
        
        reveal(click[0], click[1])
        return board