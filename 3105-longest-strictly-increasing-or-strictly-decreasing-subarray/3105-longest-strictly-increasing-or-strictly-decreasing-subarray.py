class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        increasing = 1
        decreasing = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing += 1
                decreasing = 1
            elif nums[i] < nums[i - 1]:
                decreasing += 1
                increasing = 1
            else:
                increasing = 1
                decreasing = 1

            res = max(res, increasing, decreasing)

        return res
            