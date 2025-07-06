class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            if i > 0:
                dp[0][i] += dp[0][i - 1]
            dp[0][i] += grid[0][i]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]

        return dp[m - 1][n - 1]