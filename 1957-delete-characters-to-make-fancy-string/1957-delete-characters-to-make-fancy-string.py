class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 0
        res = ""
        for char in s:
            if not res or char != res[-1]:
                res += char
                count = 1
            elif count < 2:
                res += char
                count += 1
            else:
                continue
                
        return res