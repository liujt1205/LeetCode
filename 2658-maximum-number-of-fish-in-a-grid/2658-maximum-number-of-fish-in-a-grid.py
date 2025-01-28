class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def bfs(row, col):
            nonlocal grid
            fish = 0
            if 0 <= row < m and 0 <= col < n and grid[row][col] > 0:
                fish += grid[row][col]
                grid[row][col] = 0
                for dr, dc in dirs:
                    newRow = row + dr
                    newCol = col + dc
                    fish += bfs(newRow, newCol)

            return fish
            
        for row in range(m):
            for col in range(n):
                if grid[row][col] > 0:
                    res = max(res, bfs(row, col))

        return res