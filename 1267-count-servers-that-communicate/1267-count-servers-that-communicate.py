class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    rows[row] += 1
                    cols[col] += 1

        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and rows[row] > 1 and cols[col] > 1:
                    res -= 1

        for row in range(m):
            if rows[row] > 1:
                res += rows[row]
        
        for col in range(n):
            if cols[col] > 1:
                res += cols[col]

        return res