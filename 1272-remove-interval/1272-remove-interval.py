class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        remove = 0
        lower, upper = toBeRemoved
        for interval in intervals:
            start, end = interval
            if start >= upper or end < lower:
                res.append([start, end])
            else:
                if start < lower:
                    res.append([start, lower])
                if end > upper:
                    res.append([upper, end])
        return res