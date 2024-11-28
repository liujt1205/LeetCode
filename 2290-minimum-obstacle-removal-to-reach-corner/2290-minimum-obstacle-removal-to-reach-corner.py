class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_remove = [[float('inf')] * n for _ in range(m)]
        min_remove[0][0] = 0
        queue = deque([(0, 0, 0)])
        while queue:
            count, row, col = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and min_remove[new_row][new_col] == float('inf'):
                    if grid[new_row][new_col] == 1:
                        min_remove[new_row][new_col] = count + 1
                        queue.append((count + 1, new_row, new_col))
                    else:
                        min_remove[new_row][new_col] = count
                        queue.appendleft((count, new_row, new_col))
                        
        return min_remove[m - 1][n - 1]