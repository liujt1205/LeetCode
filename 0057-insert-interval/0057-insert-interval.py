class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, stop = newInterval
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= stop:
            start = min(start, intervals[i][0])
            stop = max(stop, intervals[i][1])
            i += 1
        res.append([start, stop])
        
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
            
        return res