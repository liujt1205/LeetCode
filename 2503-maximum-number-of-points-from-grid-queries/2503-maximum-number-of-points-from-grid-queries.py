class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        minCost = [[float('inf')] * n for _ in range(m)]
        totalMin = 0
        pq = [(grid[0][0], 0, 0)]
        while pq:
            curMin, row, col = heapq.heappop(pq)
            if minCost[row][col] != float('inf'):
                continue
            minCost[row][col] = curMin
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newRow = row + dr
                newCol = col + dc
                if 0 <= newRow < m and 0 <= newCol < n and minCost[newRow][newCol] == float('inf'):
                    newCost = max(curMin, grid[newRow][newCol])
                    heapq.heappush(pq, (newCost, newRow, newCol))

        costs = []
        for i in range(m):
            for j in range(n):
                costs.append(minCost[i][j])

        costs.sort()
        print(costs)
        res = []
        for q in queries:
            left, right = 0, n * m - 1
            while left <= right:
                mid = (left + right) // 2
                if costs[mid] < q:
                    left = mid + 1
                else:
                    right = mid - 1
            res.append(left)
        
        return res