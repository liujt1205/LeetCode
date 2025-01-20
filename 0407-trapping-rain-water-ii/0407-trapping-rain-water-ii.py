class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        visited = [[False] * m for _ in range(n)]
        boundary = []
        for i in range(n):
            heapq.heappush(boundary, (heightMap[i][0], i, 0))
            heapq.heappush(boundary, (heightMap[i][m - 1], i, m - 1))
            visited[i][0] = visited[i][m - 1] = True

        for i in range(m):
            heapq.heappush(boundary, (heightMap[0][i], 0, i))
            heapq.heappush(boundary, (heightMap[n - 1][i], n - 1, i))
            visited[0][i] = visited[n - 1][i] = True

        res = 0
        while boundary:
            height, row, col = heapq.heappop(boundary)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newRow = row + dr
                newCol = col + dc
                if 0 <= newRow < n and 0 <= newCol < m and not visited[newRow][newCol]:
                    next_height = heightMap[newRow][newCol]
                    if next_height < height:
                        res += height - next_height
                    heapq.heappush(boundary, (max(height, next_height), newRow, newCol))
                    visited[newRow][newCol] = True

        return res