class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        res = 0
        
        def dfs(matrix, i, j, memo):
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            if memo[i][j] != 0:
                return memo[i][j]
            for d in dirs:
                x = i + d[0]
                y = j + d[1]
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    memo[i][j] = max(memo[i][j], dfs(matrix, x, y, memo))
            
            memo[i][j] += 1
            return memo[i][j]
        
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(matrix, i, j, memo))
                
        return res
    
