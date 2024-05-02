class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if -nums[left] == nums[right]:
                return nums[right]
            elif -nums[left] < nums[right]:
                right -= 1
            elif -nums[left] > nums[right]:
                left += 1
        return -1