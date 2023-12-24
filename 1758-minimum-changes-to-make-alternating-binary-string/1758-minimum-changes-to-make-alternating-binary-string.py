class Solution:
    def minOperations(self, s: str) -> int:
        start1 = 0
        start0 = 0
        for i in range(len(s)):
            start1 += s[i] != str((i + 1) % 2)
            start0 += s[i] != str(i % 2)
        return min(start1, start0)