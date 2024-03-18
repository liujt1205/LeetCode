class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        curStart = -float('inf')
        curStop = -float('inf')
        res = 0
        points.sort()
        for i in range(len(points)):
            start, stop = points[i]
            if start > curStop:
                res += 1
                curStart = start
                curStop = stop
            else:
                curStart = max(curStart, start)
                curStop = min(curStop, stop)
        return res