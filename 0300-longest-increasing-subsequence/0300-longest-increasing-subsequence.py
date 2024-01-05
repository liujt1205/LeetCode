class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)
        for i in range(1, len(nums)):
            cur = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    cur = max(cur, 1 + memo[j])
            memo[i] = cur
        res = 0
        for i in range(len(nums)):
            if memo[i] > res:
                res = memo[i]
        return res