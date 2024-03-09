class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            return self.getCommon(nums2, nums1)
        
        def binarySearch(target, nums):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        
        for num in nums1:
            if binarySearch(num, nums2):
                return num
            
        return -1