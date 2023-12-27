class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        highest = neededTime[0]
        cur = colors[0]
        n = len(colors)
        for i in range(1, n):
            if colors[i] == cur:
                res += min(highest, neededTime[i])
                highest = max(highest, neededTime[i])
            else:
                highest = neededTime[i]
                cur = colors[i]
        return res