class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0 or m < k:
            return 0
        memo = [[0] * (m + 1) for _ in range(k + 1)]
        mod = 1000000007
        for i in range(1, m + 1):
            memo[1][i] = 1
        for i in range(1, n):
            cur = [[0] * (m + 1) for _ in range(k + 1)]
            for j in range(1, min(i + 1, k) + 1):
                for h in range(j, m + 1):
                    cur[j][h] = (cur[j][h] + memo[j][h] * h) % mod
                    for second in range(1, h):
                        cur[j][h] = (cur[j][h] + memo[j - 1][second] ) % mod
            memo = cur
        return sum(memo[k]) % mod