class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        memo = [0] * (k + 1)
        mod = 1000000007
        for i in range(1, n + 1):
            cur = [0] * (k + 1)
            cur[0] = 1
            for j in range(1, k + 1):
                count = (memo[j] + mod - (memo[j - i] if j >= i else 0)) % mod
                cur[j] = (cur[j - 1] + count) % mod
            memo = cur
        return ((memo[k] + mod - (memo[k - 1] if k else 0)) % mod)