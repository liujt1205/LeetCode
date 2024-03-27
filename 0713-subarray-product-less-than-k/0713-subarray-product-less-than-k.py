class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        cur = 1
        start = 0
        for i, num in enumerate(nums):
            cur *= num
            while cur >= k:
                cur /= nums[start]
                start += 1
            res += i - start + 1
        return res