class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for row, col in guards:
            grid[row][col] = 1
            
        for row, col in walls:
            grid[row][col] = 2
            
        def markRow(row, col):
            newRow = row
            while newRow < m and grid[newRow][col] != 2:
                grid[newRow][col] -= 2
                newRow += 1
            newRow = row
            while newRow >= 0 and grid[newRow][col] != 2:
                grid[newRow][col] -= 2
                newRow -= 1
        
        def markCol(row, col):
            newCol = col
            while newCol < n and grid[row][newCol] != 2:
                grid[row][newCol] -= 3
                newCol += 1
            newCol = col
            while newCol >= 0 and grid[row][newCol] != 2:
                grid[row][newCol] -= 3
                newCol -= 1
            
        for row, col in guards:
            if grid[row][col] > 0:
                markRow(row, col)
                markCol(row, col)
                grid[row][col] = -4
            elif grid[row][col] == -1:
                markCol(row, col)
                grid[row][col] = -4
            elif grid[row][col] == -2:
                markRow(row, col)
            else:
                continue
                
        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    res += 1
                    
        return res