class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        
        res = []
        for i, num in enumerate(nums):
            if num < lower:
                continue
            elif num > upper:
                prev = lower if i == 0 else max(lower, nums[i - 1] + 1)
                res.append([prev, upper])
                break
            elif i == 0 and num > lower:
                res.append([lower, num - 1])
            elif i > 0 and num - nums[i - 1] > 1:
                res.append([max(lower, nums[i - 1] + 1), num - 1])
        
        if nums[-1] < upper:
            res.append([max(nums[-1] + 1, lower), upper])
                
        return res
        