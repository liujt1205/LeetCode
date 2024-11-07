class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        if x < y:
            x, y = y, x
        if x == 1 and y == 0:
            return 3
        if x == 1 and y == 1:
            return 2
        dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        queue = deque([(0, 0, 0)])
        visited = set()
        while queue:
            row, col, step = queue.popleft()
            if row == x and col == y:
                return step
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for dr, dc in dirs:
                newRow = row + dr
                newCol = col + dc
                if newRow >= 0 and newCol >= 0 and (newRow, newCol) not in visited:
                    queue.append((newRow, newCol, step + 1))
                    