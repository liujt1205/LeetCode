class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        pre = [0] * n
        for i in range(n):
            cur = pre[:]
            heapq.heapify(cur)
            smallest = heapq.heappop(cur)
            second = heapq.heappop(cur)
            for j in range(n):
                if pre[j] == smallest:
                    pre[j] = second + grid[i][j]
                else:
                    pre[j] = smallest + grid[i][j]
        res = float('inf')
        for i in range(n):
            res = min(res, pre[i])
        return res