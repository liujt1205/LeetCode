class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        delete = 1
        res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                delete -= 1
            while delete < 0:
                if nums[left] == 0:
                    delete += 1
                left += 1
            res = max(res, right - left)
            
        return res