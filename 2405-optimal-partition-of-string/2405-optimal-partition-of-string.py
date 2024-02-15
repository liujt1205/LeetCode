class Solution:
    def partitionString(self, s: str) -> int:
        seen = [0] * 26
        res = 0
        for char in s:
            seen[ord(char) - ord('a')] += 1
            if seen[ord(char) - ord('a')] > 1:
                res += 1
                seen = [0] * 26
                seen[ord(char) - ord('a')] += 1
        return res + 1