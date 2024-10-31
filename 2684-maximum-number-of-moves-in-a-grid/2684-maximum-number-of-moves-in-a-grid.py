class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = [0] * m
        res = 0
        for col in range(1, n):
            cur = [0] * m
            curBest = 0
            for row in range(m):
                if row - 1 >= 0 and grid[row][col] > grid[row - 1][col - 1] and (col - 1 == 0 or prev[row - 1] != 0):
                    cur[row] = max(cur[row], prev[row - 1] + 1)
                if grid[row][col] > grid[row][col - 1]  and (col - 1 == 0 or prev[row] != 0):
                    cur[row] = max(cur[row], prev[row] + 1)
                if row + 1 < m and grid[row][col] > grid[row + 1][col - 1]  and (col - 1 == 0 or prev[row + 1] != 0):
                    cur[row] = max(cur[row], prev[row + 1] + 1)
                curBest = max(curBest, cur[row])
            if curBest == 0:
                break
            res = max(res, curBest)
            prev = cur
        return res