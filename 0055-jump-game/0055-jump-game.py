class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curMax = 0
        for i, num in enumerate(nums):
            if i > curMax:
                return False
            curMax = max(curMax, i + num)
            if curMax >= len(nums) - 1:
                return True