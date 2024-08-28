class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid1), len(grid1[0])
        
        def sink(row, col, grid2):
            if row < 0 or row >= m or col < 0 or col >= n or grid2[row][col] == 0:
                return
            grid2[row][col] = 0
            sink(row - 1, col, grid2)
            sink(row + 1, col, grid2)
            sink(row, col - 1, grid2)
            sink(row, col + 1, grid2)

        for row in range(m):
            for col in range(n):
                if grid2[row][col] > 0 and grid1[row][col] == 0:
                    sink(row, col, grid2)
        
        res = 0
        
        for row in range(m):
            for col in range(n):
                if grid2[row][col] > 0:
                    res += 1
                    sink(row, col, grid2)
        
        return res