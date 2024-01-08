class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        memo = [{} for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                memo[i][diff] = memo[j].get(diff, 0) + memo[i].get(diff, 0) + 1
                res += memo[j].get(diff, 0)
        return res