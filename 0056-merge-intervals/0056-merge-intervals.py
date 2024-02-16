class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for interval in intervals:
            start, end = interval
            if res and res[-1][0] <= start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(interval)
        return res