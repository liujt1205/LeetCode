class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            rem = num % k
            for i in range(k):
                dp[rem][i] = dp[i][rem] + 1
                res = max(res, dp[rem][i])

        return res