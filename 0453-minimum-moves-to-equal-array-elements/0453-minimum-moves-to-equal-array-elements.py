class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        res = 0
        for num in nums:
            res += num - minimum
            
        return res