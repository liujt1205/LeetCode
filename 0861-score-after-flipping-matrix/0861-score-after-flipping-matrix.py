class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]   
        for j in range(1, n):
            count = 0
            for i in range(m):
                if grid[i][j] == 0:
                    count += 1
            if count > m - count:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]          
        res = 0
        for i in range(m):
            for j in range(n):
                columnScore = grid[i][j] << (n - j - 1)
                res += columnScore
        return res