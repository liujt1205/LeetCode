class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k = len(costs[0])
        prev = [0] * k
        first = 0
        second = 0
        for cost in costs:
            cur = [0] * k
            curFirst = float('inf')
            curSecond = float('inf')
            for i in range(k):
                if prev[i] == first:
                    cur[i] = cost[i] + second
                else:
                    cur[i] = cost[i] + first
                if cur[i] < curFirst:
                    curSecond = curFirst
                    curFirst = cur[i]
                elif cur[i] < curSecond:
                    curSecond = cur[i]
            
            first = curFirst
            second = curSecond
            prev = cur
        
        return min(prev)