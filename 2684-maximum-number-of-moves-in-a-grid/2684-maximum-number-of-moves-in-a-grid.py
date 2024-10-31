class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[0] * n for _ in range(m + 2)]
        res = 0
        for col in range(1, n):
            for row in range(1, m + 1):
                if row - 2 >= 0 and grid[row - 1][col] > grid[row - 2][col - 1] and (col - 1 == 0 or memo[row - 2][col - 1] != 0):
                    memo[row - 1][col] = max(memo[row - 1][col], memo[row - 2][col - 1] + 1)
                if grid[row - 1][col] > grid[row - 1][col - 1]  and (col - 1 == 0 or memo[row - 1][col - 1] != 0):
                    memo[row - 1][col] = max(memo[row - 1][col], memo[row - 1][col - 1] + 1)
                if row < m and grid[row - 1][col] > grid[row][col - 1]  and (col - 1 == 0 or memo[row][col - 1] != 0):
                    memo[row - 1][col] = max(memo[row - 1][col], memo[row][col - 1] + 1)
                res = max(res, memo[row - 1][col])
        return res