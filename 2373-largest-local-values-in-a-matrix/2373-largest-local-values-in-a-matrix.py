class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        largest = [[0] * n for _ in range(n)]
        def expand(row, col):
            nonlocal largest, grid, n
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 < row + i < n and 0 < col + j < n:
                        largest[row + i][col + j] = max(largest[row + i][col + j], grid[row][col])
            
        for i in range(n):
            for j in range(n):
                expand(i, j)
        
        for i in range(n - 2):
            for j in range(n - 2):
                res[i][j] = largest[i + 1][j + 1]
        
        return res