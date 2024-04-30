class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        prefix = 0
        res = 0
        for num in nums:
            prefix += num
            res |= num 
            res |= prefix
        return res