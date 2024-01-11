class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        curSum = -float('inf')
        res = -float('inf')
        while i < n:
            if curSum < 0:
                curSum = nums[i]
            else:
                curSum += nums[i]
            res = max(res, curSum)
            i += 1
        return res
        