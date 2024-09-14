class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        largest = 0
        cur = 0
        for num in nums:
            if num > largest:
                largest = num
                cur = 1
                res = 1
            elif num < largest:
                cur = 0
            else:
                cur += 1
                res = max(res, cur)
                
        return res