class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        word = False
        res = 0
        for i in range(n):
            if word and s[n - 1 - i] == ' ':
                return res
            if s[n - 1 - i] != ' ':
                word = True
                res += 1
        return res