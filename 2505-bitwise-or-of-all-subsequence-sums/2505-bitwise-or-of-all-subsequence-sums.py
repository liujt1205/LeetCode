class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        prefix = 0
        res = 0
        for num in nums:
            prefix += num
            res |= num | prefix
        return res