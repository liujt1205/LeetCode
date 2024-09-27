class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1]:
                memo[i] += memo[i - 1]
            memo[i] += 1
            
        return sum(memo)