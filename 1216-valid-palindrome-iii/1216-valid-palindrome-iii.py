class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        memo = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    memo[i][j] = memo[i + 1][j - 1]
                else:
                    memo[i][j] = 1 + min(memo[i + 1][j], memo[i][j - 1])
        return memo[0][n - 1] <= k
        