class Solution:
    def check(self, s: str, i: int) -> int:
        res = 0
        single = 0
        while i - single >= 0 and i + single < len(s):
            if s[i - single] != s[i + single]:
                break
            single += 1
        res += single
        if i and s[i] == s[i - 1]:
            double = 0
            while i - 1 - double >= 0 and i + double < len(s):
                if s[i - 1 - double] != s[i + double]:
                    break
                double += 1
            res += double
        return res

    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.check(s, i)
        return res
