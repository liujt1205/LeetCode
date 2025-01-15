class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            if queue:
                break
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    grid[i][j] = 0
                    queue.append((i, j, 0))
                    break
        
        def valid(row, col, grid):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 'X':
                return True
            return False

        while queue:
            row, col, step = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newRow = row + dr
                newCol = col + dc
                if valid(newRow, newCol, grid):
                    queue.append((newRow, newCol, step + 1))
                    if grid[newRow][newCol] == '#':
                        return step + 1
                    grid[newRow][newCol] = 'X'

        return -1

