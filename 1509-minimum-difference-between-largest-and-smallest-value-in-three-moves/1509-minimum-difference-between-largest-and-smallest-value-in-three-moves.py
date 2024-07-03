class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        large = []
        small = []
        for num in nums:
            heapq.heappush(large, num)
            heapq.heappush(small, -num)
            if len(large) > 4:
                heapq.heappop(large)
            if len(small) > 4:
                heapq.heappop(small)
        large.sort()
        newSmall = [-i for i in small]
        newSmall.sort()
        res = float('inf')
        for i in range(4):
            res = min(res, large[i] - newSmall[i])
        return res