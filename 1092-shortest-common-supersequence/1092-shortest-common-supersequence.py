class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(A, B):
            n, m = len(A), len(B)
            dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
            for i in range(n):
                for j in range(m):
                    if A[i] == B[j]:
                        dp[i + 1][j + 1] = dp[i][j] + A[i]
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
            return dp[-1][-1]

        res, i, j = "", 0, 0
        for c in lcs(str1, str2):
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i, j = i + 1, j + 1
        return res + str1[i:] + str2[j:]
            