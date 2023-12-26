class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = [[0] * (target + 1) for _ in range(n + 1)]
        memo[n][target] = 1
        mod = 1000000007
        for i in range(n - 1, -1, -1):
            for j in range(target + 1):
                ways = 0
                for l in range(1, min(k, target - j) + 1):
                    ways = (ways + memo[i + 1][j + l]) % mod
                memo[i][j] = ways
        return memo[0][0]