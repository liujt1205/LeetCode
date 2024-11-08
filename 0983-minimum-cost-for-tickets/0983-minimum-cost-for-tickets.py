class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last = days[-1]
        minCost = [0] * (last + 1)
        i = 0
        for day in range(1, last + 1):
            if day < days[i]:
                minCost[day] = minCost[day - 1]
            else:
                i += 1
                minCost[day] = min(minCost[day - 1] + costs[0], minCost[max(0, day - 7)] + costs[1], minCost[max(0, day - 30)] + costs[2])
                
        return minCost[last]