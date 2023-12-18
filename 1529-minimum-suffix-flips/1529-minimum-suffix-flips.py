class Solution:
    def minFlips(self, target: str) -> int:
        pre = '0'
        res = 0
        for c in target:
            if c != pre:
                res += 1
                pre = c
        return res