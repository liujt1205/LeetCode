class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid == len(nums) - 1:
                return nums[mid]

            if mid % 2 == 0 and nums[mid] == nums[mid + 1]:
                left = mid + 2
            elif mid % 2 == 0 and nums[mid] != nums[mid + 1]:
                right = mid
            elif mid % 2 != 0 and nums[mid] == nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1

        return nums[left]