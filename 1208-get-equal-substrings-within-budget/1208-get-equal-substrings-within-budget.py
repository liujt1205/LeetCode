class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [0] * len(s)
        for i in range(len(s)):
            cost[i] = abs(ord(s[i]) - ord(t[i]))
        start = 0
        end = 0
        curCost = 0
        res = 0
        while end < len(s) and start <= end:
            curCost += cost[end]
            while curCost > maxCost:
                curCost -= cost[start]
                start += 1
            res = max(res, end - start + 1)
            end += 1
        return res