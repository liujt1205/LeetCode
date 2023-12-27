class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
        left = 0
        for i in range(len(nums)):
            total -= nums[i]
            if left == total:
                return i
            left += nums[i]
        return -1