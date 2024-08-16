class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            curSmallest = arrays[i][0]
            curBiggest = arrays[i][-1]
            res = max(res, abs(curBiggest - smallest))
            res = max(res, abs(curSmallest - biggest))
            smallest = min(smallest, curSmallest)
            biggest = max(biggest, curBiggest)
        return res