class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = [[-1] * n for _ in range(n)]
        queue = deque()
        queue.append((0, 0, 0))
        while queue:
            row, col, step = queue.popleft()
            if not 0 <= row < n or not 0 <= col < n or grid[row][col] == 1 or memo[row][col] != -1:
                continue
            memo[row][col] = step + 1
            queue.append((row - 1, col - 1, step + 1))
            queue.append((row - 1, col, step + 1))
            queue.append((row - 1, col + 1, step + 1))
            queue.append((row, col - 1, step + 1))
            queue.append((row, col + 1, step + 1))
            queue.append((row + 1, col - 1, step + 1))
            queue.append((row + 1, col, step + 1))
            queue.append((row + 1, col + 1, step + 1))

        return memo[n - 1][n - 1]