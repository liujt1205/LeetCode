class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for num in nums:
            total += num
        return (1 + n) * n // 2 - total