class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n == 0:
            return True
        i = 0
        j = 0
        while(i < m):
            if s[j] == t[i]:
                j += 1
            i += 1
            if j == n:
                return True
        return False