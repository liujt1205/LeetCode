class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        res = []
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left < len(nums) and nums[left] == target:
            res.append(left)
        else:
            res.append(-1)
            
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        if right >= 0 and nums[right] == target:
            res.append(right)
        else:
            res.append(-1)
            
        return res