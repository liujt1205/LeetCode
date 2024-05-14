class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def expand(grid, row, col, count):
            nonlocal res
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                res = max(res, count)
            else:
                cur = grid[row][col]
                grid[row][col] = 0
                expand(grid, row+1, col, count+cur)
                expand(grid, row, col+1, count+cur)
                expand(grid, row-1, col, count+cur)
                expand(grid, row, col-1, count+cur)
                grid[row][col] = cur
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                expand(grid, i, j, 0)
        return res