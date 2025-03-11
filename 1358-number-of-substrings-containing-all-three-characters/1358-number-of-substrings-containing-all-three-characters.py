class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1] * 3
        res = 0

        for i in range(len(s)):
            last[ord(s[i]) - ord('a')] = i
            res += 1 + min(last)

        return res