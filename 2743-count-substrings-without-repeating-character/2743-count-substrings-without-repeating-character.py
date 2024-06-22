class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        freq = [0] * 26
        res = 0
        left = -1
        for right in range(len(s)):
            freq[ord(s[right]) - ord('a')] += 1
            while freq[ord(s[right]) - ord('a')] > 1:
                left += 1
                freq[ord(s[left]) - ord('a')] -= 1
            res += right - left
        return res