class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for index in range(len(s)):
            if index % 2 == 1 and s[index] != s[index - 1]:
                res += 1
            
        return res