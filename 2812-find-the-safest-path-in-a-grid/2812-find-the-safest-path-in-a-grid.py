class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distance = [[-1] * n for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    distance[i][j] = 0
        while queue:
            size = len(queue)
            while size > 0:
                cur = queue.popleft()
                for delta in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    newRow, newCol = cur[0] + delta[0], cur[1] + delta[1]
                    if 0 <= newRow < n and 0 <= newCol < n and distance[newRow][newCol] == -1:
                        distance[newRow][newCol] = distance[cur[0]][cur[1]] + 1
                        queue.append((newRow, newCol)) 
                size -= 1
        
        def explore(distance, limit):
            n = len(grid)
            if distance[0][0] < limit or distance[n-1][n-1] < limit:
                return False
            queue = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            while queue:
                cur = queue.popleft()
                if cur[0] == n - 1 and cur[1] == n - 1:
                    return True
                for delta in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    newRow, newCol = cur[0] + delta[0], cur[1] + delta[1]
                    if 0 <= newRow < n and 0 <= newCol < n and not visited[newRow][newCol] and distance[newRow][newCol] >= limit:
                        visited[newRow][newCol] = True
                        queue.append((newRow, newCol))
            return False
        
        start, end, res = 0, n, -1
        while start <= end:
            mid = start + (end - start) // 2
            if explore(distance, mid):
                res = mid
                start = mid + 1
            else:
                end = mid - 1
        return res