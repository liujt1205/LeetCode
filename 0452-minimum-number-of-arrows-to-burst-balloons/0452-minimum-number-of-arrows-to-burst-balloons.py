class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        curStop = -float('inf')
        res = 0
        points.sort()
        for start, stop in points:
            if start > curStop:
                res += 1
                curStop = stop
            else:
                curStop = min(curStop, stop)
        return res