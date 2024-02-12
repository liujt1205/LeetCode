class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        state = (0, 0, k)
        seen = set([state])
        queue = deque()
        queue.append([0, state])
        while queue:
            steps, (row, col, left) = queue.popleft()
            if row == m - 1 and col == n - 1:
                return steps
            for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= i < m and 0 <= j < n:
                    newLeft = left - grid[i][j]
                    newState = (i, j, newLeft)
                    if newLeft >= 0 and newState not in seen:
                        seen.add(newState)
                        queue.append([steps + 1, newState])
        return -1