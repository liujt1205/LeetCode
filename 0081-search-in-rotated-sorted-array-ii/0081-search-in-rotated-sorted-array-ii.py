class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[left]:
                left += 1
                continue
            if nums[left] < target < nums[mid] or nums[mid] < nums[left] < target or target < nums[mid] < nums[left]:
                right = mid - 1
            elif nums[left] < nums[mid] < target or nums[left] > target > nums[mid] or target < nums[left] < nums[mid]:
                left = mid + 1
            else:
                break
                
        return (left < len(nums) and nums[left] == target) or (right >= 0 and nums[right] == target)
            