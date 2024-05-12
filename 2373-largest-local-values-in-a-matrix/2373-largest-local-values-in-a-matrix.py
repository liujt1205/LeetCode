class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        
        def findMax(row, col, grid, n):
            maxVal = 0
            for i in range(3):
                for j in range(3):
                    maxVal = max(maxVal, grid[row + i][col + j])
            return maxVal
        
        for i in range(n - 2):
            for j in range(n - 2):
                res[i][j] = findMax(i, j, grid, n)
        
        return res