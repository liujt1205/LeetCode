class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        def explore(row, col):
            nonlocal res
            nonlocal grid
            nonlocal visited
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                res += 1
                return
            if grid[row][col] == 0:
                res += 1
            elif visited[row][col]:
                return
            else:
                visited[row][col] = True
                explore(row-1, col)
                explore(row+1, col)
                explore(row, col-1)
                explore(row, col+1)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    explore(i, j)
                    return res
        
        