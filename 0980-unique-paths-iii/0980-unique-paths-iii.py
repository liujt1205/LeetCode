class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        res = [0]
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                elif grid[i][j] == 1:
                    startRow = i
                    startCol = j
        def explore(row, col, visited):
            if grid[row][col] == 2:
                res[0] += visited == (count + 1)
            elif grid[row][col] != -1:
                grid[row][col] = -1
                for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if 0 <= i < m and 0 <= j < n:
                        explore(i, j, visited + 1)
                grid[row][col] = 0
        explore(startRow, startCol, 0)
        return res[0]
                