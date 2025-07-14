class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        dp = [False, False] + [True] * (n - 2)

        for i in range(2, int(sqrt(n)) + 1):
            if dp[i]:
                for mul in range(i * i, n, i):
                    dp[mul] = False

        return sum(dp)