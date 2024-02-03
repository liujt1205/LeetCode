class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (k + 1)
        for left in range(len(arr) - 1, -1, -1):
            curMax = 0
            right = min(len(arr), left + k)
            for i in range(left, right):
                curMax = max(curMax, arr[i])
                dp[left % (k + 1)] = max(dp[left % (k + 1)], dp[(i + 1) % (k + 1)] + curMax * (i - left + 1))
        return dp[0]
        