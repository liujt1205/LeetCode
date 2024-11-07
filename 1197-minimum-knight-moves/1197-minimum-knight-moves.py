class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
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
                if (newRow, newCol) not in visited:
                    queue.append((newRow, newCol, step + 1))
                    