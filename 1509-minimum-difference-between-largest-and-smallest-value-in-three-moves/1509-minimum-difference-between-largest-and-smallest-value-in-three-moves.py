class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        small = sorted(heapq.nsmallest(4, nums))
        large = sorted(heapq.nlargest(4, nums))
        res = float('inf')
        for i in range(4):
            res = min(res, large[i] - small[i])
        return res