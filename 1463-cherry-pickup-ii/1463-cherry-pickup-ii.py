class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[[-1] * col for _ in range(col)] for _ in range(row)]
        dp[0][0][col - 1] = grid[0][0] + grid[0][col - 1]
        
        def getAbove(i, left, right):
            res = -1
            for first in range(left - 1, left + 2):
                for second in range(right - 1, right + 2):
                    if first >= 0 and second < col and first < second:
                        res = max(res, dp[i - 1][first][second])
            return res
            
        for i in range(1, row):
            for left in range(col - 1):
                for right in range(left + 1, col):
                    pre = getAbove(i, left, right)
                    if pre != -1:
                        dp[i][left][right] = grid[i][left] + grid[i][right] + pre
        res = 0
        for left in range(col - 1):
            res = max(res, max(dp[row - 1][left]))
        return res