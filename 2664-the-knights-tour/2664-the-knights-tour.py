class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        board = [[-1] * n for _ in range(m)]
        queue = deque()
        queue.append((r, c))
        def explore(row, col, count):
            if (not 0 <= row < m) or (not 0 <= col < n) or board[row][col] != -1:
                return False
            board[row][col] = count

            if count + 1 == m * n:
                return True
            
            res = False
            for dr, dc in [(-2, -1), (-1, -2), (2, -1), (-1, 2), (-2, 1), (1, -2), (1, 2), (2, 1)]:
                newRow = row + dr
                newCol = col + dc
                res = res or explore(newRow, newCol, count + 1)
            
            if not res:
                board[row][col] = -1
            return res
            
        explore(r, c, 0)
        return board