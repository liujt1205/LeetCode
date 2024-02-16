class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(row, col):
            if grid[row][col] == "1":
                grid[row][col] = "2"
                for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                        explore(i, j)
                        
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    res += 1
                    explore(row, col)
                    
        return res