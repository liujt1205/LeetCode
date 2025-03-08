class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        diff = 0
        count = [0] * 26
        for i in range(k):
            count[ord(s[i]) - ord('a')] += 1
            if count[ord(s[i]) - ord('a')] == 1:
                diff += 1

        res = 0 if diff != k else 1
        for i in range(k, len(s)):
            count[ord(s[i]) - ord('a')] += 1
            if count[ord(s[i]) - ord('a')] == 1:
                diff += 1
            count[ord(s[i - k]) - ord('a')] -= 1
            if count[ord(s[i - k]) - ord('a')] == 0:
                diff -= 1
            if diff == k:
                res += 1

        return res