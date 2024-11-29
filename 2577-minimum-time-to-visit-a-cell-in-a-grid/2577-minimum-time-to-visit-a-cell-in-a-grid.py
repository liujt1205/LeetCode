class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        m, n = len(grid), len(grid[0])
        min_time = [[float('inf')] * n for _ in range(m)]
        min_time[0][0] = 0
        pq = []
        pq.append((0, 0, 0))
        while pq:
            count, row, col = heapq.heappop(pq)
            if row == m - 1 and col == n - 1:
                return count
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newRow = row + dr
                newCol = col + dc
                if 0 <= newRow < m and 0 <= newCol < n and min_time[newRow][newCol] == float('inf'):
                    if grid[newRow][newCol] <= count + 1:
                        min_time[newRow][newCol] = count + 1
                    else:
                        min_time[newRow][newCol] = grid[newRow][newCol] + (grid[newRow][newCol] - count - 1) % 2
                    heapq.heappush(pq, (min_time[newRow][newCol], newRow, newCol))
            
        return min_time[m - 1][n - 1] if min_time[m - 1][n - 1] != float('inf') else -1