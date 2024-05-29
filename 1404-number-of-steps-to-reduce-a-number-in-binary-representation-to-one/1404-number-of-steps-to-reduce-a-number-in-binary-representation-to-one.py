class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        leftover = 0
        for i in range(len(s) - 1, 0, -1):
            cur = (int(s[i]) + leftover) % 2
            leftover = (int(s[i]) + leftover) // 2
            if cur == 0:
                res += 1
            else:
                res += 2
                leftover = 1
        if leftover == 1:
            res += 1
        return res
            
            