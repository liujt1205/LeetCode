class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        pre = [0] * 3
        for i in range(1, n + 1):
            cur = [0] * 3
            cur[0] += costs[i - 1][0] + min(pre[1], pre[2])
            cur[1] += costs[i - 1][1] + min(pre[0], pre[2])
            cur[2] += costs[i - 1][2] + min(pre[0], pre[1])
            pre = cur
        return min(pre)