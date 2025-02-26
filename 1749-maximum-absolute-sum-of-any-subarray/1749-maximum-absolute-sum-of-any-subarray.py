class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = 0
        prefix_sum = 0
        prefix_min = 0
        prefix_max = 0
        for num in nums:
            prefix_sum += num
            res = max(res, abs(prefix_sum - prefix_min), abs(prefix_sum - prefix_max))
            prefix_min = min(prefix_min, prefix_sum)
            prefix_max = max(prefix_max, prefix_sum)

        return res