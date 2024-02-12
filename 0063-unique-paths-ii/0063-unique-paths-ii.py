class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]:
                break
            else:
                memo[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i]:
                break
            else:
                memo[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[m - 1][n - 1]