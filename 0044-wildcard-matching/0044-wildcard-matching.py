class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 1]

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '?' or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1]

        return dp[len(s)][len(p)]