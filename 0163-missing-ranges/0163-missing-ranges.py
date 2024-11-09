class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        
        res = []
        prev = lower - 1
        for num in nums:
            lo = prev + 1
            hi = num - 1
            if lo <= hi:
                res.append([lo, hi])
            prev = num
        
        if nums[-1] < upper:
            res.append([nums[-1] + 1, upper])
                
        return res
        