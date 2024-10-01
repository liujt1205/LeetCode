class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            elif mid + 1 < len(nums) and nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                return mid