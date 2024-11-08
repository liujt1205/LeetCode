class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= intervals[prev][1]:
                prev = i
            else:
                res += 1
                if end <= intervals[prev][1]:
                    prev = i
                
        return res