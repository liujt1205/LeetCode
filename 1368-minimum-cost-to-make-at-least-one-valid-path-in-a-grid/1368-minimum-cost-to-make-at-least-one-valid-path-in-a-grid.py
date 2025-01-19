class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        min_cost = [[float("inf")] * m for _ in range(n)]
        min_cost[0][0] = 0

        queue = deque([(0, 0)])

        while queue:
            row, col = queue.popleft()

            for idx, (dx, dy) in enumerate(dirs):
                newRow, newCol = row + dx, col + dy
                cost = 0 if grid[row][col] == idx + 1 else 1

                if (0 <= newRow < n and 0 <= newCol < m 
                    and min_cost[row][col] + cost < min_cost[newRow][newCol]):
                    min_cost[newRow][newCol] = min_cost[row][col] + cost
                    if cost == 1:
                        queue.append((newRow, newCol))
                    else:
                        queue.appendleft((newRow, newCol))

        return min_cost[n - 1][m - 1]
