class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = []
        for point in points:
            xs.append(point[0])
        xs.sort()
        res = 0
        pre = xs[0]
        for i in range(len(xs)):
            res = max(res, xs[i] - pre)
            pre = xs[i]
        return res